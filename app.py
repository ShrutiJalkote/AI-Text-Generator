import streamlit as st
import os
from dotenv import load_dotenv
from sentiment_fast import FastSentimentAnalyzer
from text_generator_fast import FastGeminiGenerator

# Load environment variables
load_dotenv()

@st.cache_resource
def load_fast_analyzer():
    """Cache the fast sentiment analyzer"""
    return FastSentimentAnalyzer()

def main():
    st.set_page_config(
        page_title="AI Sentiment Summary Generator",
        page_icon="🤖",
        layout="wide"
    )
    
    st.title("🤖 AI Sentiment Summary Generator")
    st.markdown("Generate text content aligned with sentiment using **Google Gemini Flash**")
    
    # Sidebar for settings
    with st.sidebar:
        st.header("⚙️ Settings")
        
        # Text length setting
        text_length = st.selectbox(
            "Output Length",
            ["Short (50-100 words)", "Medium (100-200 words)", "Long (200-300 words)"],
            index=1
        )
        
        # Manual sentiment override
        manual_sentiment = st.selectbox(
            "Override Sentiment (Optional)",
            ["Auto-detect", "Positive", "Negative", "Neutral"]
        )
        
        # API Key input
        api_key = st.text_input(
            "Google Gemini API Key (Optional)",
            type="password",
            help="Leave empty to use environment variable GOOGLE_API_KEY"
        )
        
        # Info
        st.info("⚡ **Optimized for Speed**\n\n"
                "- Fast keyword sentiment analysis\n"
                "- Direct Gemini Flash API\n"
                "- No heavy model loading\n"
                "- Quick response times")
    
    # Main interface
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("📝 Input")
        user_prompt = st.text_area(
            "Enter your prompt:",
            height=200,
            placeholder="Enter the text you want to analyze and generate content for..."
        )
        
        generate_button = st.button("🚀 Generate Content", type="primary")
    
    with col2:
        st.header("📊 Results")
        
        if generate_button and user_prompt:
            with st.spinner("Generating content..."):
                try:
                    # Initialize components
                    sentiment_analyzer = load_fast_analyzer()
                    
                    # Analyze sentiment (fast)
                    if manual_sentiment == "Auto-detect":
                        sentiment_result = sentiment_analyzer.analyze(user_prompt)
                        detected_sentiment = sentiment_result['label']
                        confidence = sentiment_result['confidence']
                    else:
                        detected_sentiment = manual_sentiment.lower()
                        confidence = 1.0
                    
                    # Display sentiment analysis
                    st.subheader("🎯 Sentiment Analysis")
                    
                    # Sentiment indicator
                    sentiment_color = {
                        'positive': '🟢',
                        'negative': '🔴', 
                        'neutral': '🟡'
                    }
                    
                    st.markdown(f"""
                    **Detected Sentiment:** {sentiment_color.get(detected_sentiment, '⚪')} {detected_sentiment.title()}
                    
                    **Confidence:** {confidence:.2%}
                    """)
                    
                    # Generate text based on sentiment
                    word_count = {
                        "Short (50-100 words)": 75,
                        "Medium (100-200 words)": 150,
                        "Long (200-300 words)": 250
                    }[text_length]
                    
                    # Initialize text generator (no caching to avoid issues)
                    text_generator = FastGeminiGenerator(api_key=api_key if api_key else None)
                    
                    generated_text = text_generator.generate_sentiment_aligned_text(
                        prompt=user_prompt,
                        sentiment=detected_sentiment,
                        word_count=word_count
                    )
                    
                    # Display generated content
                    st.subheader("✨ Generated Content")
                    st.write(generated_text)
                    
                    # Word count
                    actual_word_count = len(generated_text.split())
                    st.caption(f"Word count: {actual_word_count}")
                    
                    # Success message
                    st.success("🎉 Content generated successfully!")
                    
                except Exception as e:
                    st.error(f"Error: {str(e)}")
                    st.info("Make sure you have set your Google Gemini API key.")

if __name__ == "__main__":
    main()