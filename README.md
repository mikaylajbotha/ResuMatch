# ResuMatch – ATS Resume Optimizer

ResuMatch is a free, open-source tool that compares your resume to any job description and shows what’s missing.

## Tech Stack

**Backend:**            Python, Flask  
**AI:**                 OpenAI API (GPT-4o or GPT-3.5-turbo)  
**Resume Parsing:**     PyMuPDF, python-docx, pytesseract + Pillow  
**Frontend:**           HTML, CSS, JavaScript

## Features

- Upload PDF/DOCX or paste resume text
- Paste any job description
- AI-powered match score (0–100)
- Highlights missing keywords and suggests improvements
- 100% local processing – files never leave your machine
- No accounts, no tracking, completely free

- ## Run Locally

Clone the project

```bash
  git clone https://github.com/yourusername/ResuMatch.git
```

Go to the project directory

```bash
  cd ResuMatch
```

Create and activate a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate
```

Install dependencies

```bash
pip install Flask openai python-dotenv PyMuPDF pytesseract Pillow python-docx python-magic
```

(Optional) Install Tesseract OCR for scanned PDFs

```bash
# Windows → https://github.com/UB-Mannheim/tesseract/wiki
# macOS
brew install tesseract
# Ubuntu/Debian
sudo apt install tesseract-ocr
```

Create a .env file with your OpenAI API key

```bash
echo OPENAI_API_KEY=sk-your-real-key-here > .env
```

Start the server

```bash
python app.py

Open your browser at http://127.0.0.1:5000
```
