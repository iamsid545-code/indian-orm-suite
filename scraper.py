import os
import json
import time  # NEW: Used to add a small pause between API calls to prevent 503 drops
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from google_play_scraper import Sort, reviews
from supabase import create_client, Client

# 1. Initialize Supabase Client with your live verified credentials
SUPABASE_URL = "https://supabase.co"
SUPABASE_KEY = "sb_publishable_xqxIn47R48w8mvyn3bF9sw_uksa4tjk"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# 2. Define the Enterprise Data Structure we want back from Gemini
class IndianORMAnalysis(BaseModel):
    category: str = Field(description="Problem category, e.g., 'Delivery Delay', 'Wrong Item', 'Payment Failure', 'Cancellation Issue', 'Praise'")
    sub_category: str = Field(description="Detailed sub-issue, e.g., 'Order cancellation blocked', 'Refund stuck', 'Missing items'")
    urgency_score: float = Field(description="A score from 1.0 to 10.0 based on frustration and viral risk")
    sentiment: str = Field(description="Overall sentiment: 'Extremely Negative', 'Negative', 'Neutral', 'Positive'")
    suggested_action: str = Field(description="Internal company action recommendation")
    draft_reply_english: str = Field(description="Professional, context-aware corporate draft response in English")
    draft_reply_hindi: str = Field(description="The same context-aware corporate draft response written in clean Hindi script")

# 3. Initialize Gemini Client using your active API key
API_KEY = "AQ.Ab8RN6L8lx8b2sXBC8Q3zJArhdvdCfy_fw2M0zT00jXN-rEyHg"
client = genai.Client(api_key=API_KEY)

def analyze_review_with_gemini(raw_text: str):
    prompt = f"""
    You are the Principal ORM Specialist for top Indian E/Q-Commerce apps (Blinkit, Zepto, Swiggy Instamart).
    Analyze this live user review from the Indian Play Store. Handle any regional shortcuts/slang (e.g., 'mint' = minute).
    Provide strict, highly tactical corporate recommendations and draft professional responses.

    User Review: "{raw_text}"
    """
    
    # Brought back your preferred 3.8 Flash model
    response = client.models.generate_content(
        model='gemini-3.8-flash',
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=IndianORMAnalysis,
            temperature=0.2,
        ),
    )
    # Parse the text string back into a Python dictionary object
    return json.loads(response.text)

def process_and_save_live_reputation(app_bundle_id: str, count: int = 3):
    print(f"📡 Fetching live feeds from Google Play Store...")
    result, _ = reviews(
        app_bundle_id,
        lang='en',
        country='in',
        sort=Sort.NEWEST,
        count=count
    )
    
    print(f"✅ Grabbed {len(result)} live reviews. Launching AI Pipeline & Data Sync...\n")
    
    for i, review in enumerate(result, 1):
        user_name = review['userName']
        review_text = review['content']
        rating = review['score']
        
        print(f"==================================================")
        print(f"📝 Syncing Review #{i} by {user_name}...")
        print(f"💬 Text: \"{review_text}\"")
        
        try:
            # 1. Run Gemini Analysis
            ai_data = analyze_review_with_gemini(review_text)
            
            # 2. Package everything to send to Supabase
            database_payload = {
                "user_name": user_name,
                "review_text": review_text,
                "rating": int(rating),
                "category": ai_data.get("category"),
                "sub_category": ai_data.get("sub_category"),
                "urgency_score": float(ai_data.get("urgency_score", 5.0)),
                "sentiment": ai_data.get("sentiment"),
                "suggested_action": ai_data.get("suggested_action"),
                "draft_reply_english": ai_data.get("draft_reply_english"),
                "draft_reply_hindi": ai_data.get("draft_reply_hindi")
            }
            
            # 3. Fire it into your Cloud Database!
            supabase.table("brand_reviews").insert(database_payload).execute()
            print(f"   💾 Successfully stored in Supabase Cloud vault!")
            
        except Exception as e:
            print(f"   ❌ Pipeline error: {e}")
        
        # NEW: If there are more reviews left, pause for 5 seconds to prevent Google 503 limits
        if i < len(result):
            print("⏳ Pausing for 5 seconds to manage server load...")
            time.sleep(5)
            
        print(f"==================================================\n")

# Run the live pipeline for Blinkit
process_and_save_live_reputation('com.grofers.customerapp', count=3)
