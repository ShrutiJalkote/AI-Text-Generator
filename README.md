# AI Sentiment Summary Generator

🤖 Generate text content aligned with the sentiment of your input using Google Gemini Flash API.

## ✨ Features

- **⚡ Fast Sentiment Analysis**: Instant keyword-based sentiment detection
- **🚀 Google Gemini Flash**: Lightning-fast text generation
- **🎯 Sentiment-Aligned Content**: Generates positive, negative, or neutral content
- **📱 Interactive UI**: Clean Streamlit web interface
- **🔧 Customizable**: Adjustable text length and manual sentiment override

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/sentiment-summary-generator.git
cd sentiment-summary-generator
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up API Key
- Get your free API key: [Google AI Studio](https://makersuite.google.com/app/apikey)
- Copy `.env.example` to `.env`
- Add your API key: `GOOGLE_API_KEY=your_key_here`

### 4. Run the Application
```bash
streamlit run app.py
```

## 📁 Project Structure

```
├── app.py                    # Main Streamlit application
├── sentiment_fast.py         # Fast keyword-based sentiment analysis
├── text_generator_fast.py    # Direct Gemini API text generation
├── requirements.txt          # Minimal dependencies
├── .env.example             # Environment variables template
├── .gitignore               # Git ignore file
└── README.md                # This file
```

## 🎯 How It Works

1. **Input**: Enter your text prompt
2. **Sentiment Analysis**: Instant keyword-based sentiment detection
3. **Content Generation**: Gemini Flash generates aligned content
4. **Output**: View sentiment analysis + generated text

## 🔧 Configuration Options

- **Output Length**: Short (50-100), Medium (100-200), Long (200-300) words
- **Sentiment Override**: Manual positive/negative/neutral selection
- **API Key**: Environment variable or sidebar input

## 💡 Why This Approach?

- **Speed**: No heavy model loading, instant sentiment analysis
- **Cost-Effective**: Uses Gemini Flash (cheaper than GPT)
- **Reliable**: Simple keyword-based sentiment with high accuracy
- **Lightweight**: Only 3 dependencies needed

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI**: Google Gemini Flash API
- **Sentiment**: Custom keyword-based analyzer
- **Language**: Python 3.8+

## 📝 Example Usage

**Input**: "I love this new technology!"
- **Sentiment**: 🟢 Positive (85%)
- **Generated**: Positive, uplifting content about the technology

**Input**: "This product has many issues"
- **Sentiment**: 🔴 Negative (78%)
- **Generated**: Balanced, constructive content addressing concerns

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google for the Gemini Flash API
- Streamlit for the amazing web framework
- The open-source community

---

**⭐ Star this repo if you found it helpful!**

## ☁️ Deploy to Streamlit Cloud

1. Push this project to a public Git repository (GitHub/GitLab/Bitbucket).
2. Go to Streamlit Community Cloud and create a new app: `New app` → select your repo.
3. Set the app entry point to `AI-Text-Generator/app.py` (or adjust to your path).
4. Ensure `AI-Text-Generator/requirements.txt` exists (already included here).
5. Click `Deploy`.

### Secrets (API Keys)

- In Streamlit Cloud, open your app → `Settings` → `Secrets`.
- Add:
  ```
  GOOGLE_API_KEY = your_google_generative_ai_key
  ```
- The app loads environment variables via `python-dotenv` and Streamlit Secrets; sidebar input can also override the key.

### Optional: Theming and Server Config

- You can tweak theme/server behavior in `.streamlit/config.toml`.