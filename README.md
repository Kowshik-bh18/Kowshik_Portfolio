# 🚀 Kowshik BH — Developer Portfolio

Welcome to my interactive **developer portfolio** built with `Streamlit`, `Python`, and `MongoDB`. This application showcases my skills, achievements, projects, and contact capabilities—all in one seamless web app.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat&logo=mongodb&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=flat&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black)

---

## 🌟 Features

- 📌 **Home Page** with animated intro and theme switcher.
- 🧠 **Skills Section** displaying technical proficiencies.
- 💼 **Projects Section** with interactive visuals.
- 🏆 **Achievements Section** to highlight milestones.
- 📬 **Contact Form** with MongoDB integration.
- 📊 **Visitor Counter** with live updates via Plotly.
- 🌗 **Dark Mode** and responsive UI.

---

## 🛠️ Tech Stack

| Area            | Technologies Used                                  |
|-----------------|----------------------------------------------------|
| **Frontend**    | Streamlit, HTML5, CSS3, JavaScript (minimal)       |
| **Backend**     | Python 3, Streamlit Framework                      |
| **Database**    | MongoDB (via MongoDB Atlas or Compass)             |
| **Libraries**   | `pymongo`, `plotly`, `PIL`, `Lottie`, `requests`   |
| **Deployment**  | Streamlit Cloud                                     |

---

## 📂 Folder Structure

Kowshik_Portfolio/
│
├── .devcontainer/ # VS Code container settings (optional)
├── .streamlit/ # Theme and config settings
├── pages/ # Streamlit multipage content
│ ├── Skills.py
│ ├── Projects.py
│ ├── Achievements.py
│ └── Contact.py
├── utils/ # Helper functions/utilities
├── home.py # Main home page
├── requirements.txt # Project dependencies
├── KOWSHIK_BH_RESUME.pdf # My resume
└── README.md # This file

yaml
Copy
Edit

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Kowshik-bh18/Kowshik_Portfolio.git
cd Kowshik_Portfolio
2. Set Up Virtual Environment
bash
Copy
Edit
# Create virtual environment
python -m venv venv

# Activate it
# For Windows
venv\Scripts\activate
# For macOS/Linux
source venv/bin/activate
3. Install Required Packages
bash
Copy
Edit
pip install -r requirements.txt
4. MongoDB Connection Setup
Update your Streamlit Cloud or local .streamlit/secrets.toml with your credentials:

toml
Copy
Edit
[MONGO_URI]
MONGO_URI = "mongodb+srv://kbh:kowshik123@cluster0.azn0yvf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
⚠️ Always keep your credentials safe and never expose them in public repos!

🧪 Run Locally
bash
Copy
Edit
streamlit run home.py
Then open http://localhost:8501 in your browser.

☁️ Deployment
This app can be easily deployed to Streamlit Cloud:

Push your code to a public GitHub repository.

Go to https://streamlit.io/cloud

Click Deploy an app and select your repo.

Add your MongoDB connection string to Secrets in the Streamlit Cloud settings.

🙋‍♂️ About Me
Hi, I'm Kowshik BH, a passionate Computer Science student at CMRIT Bengaluru, building modern and scalable applications with creative flair.

📧 Email Me

🔗 LinkedIn

🐙 GitHub

📃 License
This project is open-source and available under the MIT License.

⭐ Star the Repo
If you like this project, please consider giving it a ⭐ on GitHub. It motivates and supports me to create more awesome projects.

yaml
Copy
Edit

---

Let me know if you'd like badges, deployment status, demo GIFs, or contribution guidelines added as well!








