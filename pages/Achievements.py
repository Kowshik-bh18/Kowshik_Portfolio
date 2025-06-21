import streamlit as st

st.set_page_config(page_title="Achievements", page_icon="🏆")
st.title("🏆 Achievements & Certifications")
st.markdown("### ✨ *“Every milestone reflects consistent effort and curiosity.”*")

# === 🏁 Achievements Section ===
st.markdown("## 👨‍💻 Technical Achievements")
st.markdown("""
- 🥈 Finalist in intra-college hackathon for building a scalable utility tracker  
- 🤖 Developed an AI/ML Roadmap Generator using RAG model (*in progress*)  
- 🧠 Created memory & logic game suite using Django  
- 📊 Built real-time dashboards with login and MongoDB analytics  
- 🚀 Hosted secure apps using Streamlit Cloud  
""")

# === 🎓 Certifications Section ===
st.markdown("## 🎓 Certifications")

# === Udemy Certifications ===
st.image("https://img.icons8.com/color/48/udemy.png", width=40)
st.markdown("### 🧠 Udemy Certifications")

udemy_certs = [
    {
        "title": "Python Programming",
        "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg",
        "status": "Completed"
    },
    {
        "title": "Django Web Development",
        "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg",
        "status": "Completed"
    },
    {
        "title": "Java Development",
        "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg",
        "status": "Completed"
    },
    {
        "title": "JavaScript Essentials",
        "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg",
        "status": "Completed"
    },
    {
        "title": "RAG-based AI Roadmap",
        "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg",
        "status": "In Progress"
    }
]

cols = st.columns(3)
for idx, cert in enumerate(udemy_certs):
    with cols[idx % 3]:
        st.markdown(f"""
        <div style='
            border: 1px solid #e0e0e0;
            border-radius: 10px;
            padding: 15px;
            margin: 10px 0;
            background-color: #f9f9f9;
            text-align: center;
            box-shadow: 0 0 8px rgba(0,0,0,0.05);
            transition: transform 0.3s;
        '>
            <img src="{cert['logo']}" width="40" style="margin-bottom: 10px;" />
            <h5 style="margin-bottom: 5px;">{cert['title']}</h5>
            <span style="color: {"green" if cert['status']=="Completed" else "orange"};">
                <strong>{cert['status']}</strong>
            </span>
        </div>
        """, unsafe_allow_html=True)

# === Google Cloud Certifications ===
st.markdown("---")
st.image("https://img.icons8.com/color/48/google-cloud.png", width=40)
st.markdown("### ☁️ Google Cloud Certifications")

google_certs = [
    {
        "title": "Google Cloud Essentials",
        "logo": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/googlecloud/googlecloud-original.svg",
        "status": "Completed"
    }
]

cols = st.columns(3)
for idx, cert in enumerate(google_certs):
    with cols[idx % 3]:
        st.markdown(f"""
        <div style='
            border: 1px solid #e0e0e0;
            border-radius: 10px;
            padding: 15px;
            margin: 10px 0;
            background-color: #f0f9ff;
            text-align: center;
            box-shadow: 0 0 8px rgba(0,0,0,0.05);
        '>
            <img src="{cert['logo']}" width="40" style="margin-bottom: 10px;" />
            <h5 style="margin-bottom: 5px;">{cert['title']}</h5>
            <span style="color: {"green" if cert['status']=="Completed" else "orange"};">
                <strong>{cert['status']}</strong>
            </span>
        </div>
        """, unsafe_allow_html=True)

# === 🧪 Workshops Section ===
st.markdown("## 🏫 Workshops Attended")
st.markdown("""
- 📊 **Data Science Fundamentals** – Hands-on session on ML basics and Pandas  
- 📈 **Data Visualization** – Workshop using Python, Tableau & real datasets  
""")

# === 🤔 Curiosity Box ===
with st.expander("🤔 Fun Fact"):
    st.info("""
The RAG model in my AI Roadmap Generator dynamically adapts learning plans based on user type (e.g., slow, fast, intermediate learner).  
It’s like having a smart tutor who personalizes your study journey in real time!
""")

# === 🎉 Ending Animation ===
st.markdown("---")
st.markdown("🌟 *“Skills compound. Keep learning, keep winning.”*")
st.balloons()
