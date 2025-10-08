import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class FastGeminiGenerator:
    def __init__(self, api_key=None):
        """
        Simple, fast Gemini text generator
        """
        # Configure API key
        if api_key:
            genai.configure(api_key=api_key)
        elif os.getenv("GOOGLE_API_KEY"):
            genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
        else:
            raise ValueError("Google Gemini API key required!")
        
        # Initialize model with fast settings
        self.model = genai.GenerativeModel(
            'gemini-1.5-flash',
            generation_config=genai.types.GenerationConfig(
                max_output_tokens=200,
                temperature=0.7,
                top_p=0.8,
                top_k=40
            )
        )
    
    def generate_sentiment_aligned_text(self, prompt, sentiment, word_count=150):
        """
        Generate text quickly using direct Gemini API
        """
        try:
            # Simple, direct prompts for each sentiment
            if sentiment == 'positive':
                system_prompt = f"Write a positive, uplifting {word_count}-word response about: {prompt}"
            elif sentiment == 'negative':
                system_prompt = f"Write a balanced, constructive {word_count}-word response addressing concerns about: {prompt}"
            else:
                system_prompt = f"Write a neutral, informative {word_count}-word response about: {prompt}"
            
            # Generate with timeout
            response = self.model.generate_content(
                system_prompt,
                request_options={'timeout': 10}  # 10 second timeout
            )
            
            return response.text.strip()
            
        except Exception as e:
            print(f"Gemini error: {e}")
            return self._quick_fallback(prompt, sentiment)
    
    def _quick_fallback(self, prompt, sentiment):
        """Quick fallback text"""
        starters = {
            'positive': "This presents exciting opportunities",
            'negative': "There are important considerations",
            'neutral': "This topic involves several aspects"
        }
        
        starter = starters.get(sentiment, "This is an interesting topic")
        return f"{starter} regarding {prompt}. The subject deserves careful analysis and thoughtful consideration of various perspectives and potential outcomes."