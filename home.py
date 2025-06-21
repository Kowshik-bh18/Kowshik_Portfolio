import streamlit as st
from PIL import Image
from datetime import datetime
import requests
import json

# Load Lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_animation = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_touohxv0.json")

# Page configuration
st.set_page_config(page_title="Kowshik BH", page_icon="💻", layout="wide")

# Last updated
last_updated = datetime.now().strftime("%B %d, %Y")

# Custom CSS
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Inter', sans-serif;
        background-color: #f9fafe;
    }}

    #MainMenu, footer, header {{
        visibility: hidden;
    }}

    .main .block-container {{
        padding-top: 2rem;
        max-width: 1200px;
    }}

    .main-title {{
        font-size: 3rem;
        font-weight: 700;
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: slideInDown 1s ease-out;
    }}

    .subtitle {{
        text-align: center;
        font-size: 1.3rem;
        color: #666;
        margin-bottom: 2rem;
        animation: fadeInUp 1s ease-out 0.3s both;
    }}

    .social-links {{
        display: flex;
        justify-content: center;
        gap: 1.5rem;
        margin: 2rem 0;
        animation: fadeInUp 1s ease-out 0.6s both;
    }}

    .section-card {{
        background: #fff;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        margin: 2rem 0;
        border: 1px solid rgba(0,0,0,0.05);
        animation: fadeInUp 0.8s ease-out;
    }}

    .career-objective {{
        background: linear-gradient(135deg, #f8f9ff 0%, #e8f2ff 100%);
        border-left: 4px solid #667eea;
        padding: 1.5rem;
        border-radius: 10px;
        font-size: 1.1rem;
        line-height: 1.6;
        animation: slideInRight 1s ease-out 0.8s both;
    }}

    .education-content {{
        font-size: 1.1rem;
        line-height: 1.8;
        color: #444;
        padding: 1rem;
        background: linear-gradient(135deg, #fff 0%, #f8f9fa 100%);
        border-radius: 10px;
        border-left: 4px solid #28a745;
        animation: slideInLeft 1s ease-out 1s both;
    }}

    .download-section {{
        text-align: center;
        margin: 3rem 0;
        animation: bounceIn 1s ease-out 1.2s both;
    }}

    .stDownloadButton > button {{
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        font-size: 1.1rem;
        color: white;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }}

    .stDownloadButton > button:hover {{
        transform: translateY(-3px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.4);
    }}

    @keyframes slideInDown {{
        from {{ opacity: 0; transform: translateY(-50px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}

    @keyframes fadeInUp {{
        from {{ opacity: 0; transform: translateY(30px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}

    @keyframes slideInRight {{
        from {{ opacity: 0; transform: translateX(50px); }}
        to {{ opacity: 1; transform: translateX(0); }}
    }}

    @keyframes slideInLeft {{
        from {{ opacity: 0; transform: translateX(-50px); }}
        to {{ opacity: 1; transform: translateX(0); }}
    }}

    @keyframes bounceIn {{
        0% {{ opacity: 0; transform: scale(0.3); }}
        50% {{ opacity: 1; transform: scale(1.05); }}
        70% {{ transform: scale(0.9); }}
        100% {{ opacity: 1; transform: scale(1); }}
    }}

    .footer-note {{
        text-align: center;
        font-size: 0.9rem;
        margin-top: 4rem;
        color: #888;
    }}

    .footer-note span {{
        color: #e25555;
    }}

    /* Sidebar Gradient */
    section[data-testid="stSidebar"] > div:first-child {{
        background: linear-gradient(135deg, #4e54c8, #8f94fb);
        border-radius: 0px 20px 20px 0px;
        height: 100%;
        padding-top: 3rem;
        color: white;
    }}

    section[data-testid="stSidebar"] .block-container {{
        color: white;
    }}
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## 📂 Navigation", unsafe_allow_html=True)
    st.markdown("""
- 🏠 Home  
- 🧠 Skills  
- 📁 Projects  
- 🏆 Achievements  
- 📞 Contact
""")

# Main Title
st.markdown('<h1 class="main-title">👨‍💻 Kowshik BH</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">CSE Student | Software & Web Developer | Python & Django Enthusiast</p>', unsafe_allow_html=True)

# Social links
st.markdown("""
<div class="social-links">
    <a href="https://www.linkedin.com/in/kowshikbh" target="_blank">
        <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin" height="35">
    </a>
    <a href="https://github.com/kowshik-bh18" target="_blank">
        <img src="https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github" height="35">
    </a>
    <a href="mailto:kobh22cs@cmrit.ac.in" target="_blank">
        <img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail" height="35">
    </a>
</div>
""", unsafe_allow_html=True)

# Career Objective Section
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown("### 🚀 Career Objective")
st.markdown("""
<div class="career-objective">
• I am actively seeking a dynamic IT role as a <strong>Software Developer or Web Developer</strong> at a forward-thinking company.<br><br>
• I bring a robust skill set in web and software development, bolstered by a strong work ethic, effective leadership, and exceptional adaptability.<br><br>
• I am enthusiastic about the opportunity to collaborate with experienced professionals, leveraging their expertise to enhance my skills and knowledge.
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Education Section
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown("### 🎓 Education")
st.markdown("""
<div class="education-content">
<strong>Bachelor of Engineering - Computer Science & Engineering</strong><br>
CMR Institute of Technology, Bengaluru<br>
<strong>CGPA:</strong> 8.9 | <strong>Expected Graduation:</strong> 2026 (pursuing)<br><br>

<strong>12th Grade - Science</strong><br>
BGS Independent PU College, Mandya<br>
<strong>Percentage:</strong> 97% | <strong>Year:</strong> 2022<br><br>

<strong>10th Grade</strong><br>
Sri Bhakthanatha Swamy High School, Mandya<br>
<strong>Percentage:</strong> 93% | <strong>Year:</strong> 2020
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Resume Download
st.markdown('<div class="download-section">', unsafe_allow_html=True)
try:
    with open("KOWSHIK BH_RESUME.pdf", "rb") as f:
        resume_data = f.read()
    st.download_button("📄 Download My Resume", resume_data, file_name="KowshikBH_Resume.pdf", mime="application/pdf")
except FileNotFoundError:
    st.info("📄 Resume file not found. Please add 'KOWSHIK BH_RESUME.pdf' to your project directory.")
st.markdown('</div>', unsafe_allow_html=True)

# Final Animation
st.markdown("---")
st.markdown("### 👋 Thanks for visiting!")
if lottie_animation:
    st_lottie = st.components.v1.html(f"""
    <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
    <lottie-player src="https://assets1.lottiefiles.com/packages/lf20_touohxv0.json"
                   background="transparent" speed="1" style="width: 300px; height: 300px;" loop autoplay></lottie-player>
    """, height=300)
else:
    st.info("✨ Final animation failed to load. Check your internet or Lottie URL.")

# Footer
st.markdown(f"""
<div class="footer-note">
    <p>Made with <span>❤️</span> by <strong>Kowshik BH</strong><br>
    © 2025 | Last Updated: <strong>{last_updated}</strong></p>
</div>
""", unsafe_allow_html=True)
