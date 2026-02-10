#!/usr/bin/env python3
"""
Sentiment Analysis Tool
Analyzes text sentiment using pre-trained transformer models.

Author: Timothy Logan
License: MIT
"""

from transformers import pipeline
import sys
from typing import Dict, List

class SentimentAnalyzer:
    """
    Analyzes sentiment of text using Hugging Face transformers.
    
    Uses a pre-trained DistilBERT model fine-tuned on sentiment analysis.
    Classifies text as POSITIVE or NEGATIVE with confidence scores.
    """
    
    def __init__(self):
        """Initialize the sentiment analysis pipeline."""
        print("Loading sentiment analysis model...")
        print("(This may take a moment on first run)")
        try:
            self.analyzer = pipeline(
                "sentiment-analysis",
                model="distilbert-base-uncased-finetuned-sst-2-english"
            )
            print("✓ Model loaded successfully!\n")
        except Exception as e:
            print(f"Error loading model: {e}")
            print("Please ensure you have internet connection and try again.")
            sys.exit(1)
    
    def analyze(self, text: str) -> Dict[str, any]:
        """
        Analyze sentiment of given text.
        
        Args:
            text: Input text to analyze
            
        Returns:
            Dictionary containing:
                - label: POSITIVE or NEGATIVE
                - score: Confidence score (0-1)
        
        Example:
            >>> analyzer = SentimentAnalyzer()
            >>> result = analyzer.analyze("I love this!")
            >>> print(result)
            {'label': 'POSITIVE', 'score': 0.9998}
        """
        if not text or not text.strip():
            return {'label': 'NEUTRAL', 'score': 0.0}
        
        try:
            result = self.analyzer(text)[0]
            return result
        except Exception as e:
            print(f"Error analyzing text: {e}")
            return {'label': 'ERROR', 'score': 0.0}
    
    def analyze_batch(self, texts: List[str]) -> List[Dict]:
        """
        Analyze sentiment of multiple texts.
        
        Args:
            texts: List of text strings to analyze
            
        Returns:
            List of dictionaries with sentiment results
        """
        results = []
        for text in texts:
            result = self.analyze(text)
            results.append({
                'text': text,
                'sentiment': result['label'],
                'confidence': result['score']
            })
        return results

def print_result(text: str, result: Dict):
    """Pretty print sentiment analysis result."""
    sentiment = result['label']
    confidence = result['score'] * 100
    
    # Color coding (if terminal supports it)
    if sentiment == 'POSITIVE':
        emoji = '😊'
        color = '\033[92m'  # Green
    else:
        emoji = '😟'
        color = '\033[91m'  # Red
    reset = '\033[0m'
    
    print(f"\nText: {text}")
    print(f"{color}Sentiment: {sentiment} {emoji}{reset}")
    print(f"Confidence: {confidence:.1f}%")
    print("-" * 50)

def main():
    """Main CLI interface."""
    print("=" * 50)
    print("     SENTIMENT ANALYZER")
    print("     Powered by Transformers")
    print("=" * 50)
    print()
    
    # Initialize analyzer
    analyzer = SentimentAnalyzer()
    
    print("Enter text to analyze (or 'quit' to exit)")
    print("Examples:")
    print("  - 'This is amazing!'")
    print("  - 'I'm really disappointed'")
    print()
    
    while True:
        try:
            text = input("📝 Text: ").strip()
            
            if text.lower() in ['quit', 'exit', 'q']:
                print("\n👋 Thanks for using Sentiment Analyzer!")
                break
            
            if not text:
                continue
            
            result = analyzer.analyze(text)
            print_result(text, result)
            
        except KeyboardInterrupt:
            print("\n\n👋 Thanks for using Sentiment Analyzer!")
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
