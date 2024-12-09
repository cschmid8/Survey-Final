


import streamlit as st
from openai import OpenAI
import os

# Setting up OpenAI



# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

client = OpenAI()

# Streamlit App

st.title('OpenAI Cover Letter Assistant')

st.write('This app will take information you input and generate a cover letter.')

# We will start with a side bar to ask the user for a genre

Major = st.sidebar.text_input('Enter an Major:', 'Business')

# We will then ask the user for an artist

Position = st.sidebar.text_input('Enter an Job Position:', 'CEO')

# Now we need a place to display the lyrics

Level = st.sidebar.selectbox(
    'Select a Job Level:', 
    ['Entry','Intermediate','Advanced','Executive']
)

Cover_Letter = st.empty()

Company_Title = st.sidebar.text_input('Company Title', 'United Health')
Skills = st.sidebar.text_input('Job Requirements', 'Bullet-proof')
Skills2 = st.sidebar.text_input('Relevant Personal Skills', 'Kind and chill')
Job_Description = st.sidebar.text_input('Copy/Paste Job Description', 'You will work for 2000 hours per week for 3 dollars per hour')
# Now we need a button to generate the Cover Letter


if st.sidebar.button('Generate Cover Letter'):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a Cover Letter Assistant."},
            {
                "role": "user",
                "content": f"Write a cover letter based on the student's major: {Major}, Job Position {Position}, and level of position {Level}. Take in to account the company name: {Company_Title}, the necessary job skills: {Skills}, an individual's soft skills {Skills2}, and the Job Description {Job_Description} to optimize this task."
                }
        ]
    )
    Cover_Letter.write(completion.choices[0].message.content)

feedback = st.text_area("Not Satisfactory? Help us Learn More")
if st.button("Submit Feedback"):
    st.success("Thank you for your feedback!")

# Check it out: https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps#build-a-chatgpt-like-app
#bacon rocks
