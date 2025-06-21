import streamlit as st
from pymongo import MongoClient
import os
import plotly.graph_objects as go

# --- Page Config ---
st.set_page_config(page_title="Contact", page_icon="📬")
st.title("📬 Get in Touch")
st.markdown("#### 💬 Have a question, feedback, or collaboration idea? Drop me a message!")

# --- MongoDB Setup ---
try:
    cluster = MongoClient(os.getenv("MONGO_URI"))
    db = cluster["portfolio"]
except Exception as conn_err:
    st.error("⚠️ Could not connect to MongoDB.")
    st.stop()

# --- Contact Form ---
with st.container():
    col1, col2 = st.columns([1, 2])

    with col2:
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("👤 Your Name")
            email = st.text_input("📧 Your Email")
            message = st.text_area("✍️ Your Message")

            submitted = st.form_submit_button("🚀 Send Message")

            if submitted:
                if name and email and message:
                    try:
                        db["messages"].insert_one({
                            "name": name,
                            "email": email,
                            "message": message
                        })
                        st.success("✅ Message sent successfully!")
                        st.balloons()
                    except Exception as e:
                        st.error(f"❌ Could not send message.\n{e}")
                else:
                    st.warning("⚠️ Please fill in all fields.")

# --- Visitor Counter ---
st.markdown("---")
st.markdown("## 📈 Contact Page Traffic")

try:
    counter = db["visits"].find_one({"_id": "contact_page"})
    if counter:
        db["visits"].update_one({"_id": "contact_page"}, {"$inc": {"count": 1}})
        views = counter["count"] + 1
    else:
        db["visits"].insert_one({"_id": "contact_page", "count": 1})
        views = 1

    fig = go.Figure(go.Indicator(
        mode="number+delta",
        value=views,
        number={"suffix": " views"},
        title={"text": "Total Visits"},
        delta={"reference": views - 1, "increasing": {"color": "green"}}
    ))
    fig.update_layout(height=250)
    st.plotly_chart(fig, use_container_width=True)

except:
    st.caption("👁️ Visit tracking unavailable.")

# --- Feedback Section ---
st.markdown("---")
st.markdown("## 💬 Do you like this page?")

like_col1, like_col2 = st.columns([1, 4])
with like_col1:
    feedback = st.radio("Your Feedback", ["👍 Yes", "👎 No", "🤔 Maybe"], horizontal=True)
with like_col2:
    comments = st.text_input("Optional comment:")

if st.button("Submit Feedback"):
    try:
        db["feedback"].insert_one({
            "page": "contact",
            "response": feedback,
            "comment": comments
        })
        st.success("✅ Thank you for your feedback!")
    except Exception as e:
        st.error(f"⚠️ Could not record feedback.\n{e}")

# --- Social Media Links ---
st.markdown("---")
st.markdown("### 🔗 Connect with Me")
social_cols = st.columns(4)

with social_cols[0]:
    st.markdown("[![GitHub](https://img.icons8.com/ios-glyphs/30/github.png)](https://github.com/Kowshik-bh18)")
with social_cols[1]:
    st.markdown("[![LinkedIn](https://img.icons8.com/ios-filled/30/linkedin.png)](https://www.linkedin.com/in/kowshik-bh-0b750b309/)")
with social_cols[2]:
    st.markdown("[![Email](https://img.icons8.com/ios-filled/30/email.png)](mailto:kobh22cs@cmrit.ac.in)")
with social_cols[3]:
    st.markdown("[![Phone](https://img.icons8.com/ios-filled/30/phone.png)](tel:+917483226281)")

# --- Final Footer ---
st.markdown("---")
footer = """
<div style='text-align: center; padding: 10px 0; font-size: 15px; color: #888;'>
    <p>© 2025 Kowshik BH | Made with ❤️ using <strong>Python & Streamlit</strong></p>
    <p>Theme mode: Light ☀️ / Dark 🌙 (based on system preference)</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)
