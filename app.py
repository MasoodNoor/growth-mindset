import streamlit as st

st.set_page_config(page_title="Growth Mindset App", page_icon=":seedling:")

st.title("Growth Mindset App :wave:")

st.header(":rocket: Welcome to **Your Growth Journey**")
st.write("Growth Mindset AI is a powerful web app built with Streamlit that helps you cultivate a growth-oriented mindset through AI-driven insights and personalized guidance. Whether you're a student, professional, or lifelong learner.")

#qoute sections
st.header(":mega: Today's Growth Mindset Quote")
st.write('"Successful people aren&#39;t built different, they&#39;re just consistent"')

st.header(":muscle: What's Your Challenge Today?")
user_input = st.text_input("What's your challenge today?", "I'm struggling with")

#condition
if user_input:
    st.success(f"Great! Let's tackle this challenge together. Here's a personalized growth plan to help you overcome **{user_input}:**")
else:
    st.wraning ("Let's start by identifying your challenge today.")

#reflexing 
st.header(":bulb: Reflecting on Your Growth Journey")
reflections = st.text_area("What's one thing you've learned today?")

if reflections:
    st.success(f":thumbsup: Thank you for sharing your reflections! Here's a personalized growth plan :bookmark_tabs: to help you stay motivated and focused on your goals **: {reflections} :**")
else:
    st.info(f":thumbsup: Thank you for sharing your reflections!")

#achievements

st.header(":trophy: Celebrating Your Achievements")
achievements = st.text_input("What's one thing you've achieved today?")

if achievements:
    st.success(f":tada: Congratulations on your achievement! **: {achievements} :**")
else:
    st.info(f":tada: Congratulations on your achievement!")


#footer
st.write("- - -")
st.write("Hard work is worthless for those who don't believe in themselves")
st.write(":computer: Created by Masood Noor.")