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
