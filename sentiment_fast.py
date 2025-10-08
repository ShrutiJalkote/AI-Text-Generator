import re

class FastSentimentAnalyzer:
    def __init__(self):
        """Fast keyword-based sentiment analyzer"""
        self.positive_words = {
            'love', 'like', 'great', 'good', 'excellent', 'amazing', 'wonderful', 
            'fantastic', 'awesome', 'brilliant', 'perfect', 'happy', 'joy', 'excited',
            'thrilled', 'delighted', 'pleased', 'satisfied', 'impressed', 'outstanding'
        }
        
        self.negative_words = {
            'hate', 'dislike', 'bad', 'terrible', 'awful', 'horrible', 'disgusting',
            'disappointing', 'frustrated', 'angry', 'sad', 'upset', 'annoyed', 'worried',
            'concerned', 'problem', 'issue', 'wrong', 'failed', 'broken'
        }
    
    def analyze(self, text):
        """
        Fast sentiment analysis using keywords
        """
        text_lower = text.lower()
        words = re.findall(r'\b\w+\b', text_lower)
        
        positive_count = sum(1 for word in words if word in self.positive_words)
        negative_count = sum(1 for word in words if word in self.negative_words)
        
        if positive_count > negative_count:
            confidence = min(0.6 + (positive_count * 0.1), 0.95)
            return {'label': 'positive', 'confidence': confidence}
        elif negative_count > positive_count:
            confidence = min(0.6 + (negative_count * 0.1), 0.95)
            return {'label': 'negative', 'confidence': confidence}
        else:
            return {'label': 'neutral', 'confidence': 0.65}