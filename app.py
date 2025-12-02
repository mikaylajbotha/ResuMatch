from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
from openai import OpenAI
import json
import uuid
import re
import fitz  
try:
    import pytesseract
    from PIL import Image
except ImportError:
    pytesseract = None  

# Load environment variables
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("Please set your OPENAI_API_KEY in the .env file.")

client = OpenAI(api_key=OPENAI_API_KEY)

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.pdf', '.docx']
app.config['UPLOAD_FOLDER'] = 'uploads'

# -----------------------
# --- Text Extraction ---
# -----------------------
def extract_text(file_path, file_ext):
    text = ""
    if file_ext == ".pdf":
        doc = fitz.open(file_path)
        for page in doc:
            page_text = page.get_text()
            if not page_text.strip() and pytesseract:
                pix = page.get_pixmap()
                img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
                page_text = pytesseract.image_to_string(img)
            text += page_text + "\n"
    elif file_ext == ".docx":
        from docx import Document
        doc = Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    return text

# -----------------------
# --- Structured Profile ---
# -----------------------
def build_structured_profile(resume_text):
    profile = {
        "contact": "",
        "education": [],
        "experience": [],
        "skills": [],
        "companies": [],
        "titles": [],
        "dates": []
    }
    lines = resume_text.splitlines()
    for line in lines:
        line_lower = line.lower()
        if "@" in line or any(c.isdigit() for c in line):
            profile["contact"] += line + "\n"
        if any(keyword in line_lower for keyword in ["university", "college", "degree", "certification"]):
            profile["education"].append(line.strip())
        if any(keyword in line_lower for keyword in ["developer", "engineer", "manager", "analyst", "consultant"]):
            profile["experience"].append(line.strip())
            parts = re.split(r" at |, ", line, flags=re.IGNORECASE)
            if len(parts) > 1:
                profile["titles"].append(parts[0].strip())
                profile["companies"].append(parts[1].strip())
            date_match = re.search(r"\b(20\d{2}|19\d{2})\b", line)
            if date_match:
                profile["dates"].append(date_match.group())
        if any(keyword in line_lower for keyword in ["python", "java", "node", "sql", "angular", "react", "typescript"]):
            profile["skills"].append(line.strip())
    return profile

# -----------------------
# --- Keyword Explanation ---
# -----------------------
def generate_keyword_explanations(missing_keywords, job_desc):
    explanations = {}
    if not missing_keywords:
        return explanations

    prompt = f"""
You are an ATS assistant. 

Given the job description below, for each keyword, provide:
1. A short explanation (1-2 sentences) why it is important.
2. An importance level: high, medium, or low.

Return in strict JSON format.

Job Description:
{job_desc}

Keywords:
{', '.join(missing_keywords)}
"""
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
        )
        raw_content = response.choices[0].message.content.strip()
        if raw_content.startswith("```"):
            raw_content = "\n".join(raw_content.splitlines()[1:-1]).strip()
        explanations = json.loads(raw_content)
    except Exception:
        explanations = {kw: {"explanation": "Important for job requirements.", "importance": "medium"} 
                        for kw in missing_keywords}
    return explanations

# -----------------------
# --- Main Route ---
# -----------------------
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    structured_profile = {}

    if request.method == "POST":
        job_desc = request.form.get("job", "").strip()
        resume_file = request.files.get("resume_file")
        resume_text = ""

        if resume_file and resume_file.filename != "":
            file_ext = os.path.splitext(resume_file.filename)[1].lower()
            if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                result = {"error": "Unsupported file type!"}
            else:
                os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
                unique_filename = f"{uuid.uuid4().hex}_{resume_file.filename}"
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
                resume_file.save(file_path)
                resume_text = extract_text(file_path, file_ext)
                os.remove(file_path)

        if not resume_text:
            resume_text = request.form.get("resume", "").strip()

        if resume_text and job_desc:
            resume_text = resume_text[:4000]
            structured_profile = build_structured_profile(resume_text)

            prompt = f"""
You are a sophisticated ATS resume analyzer.

Analyze resume vs job description:
- Return missing keywords, skills to add, bullet point improvements
- Score 0-100 considering keyword placement, relevance, career progression
- Highlight formatting/ATS parsing issues
- Return strict JSON with:
  missing_keywords (list)
  skills_to_add (list)
  bullet_point_improvements (list)
  match_score (int)
  explanation (str)

Include structured profile insights:

Resume Sections:
{json.dumps(structured_profile, indent=2)}

Job Description:
{job_desc}
"""
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": prompt}],
                )
                raw_content = response.choices[0].message.content.strip()
                if raw_content.startswith("```"):
                    raw_content = "\n".join(raw_content.splitlines()[1:-1]).strip()
                try:
                    result = json.loads(raw_content)
                except json.JSONDecodeError:
                    match = re.search(r"\{.*\}", raw_content, re.DOTALL)
                    if match:
                        result = json.loads(match.group())
                    else:
                        result = {"error": "AI output could not be parsed. Raw output: " + raw_content}

                if "missing_keywords" in result:
                    keyword_explanations = generate_keyword_explanations(result["missing_keywords"], job_desc)
                    result["keyword_explanations"] = keyword_explanations

            except Exception as e:
                result = {"error": str(e)}
        else:
            result = {"error": "Please provide both a resume and a job description."}

    return render_template(
        "index.html",
        result=result,
        structured_profile=structured_profile
    )

if __name__ == "__main__":
    app.run(debug=True)
