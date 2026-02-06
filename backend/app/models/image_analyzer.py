"""
Sentinel AI - Image Analyzer
Real AI-powered deepfake and AI-generated image detection using Google Gemini Vision API.
"""
import os
from pathlib import Path
from typing import Dict
import google.generativeai as genai


class ImageAnalyzer:
    """
    Image analysis using Google Gemini Vision API for detecting AI-generated 
    and manipulated images.
    """
    
    def __init__(self):
        """Initialize the image analyzer with Gemini API."""
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')
        self.loaded = True
    
    def analyze(self, file_path: Path) -> Dict:
        """
        Analyze image for AI generation or manipulation using Gemini Vision.
        
        Args:
            file_path: Path to image file
            
        Returns:
            Dict with analysis results including probabilities
        """
        try:
            from PIL import Image
            
            # Load image
            img = Image.open(file_path)
            
            # Craft a detailed prompt for AI detection
            prompt = """Analyze this image carefully and determine if it's AI-generated, manipulated, or real.

Look for these signs of AI generation:
- Unnatural textures or patterns
- Inconsistent lighting or shadows
- Distorted faces, hands, or body parts
- Unrealistic backgrounds or objects
- Artifacts or glitches typical of AI generation
- Inconsistent perspective or proportions
- Unusual text or writing
- Blending or morphing effects

Provide your analysis in this exact format:
VERDICT: [AI-Generated/Manipulated/Real]
CONFIDENCE: [0-100]
REASONING: [Brief explanation of key indicators you found]

Be thorough and specific about what you observe."""

            # Get analysis from Gemini
            response = self.model.generate_content([prompt, img])
            analysis_text = response.text
            
            # Parse the response
            verdict = "Real"
            confidence = 50
            reasoning = analysis_text
            
            # Extract verdict
            if "VERDICT:" in analysis_text:
                verdict_line = [line for line in analysis_text.split('\n') if 'VERDICT:' in line][0]
                verdict = verdict_line.split('VERDICT:')[1].strip().split()[0]
            
            # Extract confidence
            if "CONFIDENCE:" in analysis_text:
                conf_line = [line for line in analysis_text.split('\n') if 'CONFIDENCE:' in line][0]
                try:
                    confidence = int(''.join(filter(str.isdigit, conf_line.split('CONFIDENCE:')[1])))
                except:
                    confidence = 50
            
            # Extract reasoning
            if "REASONING:" in analysis_text:
                reasoning = analysis_text.split('REASONING:')[1].strip()
            
            # Convert to probabilities
            confidence_decimal = confidence / 100.0
            
            if "AI" in verdict.upper() or "GENERATED" in verdict.upper():
                return {
                    "real_probability": 1.0 - confidence_decimal,
                    "ai_generated": confidence_decimal * 0.8,
                    "manipulated": confidence_decimal * 0.2,
                    "reasoning": reasoning
                }
            elif "MANIPULATED" in verdict.upper() or "EDITED" in verdict.upper():
                return {
                    "real_probability": 1.0 - confidence_decimal,
                    "ai_generated": confidence_decimal * 0.3,
                    "manipulated": confidence_decimal * 0.7,
                    "reasoning": reasoning
                }
            else:  # Real
                return {
                    "real_probability": confidence_decimal,
                    "ai_generated": (1.0 - confidence_decimal) * 0.5,
                    "manipulated": (1.0 - confidence_decimal) * 0.5,
                    "reasoning": reasoning
                }
                
        except Exception as e:
            print(f"Image analysis failed: {e}")
            # Return uncertain results on error
            return {
                "real_probability": 0.5,
                "ai_generated": 0.25,
                "manipulated": 0.25,
                "reasoning": f"Analysis failed: {str(e)}"
            }


# Singleton instance
_analyzer = None


def get_image_analyzer() -> ImageAnalyzer:
    """Get or create the image analyzer instance."""
    global _analyzer
    if _analyzer is None:
        _analyzer = ImageAnalyzer()
    return _analyzer
