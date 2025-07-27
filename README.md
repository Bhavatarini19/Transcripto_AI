# 📝 Transcripto AI

**🔗 [Click to open transcripto-ai app](https://transcripto-ai.streamlit.app/)**

**Transcripto AI** is a simple and effective Streamlit app that lets you **summarize and translate YouTube videos** using their transcripts. It uses OpenAI’s GPT-4o model to provide clear summaries in a variety of languages. Ideal for students, researchers, professionals, or anyone looking to save time understanding video content.

---

## 📽️ Demo

![MailMate AI Demo](assets/transcriptoAIDemo.gif)

---

## ✨ What It Does

- Accepts any YouTube video URL
- Fetches transcript (manual or auto-generated)
- Summarizes video content using OpenAI GPT-4o
- Translates summary into your selected language
- Clean and readable markdown output

---

## 🧰 Tech Stack

- **UI & Frontend:** Streamlit
- **Backend:** Python
- **Language Model:** OpenAI GPT-4o
- **Transcripts:** YouTube Transcript API

---

## 🛠️ Local Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Bhavatarini19/Transcripto_AI.git
cd Transcripto_AI
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv1
source venv1/bin/activate  # On Windows: venv1\Scripts\activate
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Add Your OpenAI API Key

#### Option A: Using a `.env` File (Local)

Create a `.env` file in the project root directory and add:

```env
OPENAI_API_KEY=sk-your-api-key-here
```

#### Option B: Streamlit Cloud Deployment

In your [Streamlit Cloud app](https://streamlit.io/cloud), go to **Settings > Secrets** and paste:

```toml
OPENAI_API_KEY = "sk-your-api-key-here"
```

---

## ▶️ Run the App Locally

```bash
streamlit run app.py
```

Then open `http://localhost:8501` in your browser.

---

## 🌍 Deployment on Streamlit Cloud

1. Push your app to a GitHub repository.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud).
3. Create a new app pointing to your repo.
4. Add the `OPENAI_API_KEY` in the **Secrets Manager**.
5. Deploy and share your app URL.

---

## 💡 Use Cases

- Summarize long educational videos
- Translate key insights for multilingual users
- Quickly understand lecture, tech talks, or webinars

---
