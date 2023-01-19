import openai
from PIL import Image
import streamlit as st
from streamlit_chat import message

# API KEY
openai.api_key = "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"


# GET RESPONSE
def openai_create(prompt):
    with st.spinner('We are planning the best possible thing for you ...'):
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=1,
        stop=[" Human:", " AI:"]
        )
    print("Response ->"+response.choices[0].text)
    return response.choices[0].text

# Streamlit App

image = Image.open('img/logo.png')
st.sidebar.image(image, )
st.header("Travel Planner with ChatGPT")


resultOutput=""
col1, col2 = st.columns(2)
with col1:
    startDestination = st.text_input('From where would you like to start your journey?')
with col2:
    endDestination = st.text_input('Where would you like to go?')
days = st.slider("How many days?", min_value=1, max_value=30, value=1,format="%d")
purpose = st.text_input('What\'s your purpose of visit? (Optional)',placeholder="Education / Vacation")

col1_1, col2_1,col3_1 = st.columns(3)
if startDestination and endDestination:
    with col2_1:
        if st.button("Generate Plan"):
            print(startDestination,endDestination,str(days))
            resultOutput=""
            textHeader=""
            prompt="create a detailed travel itinerary  from "+startDestination+" to "+endDestination+" for "+str(int(days))+" days with timestamp and return list"
            if len(purpose)>2:
                prompt+=" for "+purpose+" purpose"
            print(prompt)
            resultOutput=openai_create(prompt)

if resultOutput!="":
    textHeader="Here\'s your detailed "+str(int(days))+" day itinerary  from "+startDestination.capitalize()+" to "+endDestination.capitalize()       
    st.markdown("""---""")
    st.subheader(textHeader)
    st.markdown(resultOutput)