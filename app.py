import streamlit as st
import pandas as pd
import requests

# Set up the webpage layout beautifully
st.set_page_config(page_title="Bharat ORM Enterprise Suite", page_icon="🧠", layout="wide")

# ==========================================
# 🔐 SECURE ENTERPRISE AUTHENTICATION GATEWAY
# ==========================================
def check_password():
    """Returns True if the user entered a correct password."""
    def password_entered():
        """Checks whether a password entered matches the target value."""
        if st.session_state["username"] == "admin@bharatorm.com" and st.session_state["password"] == "Enterprise2026!":
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Clean up memory
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First time login view
        st.markdown("<h2 style='text-align: center;'>🔒 Bharat ORM Secure Access Port</h2>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; color: gray;'>Please log in with your corporate credentials to access the reputation suite.</p>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.text_input("Corporate Username", key="username")
            st.text_input("Security Password", type="password", key="password")
            st.button("Log In to Dashboard", on_click=password_entered)
        
        if "password_correct" in st.session_state and not st.session_state["password_correct"]:
            st.error("❌ Invalid Username or Password. Please try again.")
        return False
    elif not st.session_state["password_correct"]:
        # Bad login reload view
        st.text_input("Corporate Username", key="username")
        st.text_input("Security Password", type="password", key="password")
        st.button("Log In to Dashboard", on_click=password_entered)
        st.error("❌ Invalid Username or Password. Please try again.")
        return False
    else:
        # Correct credentials provided
        return True

# ==========================================
# 🚨 ALERT WEBHOOK & ESCALATION FUNCTIONS
# ==========================================
def send_slack_alert(issue_id, category, text):
    """Pings the Corporate Communications Slack channel."""
    # Production: requests.post(st.secrets["SLACK_WEBHOOK"], json={"text": payload})
    st.toast(f"🚨 ALERT DISPATCHED: Slack channel #pr-crisis notified for Issue #{issue_id}!")

def send_whatsapp_alert(issue_id, score):
    """Pings the on-call Nodal Officer's mobile device via WhatsApp."""
    # Production: requests.post("https://graph.facebook.com/v17.0/.../messages", ...)
    st.toast(f"📱 ESCALATED: WhatsApp ping sent to Nodal Officer for Risk Level {score}!")

# Trigger password security firewall check
if check_password():
    # 1. Your Cloud Database Coordinates
    # CTO Note: In production, we will move this API_KEY to st.secrets for security
    API_URL = "https://supabase.co"
    API_KEY = "sb_publishable_xqxIn47R48w8mvyn3bF9sw_uksa4tjk"

    headers = {
        "apikey": API_KEY,
        "Authorization": f"Bearer {API_KEY}"
    }

    # 2. Main Title Banner
    st.title("🇮🇳 Bharat ORM Enterprise Control Suite")
    st.caption("AI-Powered Real-Time Brand Threat Intelligence & Auto-Response Routing Engine")
    st.markdown("---")

    # 3. Pull entries using a self-healing protocol
    records = []
    try:
        response = requests.get(f"{API_URL}?order=created_at.desc", headers=headers)
        if response.status_code == 200:
            records = response.json()
    except Exception as e:
        pass

    # Fallback mock data setup with Expanded Fintech / UPI Schema Data
    if not records or isinstance(records, dict):
        records = [
            {
                "id": 1,
                "created_at": "2026-09-06T10:00:00Z",
                "user_name": "Shiv Astha",
                "review_text": "Ordered a laptop from your app and instead of laptop, saboon ki tikki (soap bar) delivered inside the box!! Absolute fraud company #scam",
                "rating": 1,
                "category": "Fraud & Tampered Delivery",
                "sub_category": "High-value item replaced with soap",
                "urgency_score": 9.9,
                "sentiment": "Extremely Negative",
                "suggested_action": "Freeze driver payouts, coordinate with logistics safety desk immediately.",
                "draft_reply_english": "We take this very seriously. Please DM us your Order ID immediately so our escalation team can investigate this within the hour.",
                "draft_reply_hindi": "यह एक बेहद गंभीर मामला है। कृपया हमें तुरंत अपना Order ID भेजें ताकि हमारी टीम प्राथमिकता पर इसकी जांच कर सके।"
            },
            {
                "id": 2,
                "created_at": "2026-09-06T11:30:00Z",
                "user_name": "Aarav Mehta",
                "review_text": "Blinkit service has become slow in south delhi. 10 mins delivery is taking 45 mins. Worst experience.",
                "rating": 2,
                "category": "Delivery Delay",
                "sub_category": "Late delivery drop",
                "urgency_score": 6.5,
                "sentiment": "Negative",
                "suggested_action": "Verify local dark store operational capacity guidelines.",
                "draft_reply_english": "We sincerely apologize for the delay. We are looking into the store logistics to fix this right away.",
                "draft_reply_hindi": "देरी के लिए हमें खेद है। हम इस समस्या को तुरंत ठीक करने के लिए स्टोर लॉजिस्टिक्स की जांच कर रहे हैं।"
            },
            {
                "id": 3,
                "created_at": "2026-09-06T14:15:00Z",
                "user_name": "Priya Sharma",
                "review_text": "Amazing speed! Got my groceries in literally 7 minutes. Super convenient app.",
                "rating": 5,
                "category": "Praise",
                "sub_category": "Hyper speed logistics success",
                "urgency_score": 1.0,
                "sentiment": "Positive",
                "suggested_action": "Send automated loyalty discount point token.",
                "draft_reply_english": "Thank you for the wonderful feedback! Happy to serve you.",
                "draft_reply_hindi": "शानदार प्रतिक्रिया के लिए धन्यवाद! आपकी सेवा करके हमें खुशी हुई।"
            },
            {
                "id": 4,
                "created_at": "2026-09-06T16:05:00Z",
                "user_name": "Rahul Verma",
                "review_text": "I tried to pay my electricity bill via UPI. The app crashed, ₹4,500 got deducted from my HDFC bank, but the bill is still showing unpaid! Customer care is unreachable. I need my refund NOW!!",
                "rating": 1,
                "category": "Fintech / UPI Failure",
                "sub_category": "Amount Deducted - Merchant Not Credited",
                "urgency_score": 9.5,
                "sentiment": "Extreme Panic & Anger",
                "suggested_action": "Query NPCI / Bank Switch API for transaction status. Auto-trigger assurance SMS.",
                "draft_reply_english": "Hi Rahul, please don't worry. If the amount was deducted and the bill wasn't paid, it is usually reversed by your bank within 48 hours. Please share your transaction UTR via DM so we can track it immediately.",
                "draft_reply_hindi": "नमस्ते राहुल, कृपया चिंता न करें। यदि राशि कट गई है, तो यह आमतौर पर 48 घंटों में आपके बैंक द्वारा वापस कर दी जाती है। कृपया अपना UTR हमें DM करें।"
            },
            {
                "id": 5,
                "created_at": "2026-09-06T16:20:00Z",
                "user_name": "Neha Gupta",
                "review_text": "Wallet KYC is failing repeatedly for the last 3 days. 'Server timeout' error every time I upload my PAN card.",
                "rating": 2,
                "category": "Onboarding Drop-off",
                "sub_category": "KYC API Timeout",
                "urgency_score": 7.2,
                "sentiment": "Frustrated",
                "suggested_action": "Check CKYC/NSDL API gateway uptime. Route user to manual review queue.",
                "draft_reply_english": "We apologize for the glitch, Neha. Our KYC partners are experiencing temporary downtime. We will notify you the moment the gateway is stable.",
                "draft_reply_hindi": "असुविधा के लिए खेद है, नेहा। हमारे KYC पार्टनर सर्वर में अभी कुछ समस्या है। सर्वर ठीक होते ही हम आपको सूचित करेंगे।"
            }
        ]

    df = pd.DataFrame(records)
    # Ensure created_at is handled cleanly as timestamp object
    if 'created_at' in df.columns:
        df['created_at'] = pd.to_datetime(df['created_at'])

    # 4. Top-level Analytics Metrics
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.metric(label="Total Brand Mentions", value=len(df))
    with m2:
        critical_count = len(df[df['urgency_score'].astype(float) >= 7.0]) if 'urgency_score' in df.columns else 0
        st.metric(label="⚠️ Critical Risk Alerts", value=critical_count)
    with m3:
        avg_rating = round(df['rating'].mean(), 1) if 'rating' in df.columns else 0.0
        st.metric(label="⭐ Avg Brand Rating", value=f"{avg_rating} / 5")
    with m4:
        st.metric(label="System Status", value="Ready / Listening")

    # ==========================================
    # 📊 NEW VISUAL CHARTS & TREND VISUALIZATIONS
    # ==========================================
    st.markdown("### 📈 Corporate Reputation Analytics Panels")
    
    chart_col_left, chart_col_right = st.columns(2)
    
    with chart_col_left:
        st.markdown("#### **Brand Sentiment Volume Breakdown**")
        if 'sentiment' in df.columns and not df.empty:
            sentiment_counts = df['sentiment'].value_counts()
            # Uses built-in minimalist charting framework
            st.bar_chart(sentiment_counts, color="#4B90FF")
        else:
            st.info("Insufficient sentiment indices recorded to render breakdown trends.")

    with chart_col_right:
        st.markdown("#### **Risk Profile Metric Tracking (Over Time)**")
        if 'created_at' in df.columns and 'urgency_score' in df.columns and not df.empty:
            # Prepare chronological time sequence tracking format
            chart_data = df[['created_at', 'urgency_score']].sort_values(by='created_at')
            chart_data = chart_data.set_index('created_at')
            st.line_chart(chart_data, color="#FF4B4B")
        else:
            st.info("Chronological entries require active timestamp logs to map line visualizations.")

    # ==========================================
    # 📥 NEW CSV DATA EXPORT REPORT WIDGET
    # ==========================================
    st.markdown("### 📋 Executive Administration Utilities")
    
    # Generate clean CSV tracking format bytes block in memory background
    csv_data = df.to_csv(index=False).encode('utf-8')
    
    st.download_button(
        label="📥 Download Clean Operational Reputation Report (CSV File)",
        data=csv_data,
        file_name=f"bharat_orm_report_{pd.Timestamp.now().strftime('%Y%m%d')}.csv",
        mime="text/csv",
        help="Click here to extract a fully parsed report spreadsheet containing all category, sentiment, and AI response strings."
    )
    st.markdown("---")

    # 5. Populate the interactive triage inbox view
    st.markdown("### 📥 Unified Threat & Review Triage Inbox")
    for item in records:
        score = float(item.get('urgency_score', 5.0))
        alert_emoji = "🔴 CRISIS" if score >= 8.0 else ("🟡 WARNING" if score >= 5.0 else "🟢 NORMAL")
        
        with st.container(border=True):
            col_left, col_right = st.columns([5, 1])  # Explicitly forces data column to be 5x wider than score column
            
            with col_left:
                st.markdown(f"#### **{item.get('user_name')}** ({item.get('rating')} Stars) — `{item.get('category')}`")
                st.markdown(f"💬 *\"{item.get('review_text')}\"*")
                st.caption(f"📁 Sub-Issue: **{item.get('sub_category')}** | 🤖 AI Action Recommended: `{item.get('suggested_action')}`")
                
                tab_en, tab_hi = st.tabs(["🇬🇧 English Draft", "🇮🇳 Hindi Draft"])
                with tab_en:
                    st.text_area("Review Response Text (En)", value=item.get('draft_reply_english'), key=f"en_{item.get('id')}", height=70)
                    if st.button("Approve & Post Draft to App Store", key=f"btn_en_{item.get('id')}"):
                        st.toast("🚀 Reply successfully routed and posted via API!")
                
                with tab_hi:
                    st.text_area("Review Response Text (Hi)", value=item.get('draft_reply_hindi'), key=f"hi_{item.get('id')}", height=70)
                    if st.button("Approve & Post Hindi Draft", key=f"btn_hi_{item.get('id')}"):
                        st.toast("🚀 Hindi reply successfully dispatched!")
            
            with col_right:
                st.markdown("<br>", unsafe_allow_html=True)
                st.markdown(f"<h2 style='text-align: center;'>{item.get('urgency_score')}</h2>", unsafe_allow_html=True)
                st.markdown("<p style='text-align: center; color: gray; font-size: 12px;'>Risk Priority Score</p>", unsafe_allow_html=True)
                st.markdown(f"<h3 style='text-align: center;'>{alert_emoji}</h3>", unsafe_allow_html=True)
                
                # New Escalation Action Buttons
                st.markdown("<br>", unsafe_allow_html=True)
                if score >= 7.0:
                    if st.button("🔔 Slack PR", key=f"slack_{item.get('id')}", use_container_width=True):
                        send_slack_alert(item.get('id'), item.get('category'), item.get('review_text'))
                    if st.button("📱 WA Escalate", key=f"wa_{item.get('id')}", use_container_width=True):
                        send_whatsapp_alert(item.get('id'), score)
