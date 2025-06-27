import streamlit as st
import plotly.express as px
import pandas as pd

st.set_page_config(page_title="Projects", page_icon="📁")
st.title("📁 Projects Showcase")
st.markdown("Explore my practical experience through these real-world development projects:")

# ✅ Resume-based + detailed project list
projects = [
    {
        "name": "Dormitory Management System",
        "desc": "A full-stack web app to manage hostel operations such as student registrations, room assignments, and admin analytics.",
        "stack": ["Django", "MySQL", "HTML5", "CSS3"],
        "github": "https://github.com/Kowshik-bh18/Dormitory_Management_System",
        "status": "Completed",
        "details": """
### 🔧 Features:
- Admin authentication and secure dashboard  
- Add, update, delete student records  
- Allocate rooms dynamically  
- Track room status and generate allocation reports  
- Real-time search and filters  
### 🧠 What I Learned:
- Django ORM for efficient queries  
- Dashboard structuring with dynamic views  
- CRUD and security implementation  
"""
    },
    {
        "name": "Gym Management System",
        "desc": "A member and staff tracking system for gym environments, with scheduling and trainer assignment features.",
        "stack": ["Django", "SQLite", "HTML5", "CSS3"],
        "github": "https://github.com/Kowshik-bh18/gym-management",
        "status": "Completed",
        "details": """
### 🔧 Features:
- Register/manage gym members  
- Assign workout schedules and trainers  
- View trainer availability  
- Export monthly reports  
### 🧠 What I Learned:
- Django Admin customization  
- Efficient use of SQLite in development  
- UI layout using Bootstrap inside Django templates  
"""
    },
    {
        "name": "Password Generator Tool",
        "desc": "An interactive tool that generates strong passwords based on user-chosen criteria like length, symbols, and numbers.",
        "stack": ["Python", "JavaScript"],
        "github": "https://github.com/Kowshik-bh18/password-check",
        "status": "Completed",
        "details": """
### 🔧 Features:
- Password length customization  
- Toggle for special characters, numbers, uppercase  
- Real-time feedback on strength  
### 🧠 What I Learned:
- Using JavaScript for instant UI updates  
- Generating secure random passwords in Python  
- Regex and validation techniques  
"""
    },
    {
        "name": "Hangman CLI Game",
        "desc": "A classic CLI game built with Python that lets users guess random words with limited tries.",
        "stack": ["Python"],
        "github": "https://github.com/Kowshik-bh18/Hangman",
        "status": "Completed",
        "details": """
### 🔧 Features:
- Word bank of over 100 terms  
- Tracks lives, guessed letters, and score  
- CLI interface with ASCII art  
### 🧠 What I Learned:
- Python logic and loops  
- Error handling and user input flow  
- Game state management  
"""
    },
    {
        "name": "Social Media Platform Prototype",
        "desc": "A basic social media prototype with post creation, likes, and simple comment structure.",
        "stack": ["Django", "HTML5", "CSS3", "SQLite"],
        "github": "https://github.com/Kowshik-bh18/social_media_app",
        "status": "In Progress",
        "details": """
### 🔧 Features:
- Create and display user posts  
- Like tracking with counts  
- Comment model in prototype phase  
### 🧠 What I Learned:
- Advanced Django model relations  
- CSRF and session handling  
- Template reuse and layout inheritance  
"""
    }
]

# 🔗 Logo references
logos = {
    "Python": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg",
    "JavaScript": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg",
    "Django": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg",
    "MySQL": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg",
    "HTML5": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg",
    "CSS3": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg",
    "SQLite": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg"
}

# 🧩 Render projects
for project in projects:
    with st.container():
        st.subheader(f"🔹 {project['name']}")
        st.write(project['desc'])

        st.markdown("**🛠 Tech Stack:**")
        cols = st.columns(len(project['stack']))
        for i, tech in enumerate(project['stack']):
            with cols[i % 4]:
                st.image(logos.get(tech, ""), width=40)
                st.markdown(f"**{tech}**")

        st.markdown(
            f"[![GitHub](https://img.shields.io/badge/View%20on%20GitHub-black?style=for-the-badge&logo=github)]({project['github']})",
            unsafe_allow_html=True
        )

        with st.expander("🔍 More Information"):
            st.markdown(project["details"])
            st.markdown(f"**Status:** `{project['status']}`")

        st.markdown("---")

# 📊 Visualization: Project Completion Chart
st.markdown("### 📈 Project Completion Summary")

df = pd.DataFrame([proj["status"] for proj in projects], columns=["Status"])
status_counts = df["Status"].value_counts().reset_index()
status_counts.columns = ["Status", "Count"]

fig = px.bar(status_counts, x="Status", y="Count", color="Status",
             title="Projects by Status",
             color_discrete_sequence=px.colors.qualitative.Safe)

st.plotly_chart(fig, use_container_width=True)
