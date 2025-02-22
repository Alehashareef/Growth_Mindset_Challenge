import streamlit as st
import random
import datetime

st.title("🌱 GROWTH MINDSET CHALLENGE!")
st.subheader(" Never Stop Growing , Push Your Limits!🔥")
st.markdown("---")  

# Personalized Dashboard
st.sidebar.header("📌 Personalized Dashboard")
name = st.sidebar.text_input("Enter your name:")
if name:
    st.sidebar.write(f"Welcome back, {name}! Ready for today’s challenge?")
    st.sidebar.markdown("### Your Progress")
    progress = st.sidebar.slider("Your Growth Progress", 0, 100, 50)
    st.sidebar.write(f"You rated your growth as: {progress}%")
    streak = st.sidebar.number_input("Your Streak (Days)", min_value=0, step=1)
    st.sidebar.write(f"🔥 You're on a {streak}-day streak!")


# Daily Challenge Section
st.header("📅 Today's Challenge")
challenges = [
    "Write down three things you learned today.",
    "Try solving a difficult problem and analyze your mistakes.",
    "Teach someone a concept you recently learned.",
    "Step out of your comfort zone by trying something new.",
    "Read about someone who overcame failure to succeed."
]
today_challenge = random.choice(challenges)
st.info(today_challenge)

# User Reflection Box
challenge_response = st.text_area("✍️ Reflect on today's challenge:")
if st.button("Submit Reflection"):
    st.write("✅ Thank you for sharing! Keep growing!")

# Gratitude Section
st.header("🙏 Gratitude Journal")
gratitude_entry = st.text_area("Write one thing you are grateful for today:")
if st.button("Submit Gratitude"):
    st.write("🌟 Thank you for sharing your gratitude!")

# Motivational Quotes
quotes = [
    "Failure is simply the opportunity to begin again, this time more intelligently. – Henry Ford",
    "Success is not final, failure is not fatal: it is the courage to continue that counts. – Winston Churchill",
    "Your mindset determines your success!", 
    "Mistakes are proof that you are trying.",
    "Believe you can and you're halfway there. – Theodore Roosevelt",
    "It does not matter how slowly you go as long as you do not stop. – Confucius",
    "Do what you can, with what you have, where you are. – Theodore Roosevelt",
    "Difficulties in life are intended to make us better, not bitter. – Dan Reeves",
    "Opportunities don't happen. You create them. – Chris Grosser",
    "Act as if what you do makes a difference. It does. – William James",
    "Dream big and dare to fail. – Norman Vaughan",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. – Ralph Waldo Emerson",
    "The only way to do great work is to love what you do. – Steve Jobs",
    "You are never too old to set another goal or to dream a new dream. – C.S. Lewis"
]
st.header("💬 Motivational Quote")
st.success(random.choice(quotes))

# Learning Resources
st.header("📚 Learning Resources")
st.markdown("""
- [The Power of a Growth Mindset](https://www.mindsetworks.com/)
- [TED Talk: The Power of Believing You Can Improve](https://www.ted.com/talks/carol_dweck_the_power_of_believing_that_you_can_improve)
- [Growth Mindset Guide](https://www.edutopia.org/article/developing-growth-mindset)
""")

# Mini Quizzes
st.header("🧠 Mini Quiz")
questions = {
    "What is a Growth Mindset?": ["A fixed trait", "A belief in developing abilities", "A talent you're born with", "Something only geniuses have"],
    "What should you do when you make a mistake?": ["Ignore it", "Learn from it", "Give up", "Blame someone else"],
    "Which of these helps develop a growth mindset?": ["Avoiding challenges", "Embracing challenges", "Sticking to easy tasks", "Fearing failure"]
}
for question, options in questions.items():
    answer = st.radio (question, options)
    if st.button(f"Submit Answer:{question}"):
        if answer == options[1]:
            st.success("✅ Correct!")
        else:
            st.error("❌ Try again!")

# Audio Motivation
st.header("🎵 Boost Your Motivation")
audio_options = {
    "Inspiring Speech": "https://www.learningcontainer.com/wp-content/uploads/2020/02/Kalimba.mp3",
    "Powerful Motivation": "powerful motivation.mp3",
    "Success Mindset": "become-successful-299818.mp3"
}
selected_audio = st.selectbox("Choose a motivational audio:", list(audio_options.keys()))
if st.button("Play Audio"):
    st.audio(audio_options[selected_audio])

# Progress Chart
st.header("📊 Your Growth Over Time")
st.line_chart([random.randint(10, 100) for _ in range(10)])

st.markdown("---")  # Adds a separator line
st.markdown(" 🚀**Aleha Shareef** |  Keep Growing & Learning!")
