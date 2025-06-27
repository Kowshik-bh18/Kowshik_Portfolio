import streamlit as st
from pymongo import MongoClient
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
import requests
import time
import pandas as pd
from streamlit_lottie import st_lottie
import json

# --- Page Config ---
st.set_page_config(
    page_title="Contact - Kowshik BH", 
    page_icon="📬", 
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- Custom CSS for Modern Styling ---
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    .main {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Hero Section */
    .hero-section {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 3rem 2rem;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 2rem;
        color: white;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }
    
    .hero-title {
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .hero-subtitle {
        font-size: 1.2rem;
        font-weight: 300;
        opacity: 0.9;
    }
    
    /* Contact Form Styling */
    .contact-form {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }
    
    /* Stats Cards */
    .stat-card {
        background: linear-gradient(145deg, #f0f0f0, #cacaca);
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 700;
        color: #667eea;
    }
    
    .stat-label {
        font-size: 0.9rem;
        color: #666;
        margin-top: 0.5rem;
    }
    
    /* Social Media Buttons */
    .social-button {
        display: inline-block;
        padding: 12px 24px;
        margin: 8px;
        background: linear-gradient(45deg, #667eea, #764ba2);
        color: white;
        text-decoration: none;
        border-radius: 50px;
        font-weight: 500;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }
    
    .social-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.6);
        text-decoration: none;
        color: white;
    }
    
    /* Feedback Section */
    .feedback-section {
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
        padding: 2rem;
        border-radius: 20px;
        margin: 2rem 0;
    }
    
    /* Timeline Styles */
    .timeline-item {
        border-left: 3px solid #667eea;
        padding-left: 1rem;
        margin-bottom: 1rem;
        position: relative;
    }
    
    .timeline-item::before {
        content: '';
        position: absolute;
        left: -6px;
        top: 0;
        width: 12px;
        height: 12px;
        background: #667eea;
        border-radius: 50%;
    }
    
    /* Quick Actions */
    .quick-action {
        background: rgba(102, 126, 234, 0.1);
        border: 2px solid #667eea;
        border-radius: 15px;
        padding: 1rem;
        text-align: center;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    
    .quick-action:hover {
        background: rgba(102, 126, 234, 0.2);
        transform: scale(1.05);
    }
    
    /* Response Time Badge */
    .response-badge {
        background: linear-gradient(45deg, #4CAF50, #45a049);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 500;
        display: inline-block;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

# --- Load Lottie Animations ---
def load_lottie_url(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

def load_lottie_local(filepath: str):
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except:
        return None

# Lottie animation URLs
contact_animation = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_u25cckyh.json")
success_animation = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_xlkxtmul.json")
email_animation = load_lottie_url("https://assets4.lottiefiles.com/packages/lf20_8pgxhzgf.json")

# --- MongoDB Setup ---
@st.cache_resource
def init_connection():
    try:
        cluster = MongoClient(st.secrets["MONGO_URI"])
        return cluster["portfolio"]
    except Exception as conn_err:
        st.error("⚠️ Could not connect to MongoDB.")
        st.stop()

db = init_connection()

# --- Hero Section ---
st.markdown("""
<div class="hero-section">
    <h1 class="hero-title">Let's Connect! 🎓</h1>
    <p class="hero-subtitle">Computer Science Student | Ready to collaborate on projects, share ideas, or discuss tech!</p>
    <div class="response-badge">⚡ Typical response time: 4-8 hours (between classes)</div>
</div>
""", unsafe_allow_html=True)

# --- Real-time Statistics ---
col1, col2, col3, col4 = st.columns(4)

try:
    # Get various statistics
    total_messages = db["messages"].count_documents({})
    total_visits = db["visits"].find_one({"_id": "contact_page"}, {"count": 1})
    total_visits = total_visits["count"] if total_visits else 0
    
    # Messages this week
    week_ago = datetime.now() - timedelta(days=7)
    messages_this_week = db["messages"].count_documents({
        "timestamp": {"$gte": week_ago}
    })
    
    # Average response satisfaction
    feedback_data = list(db["feedback"].find({"page": "contact"}))
    satisfaction = len([f for f in feedback_data if "👍" in f.get("response", "")]) / max(len(feedback_data), 1) * 100
    
    with col1:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{total_messages}</div>
            <div class="stat-label">Total Messages</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{total_visits}</div>
            <div class="stat-label">Page Views</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{messages_this_week}</div>
            <div class="stat-label">This Week</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-number">{satisfaction:.0f}%</div>
            <div class="stat-label">Satisfaction</div>
        </div>
        """, unsafe_allow_html=True)

except Exception as e:
    st.warning("Statistics temporarily unavailable")

st.markdown("---")

# --- Main Contact Section ---
contact_col1, contact_col2 = st.columns([1, 1])

with contact_col1:
    st.markdown("### 📬 Send me a message")
    
    # Contact form with enhanced features
    with st.form("enhanced_contact_form", clear_on_submit=True):
        # Basic contact info
        name = st.text_input("👤 Your Name", placeholder="John Doe")
        email = st.text_input("📧 Your Email", placeholder="john@example.com")
        
        # Enhanced fields
        subject = st.selectbox("📋 Subject", [
            "Project Collaboration",
            "Study Group/Academic Help", 
            "Internship Opportunity",
            "Technical Question",
            "Assignment Help",
            "Coding Doubt",
            "General Chat",
            "Other"
        ])
        
        priority = st.select_slider("⚡ Priority", ["Low", "Medium", "High", "Urgent"])
        
        message = st.text_area("✍️ Your Message", 
                              placeholder="Tell me about your project idea, study doubt, or how we can collaborate...",
                              height=120)
        
        # Additional options
        col_a, col_b = st.columns(2)
        with col_a:
            newsletter = st.checkbox("📚 Get study updates")
        with col_b:
            study_buddy = st.checkbox("👥 Looking for study buddy")
        
        # File attachment (simulated)
        uploaded_file = st.file_uploader("📎 Attach file (optional)", 
                                       type=['pdf', 'doc', 'docx', 'txt', 'png', 'jpg'])
        
        submitted = st.form_submit_button("🚀 Send Message", use_container_width=True)
        
        if submitted:
            if name and email and message:
                try:
                    # Enhanced message data
                    message_data = {
                        "name": name,
                        "email": email,
                        "subject": subject,
                        "priority": priority,
                        "message": message,
                        "study_updates": newsletter,
                        "study_buddy": study_buddy,
                        "timestamp": datetime.now(),
                        "has_attachment": uploaded_file is not None,
                        "status": "new"
                    }
                    
                    db["messages"].insert_one(message_data)
                    
                    # Show success animation
                    if success_animation:
                        st_lottie(success_animation, height=100, key="success")
                    
                    st.success("✅ Message sent successfully!")
                    st.balloons()
                    
                    # Show estimated response time
                    response_time = "4-6 hours" if priority in ["High", "Urgent"] else "8-24 hours"
                    st.info(f"📅 Expected response time: {response_time} (depending on class schedule)")
                    
                except Exception as e:
                    st.error(f"❌ Could not send message. Please try again later.")
            else:
                st.warning("⚠️ Please fill in the required fields (Name, Email, Message).")

with contact_col2:
    st.markdown("### 🎓 Why connect with me?")
    
    # Lottie animation
    if contact_animation:
        st_lottie(contact_animation, height=200, key="contact")
    
    # Quick action buttons
    st.markdown("#### 🎯 Quick Actions")
    
    quick_actions = [
        ("📚 Study Together", "Looking for a study partner"),
        ("🤝 Collaborate", "Have a project idea to work on"),
        ("❓ Get Help", "Need help with assignments/coding"),
        ("💡 Share Idea", "Want to discuss a cool project")
    ]
    
    for action, description in quick_actions:
        if st.button(action, key=action, use_container_width=True):
            st.info(f"Great choice! {description}. Please fill out the form with details.")

# --- Interactive FAQ Section ---
st.markdown("---")
st.markdown("### ❓ Frequently Asked Questions")

faq_data = {
    "🕐 How quickly do you respond?": "I typically respond within 4-8 hours during weekdays (between classes), and within 12-24 hours on weekends.",
    "📚 What subjects can you help with?": "I can help with Computer Science topics, programming (Python, Java, C++), web development, data structures, and algorithms.",
    "🤝 Are you available for group projects?": "Absolutely! I love collaborating on academic projects and hackathons. Let's discuss your project requirements.",
    "💻 Do you do coding assignments?": "I can help explain concepts and guide you through problems, but I encourage learning rather than just providing solutions.",
    "🎓 What's your academic background?": "I'm currently pursuing Computer Science at CMRIT. I'm passionate about software development and emerging technologies.",
    "📱 What's the best way to reach you?": "Email works best for detailed discussions, but feel free to connect on LinkedIn for quick questions or networking."
}

selected_faq = st.selectbox("Select a question:", list(faq_data.keys()))
if selected_faq:
    st.info(faq_data[selected_faq])

# --- Contact Analytics Dashboard ---
st.markdown("---")
st.markdown("### 📊 Contact Analytics")

try:
    # Message trend over time
    messages = list(db["messages"].find({}, {"timestamp": 1, "subject": 1, "priority": 1}))
    
    if messages:
        df = pd.DataFrame(messages)
        df['date'] = pd.to_datetime(df['timestamp']).dt.date
        
        # Daily message count
        daily_counts = df.groupby('date').size().reset_index(name='count')
        
        fig_trend = px.line(daily_counts, x='date', y='count', 
                           title='📈 Daily Messages Trend',
                           color_discrete_sequence=['#667eea'])
        fig_trend.update_layout(height=300)
        st.plotly_chart(fig_trend, use_container_width=True)
        
        # Subject distribution
        col_chart1, col_chart2 = st.columns(2)
        
        with col_chart1:
            subject_counts = df['subject'].value_counts()
            fig_pie = px.pie(values=subject_counts.values, names=subject_counts.index,
                           title='📋 Message Categories')
            fig_pie.update_layout(height=300)
            st.plotly_chart(fig_pie, use_container_width=True)
        
        with col_chart2:
            priority_counts = df['priority'].value_counts()
            fig_bar = px.bar(x=priority_counts.index, y=priority_counts.values,
                           title='⚡ Message Priority Distribution',
                           color_discrete_sequence=['#ff9a9e'])
            fig_bar.update_layout(height=300)
            st.plotly_chart(fig_bar, use_container_width=True)

except Exception as e:
    st.caption("📊 Analytics will appear after receiving messages")

# --- Enhanced Feedback Section ---
st.markdown("---")
st.markdown("""
<div class="feedback-section">
    <h3>💝 Your Experience Matters</h3>
    <p>Help me improve by sharing your thoughts about this contact page!</p>
</div>
""", unsafe_allow_html=True)

feedback_col1, feedback_col2 = st.columns([1, 2])

with feedback_col1:
    feedback = st.radio("Rate this page:", 
                       ["⭐⭐⭐⭐⭐ Excellent", "⭐⭐⭐⭐ Good", "⭐⭐⭐ Average", "⭐⭐ Poor", "⭐ Terrible"], 
                       horizontal=False)

with feedback_col2:
    improvement = st.text_area("What could be improved?", 
                              placeholder="Suggestions for better collaboration, study resources, or features you'd like to see...")
    
    contact_method = st.selectbox("Best way to connect?", 
                                 ["Email", "LinkedIn", "WhatsApp", "Discord", "No preference"])

if st.button("💌 Submit Feedback", use_container_width=True):
    try:
        feedback_data = {
            "page": "contact",
            "rating": feedback,
            "improvement": improvement,
            "preferred_contact": contact_method,
            "timestamp": datetime.now()
        }
        db["feedback"].insert_one(feedback_data)
        st.success("✅ Thank you for your valuable feedback!")
        st.snow()
    except Exception as e:
        st.error("⚠️ Could not record feedback. Please try again.")

# --- Enhanced Social Media Section ---
st.markdown("---")
st.markdown("### 🌐 Connect & Follow My Journey")

# Social media with enhanced styling
st.markdown("""
<div style="text-align: center; margin: 2rem 0;">
    <a href="https://github.com/Kowshik-bh18" class="social-button">
        💻 GitHub Projects
    </a>
    <a href="https://www.linkedin.com/in/kowshik-bh-0b750b309/" class="social-button">
        🎓 LinkedIn Profile
    </a>
    <a href="mailto:kobh22cs@cmrit.ac.in" class="social-button">
        📧 Email Me
    </a>
    <a href="tel:+917483226281" class="social-button">
        📱 Call/WhatsApp
    </a>
</div>
""", unsafe_allow_html=True)

# Alternative contact methods
st.markdown("#### 📱 Best Ways to Reach Me")
alt_contact_cols = st.columns(3)

with alt_contact_cols[0]:
    st.markdown("""
    **📧 Email**  
    kobh22cs@cmrit.ac.in  
    *Best for project discussions*
    """)

with alt_contact_cols[1]:
    st.markdown("""
    **📱 WhatsApp**  
    +91 7483226281  
    *Available 8 AM - 10 PM IST*
    """)

with alt_contact_cols[2]:
    st.markdown("""
    **🎓 LinkedIn**  
    Academic & Professional  
    *Connect for opportunities*
    """)

# --- Visit Counter with Enhanced Visualization ---
st.markdown("---")
st.markdown("### 📈 Page Analytics")

try:
    # Update visit counter
    counter = db["visits"].find_one({"_id": "contact_page"})
    if counter:
        db["visits"].update_one({"_id": "contact_page"}, {"$inc": {"count": 1}})
        views = counter["count"] + 1
    else:
        db["visits"].insert_one({"_id": "contact_page", "count": 1})
        views = 1
    
    # Enhanced visitor counter visualization
    fig = go.Figure()
    
    fig.add_trace(go.Indicator(
        mode="number+delta+gauge",
        value=views,
        domain={'x': [0, 1], 'y': [0, 1]},
        number={'suffix': " visits", 'font': {'size': 40}},
        title={"text": "🎯 Total Page Visits", 'font': {'size': 20}},
        delta={'reference': views - 1, 'increasing': {'color': "#667eea"}},
        gauge={
            'axis': {'range': [None, views * 1.2]},
            'bar': {'color': "#667eea"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "#667eea",
            'steps': [
                {'range': [0, views * 0.5], 'color': 'lightgray'},
                {'range': [views * 0.5, views * 0.8], 'color': 'gray'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': views * 0.9
            }
        }
    ))
    
    fig.update_layout(height=300, font={'color': "#667eea", 'family': "Poppins"})
    st.plotly_chart(fig, use_container_width=True)
    
except Exception as e:
    st.caption("📊 Visit tracking temporarily unavailable")

# --- Footer with Enhanced Styling ---
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 2rem 0; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
            border-radius: 20px; color: white; margin-top: 2rem;'>
    <h4 style='margin-bottom: 1rem;'>🎓 Thanks for Stopping By!</h4>
    <p style='margin: 0.5rem 0;'>© 2025 Kowshik BH | CS Student @ CMRIT | Built with ❤️ using Python & Streamlit</p>
    <p style='margin: 0.5rem 0; opacity: 0.8;'>
        🌟 Always excited to connect with fellow students and tech enthusiasts! 
        <br>
        💡 "Learning is better when shared with others"
    </p>
    <div style='margin-top: 1rem; font-size: 0.9rem; opacity: 0.7;'>
        Currently in: Final Year | Available for: Projects & Collaborations
    </div>
</div>
""", unsafe_allow_html=True)

# --- Real-time Notifications (Simulated) ---
if st.sidebar.button("🔔 Check Notifications"):
    try:
        recent_messages = db["messages"].count_documents({
            "timestamp": {"$gte": datetime.now() - timedelta(hours=24)}
        })
        st.sidebar.success(f"📬 {recent_messages} new messages in the last 24 hours")
    except:
        st.sidebar.info("📡 Notification system offline")

# --- Session State Management ---
if 'page_loaded' not in st.session_state:
    st.session_state.page_loaded = datetime.now()
    
session_duration = datetime.now() - st.session_state.page_loaded
st.sidebar.caption(f"⏱️ Session: {int(session_duration.total_seconds())}s")
