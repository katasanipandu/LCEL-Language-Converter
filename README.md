🌍 LCEL Language Translator (Groq + Streamlit)
📌 Overview
This project is a real-time language translation app built using:

LangChain Expression Language (LCEL) – for creating a structured AI processing pipeline.

Groq's Gemma2-9b-It model – for fast and accurate text translations.

Streamlit – for an interactive web interface.

The app allows users to input text in any language and get an instant translation in their target language, preserving punctuation, tone, and meaning.

🚀 Features
Multi-language Support – Translate text into any target language.

LCEL Pipeline – Modular AI workflow: Prompt → Model → Output Parser.

Groq API Integration – Uses Gemma2-9b-It, optimized for high speed and low latency.

Streamlit Web App – Clean and interactive UI.

Secure API Key Handling – Uses .env file to store sensitive keys.

🛠️ Tech Stack
Python – Core programming language.

LangChain – LCEL pipeline and model integration.

Groq API – LLM backend for translation.

Streamlit – UI framework for deployment.

dotenv – For environment variable management.

⚙️ How It Works
User Input: Enter the text and select the target language.

LCEL Processing:

Prompt Template – Defines the translation task.

Groq Model – Processes the input using Gemma2-9b-It.

Output Parser – Extracts and formats the translation.

Output: Display the translated text instantly in the UI.

📦 Installation

# Clone the repository
git clone https://github.com/yourusername/LCEL-Language-Translator.git
cd LCEL-Language-Translator

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt
🔑 Environment Variables
Create a .env file in the project root:


GROQ_API_KEY=your_groq_api_key_here
⚠ Never share your .env file or commit it to GitHub.

▶️ Usage
Run the app locally:


streamlit run langconv.py
Open your browser and navigate to http://localhost:8501.

📌 Example
Input:
Hello, how are you? I hope you are doing well.
Target Language:
Telugu

Output:
హలో, మీరు ఎలా ఉన్నారు? మీరు బాగున్నారని ఆశిస్తున్నాను.
<img width="1483" height="774" alt="image" src="https://github.com/user-attachments/assets/58a9a484-f304-4fe1-9ba5-f69ec5950926" />
