# 📹📝 Transcripto AI

**Transcripto AI** is a Streamlit-based web application that summarizes and translates YouTube videos using their transcripts. It leverages OpenAI's GPT-4o model to generate accurate, markdown-formatted summaries in your selected language.

---

## 🚀 Features

- 🔗 Paste any YouTube video URL
- 📝 Auto-fetches the transcript (manual or auto-generated)
- 🤖 Summarizes the video using GPT-4o
- 🌍 Supports 25+ output languages for translated summaries
- 🧠 Clean markdown format with title + bullet points

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **LLM API:** OpenAI GPT-4o
- **Transcripts:** YouTube Transcript API

---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/transcripto-ai.git
cd transcripto-ai
```

### 2. Create a Virtual Environment
```bash
python -m venv namevenv
source namevenv/bin/activate  # On Windows: namevenv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set the OpenAI API Key

#### Option A: Using `.env` locally
Create a `.env` file in the project root:
```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

#### Option B: On Streamlit Cloud (Recommended)
Go to your [Streamlit Cloud dashboard](https://streamlit.io/cloud) → App Settings → **Secrets** tab  
Paste:
```toml
OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

---

## ▶️ Run Locally

```bash
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

---

## 🌐 Deployment

This app is ready for deployment on [Streamlit Cloud](https://streamlit.io/cloud). Just push your code to GitHub and deploy using their UI.  
Make sure to configure `OPENAI_API_KEY` in the **Secrets Manager**.

---

## 📎 Sample Use Case

- Students summarizing long lectures
- Researchers translating domain videos
- Professionals extracting key insights from video content

