import streamlit as st
import random

st.set_page_config(
    page_title="Growth Mindset App",
    page_icon="🚀",
    layout="wide"
)

st.markdown("""
<style>
    [data-testid="stAppViewContainer"] {
        background: #f0f2f6;
    }
    .title {
        color: #2ecc71;
        text-align: center;
        font-size: 3em;
        margin: 20px 0;
    }
    .section {
        background: white;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        border-left: 5px solid #2ecc71;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='title'>Growth Mindset App created by Mudasir Ali</h1>", unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <h2>What is Growth Mindset?</h2>
    <p>A growth mindset is the belief that your abilities and intelligence can be developed through dedication, hard work, and learning from your mistakes. This view fosters a love for learning and resilience essential for achieving great accomplishments.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <h2>Why Adopt a Growth Mindset?</h2>
    <ul>
        <li><strong>Embrace Challenges:</strong> View obstacles as opportunities to learn.</li>
        <li><strong>Learn from Mistakes:</strong> Mistakes are natural steps in the learning process.</li>
        <li><strong>Persist Through Difficulties:</strong> Persistence leads to growth and success.</li>
        <li><strong>Celebrate Effort:</strong> Value the effort you put into learning over just the final outcome.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section">
    <h2>Reflect on Your Journey</h2>
    <p>What challenges have you overcome recently? How did you grow from those experiences?</p>
</div>
""", unsafe_allow_html=True)

reflection = st.text_area("Your Reflection", height=150)

if st.button("Submit Reflection"):
    if reflection.strip():
        st.success("Great reflection! Keep embracing challenges and growing.")
    else:
        st.error("Please share your thoughts in the reflection box.")

st.markdown("""
<div class="section">
    <h2>Set Your Learning Goals</h2>
    <p>What skills or knowledge do you aim to develop? Outline your learning goals for the near future.</p>
</div>
""", unsafe_allow_html=True)

learning_goals = st.text_area("Your Learning Goals", height=150)

if st.button("Submit Learning Goals"):
    if learning_goals.strip():
        st.success("Excellent! Setting clear learning goals is a key step in your growth journey.")
    else:
        st.error("Please enter your learning goals.")

quotes = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "The journey of a thousand miles begins with one step. – Lao Tzu"
]
selected_quote = random.choice(quotes)

st.markdown(f"""
<div class="section">
    <h2>Motivational Quote of the Day</h2>
    <p style="font-size: 1.2em;">{selected_quote}</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<p style='text-align: center;'>Keep growing and stay motivated!</p>", unsafe_allow_html=True)
