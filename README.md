# ResuMatch – ATS Resume Optimizer

**ResuMatch** is a free, open-source tool that compares your resume to any job description and shows what’s missing.

---

## Features

- Upload PDF/DOCX or paste resume text  
- Paste any job description  
- AI-powered match score (0–100)  
- Highlights missing keywords and suggests improvements  
- 100% local processing – files never leave your machine  
- No accounts, no tracking, completely free  

---

## How to Run Locally

```bash
git clone https://github.com/yourusername/ResuMatch.git
cd ResuMatch

python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

pip install Flask openai python-dotenv PyMuPDF pytesseract Pillow python-docx python-magic

# Optional: Install Tesseract OCR for scanned PDFs
# Windows → https://github.com/UB-Mannheim/tesseract/wiki
# macOS → brew install tesseract
# Ubuntu/Debian → sudo apt install tesseract-ocr

echo OPENAI_API_KEY=sk-your-real-key-here > .env

python app.py
