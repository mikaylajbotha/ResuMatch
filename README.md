# ResuMatch – ATS Resume Optimizer

**Beat ATS systems in seconds.**  
Upload your resume (PDF/DOCX or paste text) → paste any job description → instantly get an AI-powered match score and exact fixes.

### Features
- AI-powered match score (0–100)
- Missing keywords highlighted with **high/medium/low** importance
- Hover tooltips explaining why each keyword matters
- Skills to add & smarter bullet-point suggestions
- Works 100% locally — your resume is deleted instantly after analysis

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

**Open your browser →** **http://127.0.0.1:5000**

### Requirements

- Python 3.9+
- Tesseract OCR *(only for scanned/image-based PDFs)*  
  → Windows: https://github.com/UB-Mannheim/tesseract/wiki  
  → macOS: `brew install tesseract`  
  → Ubuntu: `sudo apt install tesseract-ocr`

### Privacy & Security

- Resume file is deleted immediately after processing
- Nothing is ever stored on disk
- Only plain text is sent to OpenAI (no files, no logs)

### Project Structure
ResuMatch/
├── app.py
├── index.html
├── style.css
├── requirements.txt
├── .gitignore
└── README.md

Made with love for job seekers worldwide  
If this helps you land your dream job — **please give it a star!**
