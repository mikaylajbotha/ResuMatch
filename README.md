# ResuMatch – ATS Resume Optimizer

A **free, open-source** tool that instantly compares your resume to any job description and tells you **exactly what’s missing**.

![Demo](https://via.placeholder.com/800x400?text=ResuMatch+Demo)  
*(Replace with actual screenshot when available)*

🚀 **Live Demo** (when deployed): https://resumatch.yourname.com *(optional)*

## Features

- Upload **PDF/DOCX** or paste resume text  
- Paste any job description  
- AI-powered **match score (0–100)**  
- Highlights **missing keywords** with importance level & explanations  
- Suggests **skills to add** + improved bullet-point suggestions  
- **100% local processing** – your resume file never leaves your machine *(only extracted text is sent to OpenAI)*  
- No accounts, no tracking, completely free

## Screenshots

*(Add screenshots here later)*

## How to Run Locally (Copy-Paste Instructions)

```bash
# 1. Clone or download the project
git clone https://github.com/yourusername/ResuMatch.git
cd ResuMatch
# (or just download and extract the ZIP)

# 2. Create and activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
# source venv/bin/activate

# 3. Install dependencies
pip install Flask openai python-dotenv PyMuPDF pytesseract Pillow python-docx python-magic

# 4. (Important for scanned PDFs) Install Tesseract OCR
# Windows → Download & add to PATH: https://github.com/UB-Mannheim/tesseract/wiki
# macOS → brew install tesseract
# Ubuntu/Debian → sudo apt install tesseract-ocr

# 5. Create .env file with your OpenAI key
echo OPENAI_API_KEY=sk-your-real-key-here > .env
# Get your key from → https://platform.openai.com/api-keys

# 6. Run the app
python app.py
The app will be available at: http://127.0.0.1:5000
Tech Stack

Python + Flask (backend)
OpenAI API (GPT-4o or GPT-3.5-turbo)
PyMuPDF, python-docx, pytesseract + Pillow (resume parsing)
Vanilla HTML/CSS/JS (frontend – no heavy frameworks)

Contributing
Contributions are welcome! Feel free to submit issues or pull requests.
