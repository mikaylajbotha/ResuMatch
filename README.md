# ResuMatch – ATS Resume Optimizer

**ResuMatch** is a **free, open-source tool** that instantly compares your resume to any job description and tells you **exactly what’s missing**.

---

## Features

- Upload **PDF/DOCX** files or paste resume text  
- Paste any job description  
- AI-powered **match score (0–100)**  
- Highlights missing keywords with importance levels & explanations  
- Suggests skills to add and improved bullet-point suggestions  
- **100% local processing** – your resume file never leaves your machine *(only extracted text is sent to OpenAI)*  
- No accounts, no tracking, completely free  

---

## How to Run Locally

# 1. Clone or download the project
git clone https://github.com/yourusername/ResuMatch.git
cd ResuMatch
# Or just download and extract the ZIP

# 2. Create and activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# 3. Install dependencies
pip install Flask openai python-dotenv PyMuPDF pytesseract Pillow python-docx python-magic

# 4. (Optional, for scanned PDFs) Install Tesseract OCR
# Windows → https://github.com/UB-Mannheim/tesseract/wiki
# macOS → brew install tesseract
# Ubuntu/Debian → sudo apt install tesseract-ocr

# 5. Create a .env file with your OpenAI key
echo OPENAI_API_KEY=sk-your-real-key-here > .env
# Get your key → https://platform.openai.com/api-keys

# 6. Run the app
python app.py
The app will run at: http://127.0.0.1:5000

Tech Stack
Component	Technology
Backend	Python + Flask
AI	OpenAI API (GPT-4o or GPT-3.5-turbo)
Resume Parsing	PyMuPDF, python-docx, pytesseract + Pillow
Frontend	Vanilla HTML / CSS / JavaScript (no frameworks)
