"""
Sentinel AI - Text Analyzer
Real AI-powered scam and AI-generated text detection using Google Gemini API.
"""
import os
from typing import Dict
import google.generativeai as genai


class TextAnalyzer:
    """
    Text analysis using Google Gemini API for detecting AI-generated text,
    scams, phishing, and social engineering attempts.
    """
    
    def __init__(self):
        """Initialize the text analyzer with Gemini API."""
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        self.loaded = True
    
    def analyze(self, text: str) -> Dict:
        """
        Analyze text for AI generation, scams, and manipulation.
        
        Args:
            text: Text content to analyze
            
        Returns:
            Dict with analysis results including probabilities
        """
        try:
            # Craft a detailed prompt for text analysis
            prompt = f"""Analyze this text message/content and determine if it's:
1. AI-generated text
2. A scam, phishing attempt, or social engineering
3. Legitimate human-written content

Text to analyze:
"{text}"

Look for these indicators:
- Urgency tactics or pressure to act quickly
- Requests for money, personal info, or credentials
- Too-good-to-be-true offers
- Suspicious links or contact methods
- Generic greetings or impersonal language
- Grammar/spelling that seems off
- AI-like patterns (overly formal, repetitive, generic)
- Emotional manipulation
- Authority impersonation

Provide your analysis in this exact format:
VERDICT: [Scam/AI-Generated/Suspicious/Legitimate]
RISK_SCORE: [0-100]
REASONING: [Brief explanation of key indicators]

Be specific about what makes this text suspicious or safe."""

            # Get analysis from Gemini
            response = self.model.generate_content(prompt)
            analysis_text = response.text
            
            # Parse the response
            verdict = "Legitimate"
            risk_score = 20
            reasoning = analysis_text
            
            # Extract verdict
            if "VERDICT:" in analysis_text:
                verdict_line = [line for line in analysis_text.split('\n') if 'VERDICT:' in line][0]
                verdict = verdict_line.split('VERDICT:')[1].strip().split()[0]
            
            # Extract risk score
            if "RISK_SCORE:" in analysis_text:
                risk_line = [line for line in analysis_text.split('\n') if 'RISK_SCORE:' in line][0]
                try:
                    risk_score = int(''.join(filter(str.isdigit, risk_line.split('RISK_SCORE:')[1])))
                except:
                    risk_score = 50
            
            # Extract reasoning
            if "REASONING:" in analysis_text:
                reasoning = analysis_text.split('REASONING:')[1].strip()
            
            # Convert to probabilities
            risk_decimal = risk_score / 100.0
            
            if "SCAM" in verdict.upper() or "PHISHING" in verdict.upper():
                return {
                    "safe_probability": 1.0 - risk_decimal,
                    "scam_probability": risk_decimal * 0.7,
                    "ai_generated": risk_decimal * 0.3,
                    "reasoning": reasoning,
                    "risk_score": risk_score
                }
            elif "AI" in verdict.upper() or "GENERATED" in verdict.upper():
                return {
                    "safe_probability": 1.0 - risk_decimal,
                    "scam_probability": risk_decimal * 0.2,
                    "ai_generated": risk_decimal * 0.8,
                    "reasoning": reasoning,
                    "risk_score": risk_score
                }
            elif "SUSPICIOUS" in verdict.upper():
                return {
                    "safe_probability": 1.0 - risk_decimal,
                    "scam_probability": risk_decimal * 0.5,
                    "ai_generated": risk_decimal * 0.5,
                    "reasoning": reasoning,
                    "risk_score": risk_score
                }
            else:  # Legitimate
                return {
                    "safe_probability": 1.0 - risk_decimal,
                    "scam_probability": risk_decimal * 0.5,
                    "ai_generated": risk_decimal * 0.5,
                    "reasoning": reasoning,
                    "risk_score": risk_score
                }
                
        except Exception as e:
            print(f"Text analysis failed: {e}")
            # Return uncertain results on error
            return {
                "safe_probability": 0.5,
                "scam_probability": 0.25,
                "ai_generated": 0.25,
                "reasoning": f"Analysis failed: {str(e)}",
                "risk_score": 50
            }


# Singleton instance
_analyzer = None


def get_text_analyzer() -> TextAnalyzer:
    """Get or create the text analyzer instance."""
    global _analyzer
    if _analyzer is None:
        _analyzer = TextAnalyzer()
    return _analyzer
