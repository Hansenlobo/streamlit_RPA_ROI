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
        # prompt="Plan a detailed, descriptive, and elaborate five-day travel itinerary to Bavaria for a family of four with children. Include places to visit, places to stay, local cuisine, restaurants, activities, experiences, types of clothes to be taken, weather conditions, the best mode of travel, and timestamps.",
        temperature=0.45,
        max_tokens=2000,
        top_p=1,
        frequency_penalty=2,
        presence_penalty=0,
        stop=[" Human:", " AI:"]
        # stop=["END"]
        )
    # print("======\n")
    print("Response ->"+response.choices[0].text)
    # print("======\n")
    return response.choices[0].text

# Streamlit App

image = Image.open('img/logo.png')
st.sidebar.image(image, )
st.markdown("# Travel Planner with GPT3 :earth_asia:")


resultOutput=""
col1, col2 = st.columns(2)
with col1:
    startDestination = st.text_input('From where would you like to start your journey?')
with col2:
    endDestination = st.text_input('Where would you like to go?')
# days = st.number_input('How many days?',format="%d")
days = st.slider("How many days?", min_value=1, max_value=30, value=1,format="%d")
# purpose = st.text_input('What\'s your purpose of visit? (Optional)',placeholder="Education / Vacation")
goingOption = st.selectbox(
    'Who will you be going with?',
    ('Solo Trip', 'A group of friends', 'Family along with kids'))
# print(goingOption)

col1_1, col2_1,col3_1 = st.columns(3)
if startDestination and endDestination:
    with col2_1:
        if st.button("Generate Plan"):
            print(startDestination,endDestination,str(days))
            resultOutput=""
            textHeader=""
            prompt="Plan a detailed, descriptive, and elaborate "+str(int(days))+" -day travel itinerary from "+startDestination+" to "+endDestination+" for "+goingOption+". Include places to visit, places to stay, local cuisine, restaurants, activities, experiences, types of clothes to be taken, weather conditions, the best mode with timestamps."
            print(prompt)
            resultOutput=openai_create(prompt)

if resultOutput!="":
    textHeader="Here\'s your detailed "+str(int(days))+" day itinerary  from "+startDestination.capitalize()+" to "+endDestination.capitalize()    
    st.markdown("""---""")
    st.subheader(textHeader)
    st.markdown(resultOutput)
    print(repr(resultOutput))
    haha=repr(resultOutput)
    with open("example.txt", "w") as file:
    # Write the string to the file
        file.write(haha)
