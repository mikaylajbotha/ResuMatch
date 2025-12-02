Markdown# ResuMatch – ATS Resume Optimizer

**Beat ATS systems in seconds.**  
Upload your resume (PDF/DOCX or paste text) → paste any job description → instantly see your match score and exactly what’s missing.

- AI-powered scoring (0–100)  
- Missing keywords highlighted with importance level  
- Smart tooltips explaining why each keyword matters  
- Skills to add & bullet-point improvement suggestions  
- Works completely locally — your resume is deleted instantly

### Quick Start (Copy & Paste)

```bash
git clone https://github.com/mikaylajbotha/ResuMatch.git
cd ResuMatch

# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS / Linux

# Install dependencies
pip install -r requirements.txt

# Add your OpenAI API key
echo OPENAI_API_KEY=sk-your-key-here > .env

# Run the app
python app.py
Open your browser → http://127.0.0.1:5000
Requirements

Python 3.9+
Tesseract OCR (only needed for scanned/image-based PDFs)
→ Windows: https://github.com/UB-Mannheim/tesseract/wiki
→ macOS: brew install tesseract
→ Ubuntu/Debian: sudo apt install tesseract-ocr

Privacy & Security

Your resume file is deleted immediately after processing
No data is ever stored on disk
Only plain text is sent to OpenAI for analysis

Project Structure
textResuMatch/
├── app.py
├── index.html
├── style.css
├── requirements.txt
├── .gitignore
└── README.md
Made with love for job seekers worldwide
If this helps you land your dream job — please give it a star!
