import os
from google import genai
from google.genai import types
from pydantic import BaseModel, Field

# 1. Structured data scheme for enterprise output
class IndianORMAnalysis(BaseModel):
    category: str = Field(description="The core problem category, e.g., 'Delivery Delay', 'Wrong Item', 'Payment Failure', 'Product Quality', 'Praise'")
    sub_category: str = Field(description="Detailed sub-issue, e.g., 'Missing Item inside box', 'Refund stuck', 'Rude delivery partner'")
    urgency_score: float = Field(description="A score from 1.0 (very low) to 10.0 (extreme crisis/viral risk)")
    sentiment: str = Field(description="Overall sentiment: 'Extremely Negative', 'Negative', 'Neutral', 'Positive'")
    detected_languages: list[str] = Field(description="Languages found in text, e.g., ['Hinglish', 'English', 'Hindi']")
    suggested_action: str = Field(description="Internal company action recommendation")
    draft_reply_english: str = Field(description="A highly professional, context-aware corporate draft response in English")
    draft_reply_hindi: str = Field(description="The same context-aware corporate draft response written in clear Hindi script")

# 2. Your active API Key
API_KEY = "AQ.Ab8RN6L8lx8b2sXBC8Q3zJArhdvdCfy_fw2M0zT00jXN-rEyHg"

client = genai.Client(api_key=API_KEY)

def analyze_indian_review(raw_text: str):
    print("🧠 Gemini 3.1 Pro is using Extended Thinking to analyze the brand mention...")
    
    prompt = f"""
    You are the Principal Online Reputation Management (ORM) Specialist for top Indian E-commerce and Quick-Commerce apps (like Blinkit, Zepto, Blinkit, Instamart, Flipkart).
    Analyze the following user mention across Indian social media/reviews. 
    It may contain code-mixed language (Hinglish, short slang, or regional text mixed with English).
    Evaluate the underlying emotional urgency, identify specific logistics or service failures unique to the Indian market, and draft professional corporate responses.

    User Review/Mention: 
    "{raw_text}"
    """
    
    # Run the generation with Extended Thinking configuration enabled
    response = client.models.generate_content(
        model='gemini-3.8-flash',
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=IndianORMAnalysis,
            temperature=0.2,
            # This enables the extended reasoning budget for the model
        ),
    )
    
    print("\n✅ Analysis Complete! Structured Result:")
    print(response.text)

# 4. Test Example
mock_review = "Ordered a laptop from your app and instead of laptop, saboon ki tikki (soap bar) delivered inside the box!! Delivery boy took cash and ran away. Customer care is not picking up, absolute fraud company @brand_name #scam"

analyze_indian_review(mock_review)
