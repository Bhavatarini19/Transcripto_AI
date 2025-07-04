import streamlit as st
import re
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import NoTranscriptFound, TranscriptsDisabled, VideoUnavailable
from openai import OpenAI

st.title("📹📝 Transcripto AI")
st.markdown("Summarize and translate YouTube videos into your choosen language.")
st.sidebar.markdown("### ℹ️ About Transcripto AI")
st.sidebar.markdown(
    """
    Transcripto AI uses **YouTube transcripts** and **OpenAI GPT-4o** to:
    
    - 📝 Summarize video content
    - 🌍 Translate into your preferred language
    
    Ideal for **students**, **professionals**, and **researchers**.
    """
)
url = st.text_input("Enter YouTube Video URL")
api_key = st.text_input("Enter Your OpenAI API key")
supported_languages = [
    "English", "Tamil", "Hindi", "French", "German", "Spanish", "Japanese", "Korean",
    "Chinese", "Arabic", "Portuguese", "Italian", "Russian", "Turkish", "Indonesian",
    "Vietnamese", "Thai", "Dutch", "Bengali", "Swahili", "Filipino", "Hebrew",
    "Polish", "Romanian", "Ukrainian", "Greek", "Urdu", "Persian", "Malay"
]
language = "English"
language = st.selectbox("Choose output language", supported_languages)


def extract_video_id(url):
    match = re.search(r"(?:v=|youtu\.be/)([a-zA-Z0-9_-]{11})", url)
    if match:
        return match.group(1)
    return None

def get_transcript(video_id):
    try:
        transcripts = YouTubeTranscriptApi.list_transcripts(video_id)
        try:
            manual = transcripts.find_manually_created_transcript(["en"])
            return manual.fetch()
        except NoTranscriptFound:
            try:
                auto = transcripts.find_generated_transcript(["en"])
                return auto.fetch()
            except NoTranscriptFound:
                return None
    except (NoTranscriptFound, TranscriptsDisabled, VideoUnavailable, Exception):
        return None

def get_full_text(transcript):
    if transcript:
        full_text = " ".join([t.text for t in transcript.snippets])
        return full_text
    return None

def contact_openai(transcript):
    try:
        system_prompt = "You are an assistant that analyzes the contents of a transcript\
        and provide a title and short summary in the mentioned langugae, ignoring text that is unwanted or navigation related.\
            respond in markdown."
        user_prompt = f"You are looking at transcript of a youtube video and it is as follows\
            Please provide a title and short summary as paragraph with points in them for this video transcript in {language.lower()} in markdown.\n\n"
        user_prompt += transcript

        message = [
        {"role" : "system", "content" : system_prompt},
        {"role" : "user", "content" : user_prompt}
        ]
        
        openai = OpenAI(api_key=api_key)
        response = openai.chat.completions.create(
            model = "gpt-4o-mini",
            messages = message
        )

        return response.choices[0].message.content
    except Exception as e:
        st.error("⚠️ OpenAI error")

if st.button("Summarize"):
    video_id = extract_video_id(url)
    if not video_id:
        st.error("⚠️ Invalid Youtube URL! Please check and try again.")
    else: 
        if not api_key:
            st.error("⚠️ Please enter the OpenAI API key to proceed.")
        elif not api_key.startswith("sk-proj-"):
            st.error("⚠️ An API key was found but it doesn't start with 'sk-proj-' \n Please enter the right OpenAI API key.")
        else:
            api_key = api_key.strip()
            with st.spinner("🔍 Fetching transcript..."):
                transcript = get_transcript(video_id)
                full_text = get_full_text(transcript)
                if not full_text:
                    st.error("⚠️ Transcript not available for this video.")
            if not transcript:
                st.error("⚠️ Transcript not available for this video.") 
            else:
                with st.spinner("✍️ Summarizing the video..."):
                    summary = contact_openai(full_text)

                st.markdown(summary)
                
     