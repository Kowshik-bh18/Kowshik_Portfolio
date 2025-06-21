import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Skills", page_icon="🧠")
st.title("🧠 Technical Skills & Tools")
st.markdown("### 💼 Tech I'm Comfortable With")

# ---------------------------
# 🧩 Skill categories with logos
# ---------------------------
skills = {
    "Languages": {
        "Python": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg",
        "Java": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg",
        "JavaScript": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg",
        "C": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/c/c-original.svg"
    },
    "Web & Frameworks": {
        "HTML": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg",
        "CSS": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg",
        "Bootstrap": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bootstrap/bootstrap-original.svg",
        "Django": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg",
        "Streamlit": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/streamlit/streamlit-original.svg"
    },
    "Databases": {
        "MySQL": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg",
        "MongoDB": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg",
        "PostgreSQL": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg"
    },
    "Cloud & DevOps": {
        "Google Cloud": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/googlecloud/googlecloud-original.svg",
        "CI/CD": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/gitlab/gitlab-original.svg",
        "Bash": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/bash/bash-original.svg"
    },
    "Tools & OS": {
        "Linux": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/linux/linux-original.svg",
        "Git": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg",
        "VS Code": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg",
        "Excel": "https://cdn.jsdelivr.net/gh/devicons/devicon/icons/microsoftsqlserver/microsoftsqlserver-plain.svg"
    }
}

# ---------------------------
# 🧠 Display each skill section
# ---------------------------
for category, techs in skills.items():
    st.markdown(f"#### 🔹 {category}")
    cols = st.columns(4)
    for i, (tech, logo) in enumerate(techs.items()):
        with cols[i % 4]:
            st.image(logo, width=40)
            st.markdown(f"**{tech}**", unsafe_allow_html=True)
    st.markdown("---")

# ---------------------------
# 📊 Proficiency Chart using Plotly
# ---------------------------
st.markdown("### 📊 Skill Proficiency Overview")

skill_levels = {
    "Python": "Advanced",
    "JavaScript": "Intermediate",
    "Java": "Intermediate",
    "C": "Intermediate",
    "HTML": "Intermediate",
    "CSS": "Intermediate",
    "Streamlit": "Intermediate"
}

level_map = {"Beginner": 1, "Intermediate": 2, "Advanced": 3}
df = pd.DataFrame({
    "Skill": list(skill_levels.keys()),
    "Level": [level_map[level] for level in skill_levels.values()]
})

fig = px.bar(
    df.sort_values("Level"),
    x="Skill",
    y="Level",
    color="Level",
    color_continuous_scale="Blues",
    labels={"Level": "Proficiency"},
    height=400
)

fig.update_layout(
    yaxis=dict(tickvals=[1, 2, 3], ticktext=["Beginner", "Intermediate", "Advanced"]),
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)

st.success("I enjoy combining these technologies to build smart, scalable systems.")
