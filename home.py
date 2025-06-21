import streamlit as st
from datetime import datetime
import requests

# --- Lottie Animation ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_animation = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_touohxv0.json")

# --- Page Config ---
st.set_page_config(page_title="Kowshik BH", page_icon="💻", layout="wide")
last_updated = datetime.now().strftime("%B %d, %Y")

# --- Custom CSS ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #f9fafe;
}
#MainMenu, footer, header {
    visibility: hidden;
}
.main-title {
    font-size: 3.5rem;
    font-weight: 800;
    text-align: center;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: fadeIn 2s ease-in-out;
}
.subtitle {
    text-align: center;
    font-size: 1.3rem;
    color: #666;
    margin-bottom: 2rem;
}
.nav-buttons {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin-bottom: 2rem;
}
.stButton>button {
    background: #667eea;
    border: none;
    color: white;
    padding: 0.5rem 1.2rem;
    font-size: 1rem;
    font-weight: 600;
    border-radius: 8px;
    cursor: pointer;
    transition: 0.2s;
}
.stButton>button:hover {
    background: #4e54c8;
    transform: translateY(-2px);
}
.section-card {
    background: #fff;
    padding: 2rem;
    border-radius: 15px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    margin: 2rem 0;
}
.footer-note {
    text-align: center;
    font-size: 0.9rem;
    margin-top: 4rem;
    color: #888;
}
</style>
""", unsafe_allow_html=True)

# --- Title & Subtitle ---
st.markdown('<h1 class="main-title">👨‍💻 Kowshik BH</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">CSE Student | Software & Web Developer | Python & Cloud Enthusiast</p>', unsafe_allow_html=True)

# --- Navigation Buttons ---
st.markdown('<div class="nav-buttons">', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🧠 Skills"):
        st.switch_page("pages/Skills.py")
with col2:
    if st.button("📁 Projects"):
        st.switch_page("pages/Projects.py")
with col3:
    if st.button("🏆 Achievements"):
        st.switch_page("pages/Achievements.py")
with col4:
    if st.button("📬 Contact"):
        st.switch_page("pages/Contact.py")
st.markdown('</div>', unsafe_allow_html=True)

# --- Social Links ---
st.markdown("""
<div style='text-align: center; margin-top: 1rem; margin-bottom: 2rem;'>
    <a href="https://www.linkedin.com/in/kowshikbh" target="_blank">
        <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin">
    </a>
    <a href="https://github.com/kowshik-bh18" target="_blank">
        <img src="https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github">
    </a>
    <a href="mailto:kobh22cs@cmrit.ac.in" target="_blank">
        <img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail">
    </a>
</div>
""", unsafe_allow_html=True)

# --- Career Objective ---
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown("### 🚀 Career Objective")
st.write("""
I’m actively seeking a dynamic role as a **Software/Web Developer** at a forward-thinking company.  
I bring strong skills in Python, Django, and modern web technologies, with a passion for collaboration and innovation.
""")
st.markdown('</div>', unsafe_allow_html=True)

# --- Education Section ---
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.markdown("### 🎓 Education")
st.write("""
- **B.E. in Computer Science** – CMRIT, Bengaluru — *CGPA: 8.9 (Ongoing)*  
- **12th – Science** – BGS PU College, Mandya — *97%*  
- **10th – SSLC** – Bhakthanatha Swamy HS, Mandya — *93%*
""")
st.markdown('</div>', unsafe_allow_html=True)

# --- Resume Download ---
st.markdown('<div class="section-card" style="text-align:center;">', unsafe_allow_html=True)
try:
    with open("KOWSHIK BH_RESUME.pdf", "rb") as f:
        resume_data = f.read()
    st.download_button("📄 Download My Resume", resume_data, file_name="KowshikBH_Resume.pdf", mime="application/pdf")
except FileNotFoundError:
    st.warning("📄 Resume file not found. Please add 'KOWSHIK BH_RESUME.pdf' to your root folder.")
st.markdown('</div>', unsafe_allow_html=True)

# --- Animation ---
st.markdown("### 👋 Thanks for visiting!")
if lottie_animation:
    st.components.v1.html(f"""
        <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
        <lottie-player src="https://assets1.lottiefiles.com/packages/lf20_touohxv0.json"
                       background="transparent" speed="1" style="width: 300px; height: 300px;" loop autoplay></lottie-player>
    """, height=300)
else:
    st.info("🎬 Animation failed to load.")

# --- Footer ---
st.markdown(f"""
<div class="footer-note">
    Made with ❤️ by <strong>Kowshik BH</strong><br>
    © 2025 • Last Updated: <strong>{last_updated}</strong>
</div>
""", unsafe_allow_html=True)
