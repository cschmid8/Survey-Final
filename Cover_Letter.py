import streamlit as st
from openai import OpenAI
import os

# Setting up OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

#  Streamlit App
st.set_page_config(
    page_title="OpenAI Cover Letter Assistant",
    page_icon="📝",
    layout="wide",
)

st.markdown(
    """
    <style>
    .main-title {
        font-size: 36px;
        color: #4CAF50;
        text-align: center;
        margin-top: -50px;
    }
    .sub-title {
        font-size: 20px;
        color: #555;
        text-align: center;
    }
    .sidebar-title {
        font-size: 18px;
        font-weight: bold;
        color: #4CAF50;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<h1 class="main-title">📝 OpenAI Cover Letter Assistant</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Generate a personalized cover letter effortlessly.</p>', unsafe_allow_html=True)

# Sidebar for inputs
st.sidebar.markdown('<h2 class="sidebar-title">Input Details</h2>', unsafe_allow_html=True)
Major = st.sidebar.text_input('🎓 Enter Major:', 'Business Analytics')
Position = st.sidebar.text_input('💼 Enter Job Position:', 'Data Analyst')
Level = st.sidebar.selectbox(
    '📈 Select Job Level:', 
    ['Entry', 'Intermediate', 'Advanced', 'Executive']
)
Company_Title = st.sidebar.text_input('🏢 Company Name:', 'Google')
Skills = st.sidebar.text_input('🛠️ Job Requirements:', 'Python')
Skills2 = st.sidebar.text_input('💡 Personal Skills:', 'Hardworking, Driven')
Job_Description = st.sidebar.text_area(
    '📜 Copy/Paste Job Description:', 
    'Create an Open AI with Python'
)

# Generate Cover Letter Button
if st.sidebar.button('✨ Generate Cover Letter'):
    with st.spinner('Generating your cover letter...'):
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a Cover Letter Assistant."},
                {
                    "role": "user",
                    "content": f"Write a cover letter based on the student's major: {Major}, Job Position {Position}, and level of position {Level}. Take into account the company name: {Company_Title}, the necessary job skills: {Skills}, an individual's soft skills {Skills2}, and the Job Description {Job_Description} to optimize this task."
                }
            ]
        )
        cover_letter = completion.choices[0].message.content
        st.markdown(
            f"""
            <div style="background-color: #f9f9f9; padding: 20px; border-radius: 5px;">
                <h3 style="color: #4CAF50;">Your Cover Letter:</h3>
                <p style="white-space: pre-wrap; font-family: 'Courier New', Courier, monospace;">{cover_letter}</p>
            </div>
            """, 
            unsafe_allow_html=True
        )

# Feedback Section
st.markdown('---')
st.markdown('<h2 class="sidebar-title">Feedback</h2>', unsafe_allow_html=True)
feedback = st.text_area("🔧 Not Satisfied? Help us improve:")
rating = st.slider("Rate your experience:", 1, 5, 3)
if st.button("Submit Feedback"):
    st.success("Thank you for your feedback!")

# Check it out: https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps#build-a-chatgpt-like-app
#bacon rocks
# yes it does
