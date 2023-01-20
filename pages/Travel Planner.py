import openai
from PIL import Image
import streamlit as st
from streamlit_chat import message
import time
# API KEY
openai.api_key = "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"


# GET RESPONSE
def openai_create(prompt):
    with st.spinner('We are planning the best possible trip for you ...'):
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

# image = Image.open('img/logo.png')
# st.sidebar.image(image, )
st.markdown("# Travel Planner using GPT3 :world_map: 	:airplane_departure:")


mainOutput=""
# resultOutput2=""
# resultOutput3=""
visitOutput=""
stayOutput=""
activityOutput=""
foodOutput=""
localAttractionOutput=""
col1, col2 = st.columns(2)
with col1:
    startDestination = st.text_input('From where would you like to start your journey?')
with col2:
    endDestination = st.text_input('Where would you like to go?')
days = st.slider("How many days?", min_value=1, max_value=30, value=1,format="%d")
# purpose = st.text_input('What\'s your purpose of visit? (Optional)',placeholder="Education / Vacation")

col1_1, col2_1,col3_1 = st.columns(3)
if startDestination and endDestination:
    with col2_1:
        if st.button("Generate Plan"):
            print(startDestination,endDestination,str(days))
            resultOutput=""
            textHeader=""
            # mainPrompt="create a detailed travel itinerary  from "+startDestination+" to "+endDestination+" for "+str(int(days))+" days with timestamp in list format?"
            mainPrompt="create a list of detailed travel itinerary  to "+endDestination+" for "+str(int(days))+" days with timestamp"
            # prompt="create a detailed travel itinerary  from "+startDestination+" to "+endDestination+" for "+str(int(days))+" days with place to stay and eat with timestamp and return in list format"
            # if len(purpose)>2:
            #     mainPrompt+=" for "+purpose+" purpose"
            print(mainPrompt)
            visitPrompt="Whats the best time to visit "+endDestination.capitalize()+"?"
            stayPrompt="Recommend 5 places to stay, along with address at"+endDestination.capitalize()+"?"
            activityPrompt="What are the activities and experiences to lookout for at "+endDestination.capitalize()+"?"
            foodPrompt="What are the local cusines, resturants, bars, eateries, cafes to visit in "+endDestination.capitalize()+" in list format?"
            localAttractionPrompt="What are the local attractions and historic places at "+endDestination.capitalize()+" in list format?"
            visitOutput=openai_create(visitPrompt)
            stayOutput=openai_create(stayPrompt)
            activityOutput=openai_create(activityPrompt)
            foodOutput=openai_create(foodPrompt)
            mainOutput=openai_create(mainPrompt)
            localAttractionOutput=openai_create(localAttractionPrompt)
            # resultOutput2=openai_create(prompt)
            # resultOutput3=openai_create(prompt)
            # print(resultOutput1)
            
col1_2, col2_2,col_3_2 = st.columns(3)
# if resultOutput1!="" and visitOutput!="" and resultOutput2!="" and resultOutput3!="":
if mainOutput!="" and visitOutput!="" and stayOutput!="" and activityOutput!="" and foodOutput!="" and localAttractionOutput!="":
    # time.sleep(50)
    bestVistHeader=" Best time to visit "
    activityHeader=" Activities and experiences to look out for "
    stayHeader=" Top stay recommendations"
    foodHeader=" Check out the food scene at"
    localAttractionHeader=" Some of the local attractions"
    mainHeader=" Here\'s your detailed "+str(int(days))+" day itinerary  from "+startDestination.capitalize()+" to "+endDestination.capitalize()       
    # textHeader2="Option 2 :Here\'s your detailed "+str(int(days))+" day itinerary  from "+startDestination.capitalize()+" to "+endDestination.capitalize()       
    # textHeader3="Option 3 :Here\'s your detailed "+str(int(days))+" day itinerary  from "+startDestination.capitalize()+" to "+endDestination.capitalize()       
    st.markdown("""---""")
    st.subheader(":partly_sunny_rain:"+bestVistHeader)
    st.markdown(visitOutput)
    st.markdown("""---""")
    st.subheader(":pushpin:"+mainHeader)
    st.markdown(mainOutput)
    st.markdown("""---""")
    st.subheader(":house_with_garden:"+stayHeader)
    st.markdown(stayOutput)
    st.markdown("""---""")
    st.subheader(":taco:"+foodHeader)
    st.markdown(foodOutput)
    st.markdown("""---""")
    st.subheader(":shinto_shrine:"+localAttractionHeader)
    st.markdown(localAttractionOutput)
    st.markdown("""---""")
    st.subheader("	:skier:"+activityHeader) 
    st.markdown(activityOutput)



    

# TO-DOs
# 1 icons
# 2 Mail
# 3 Language
# 4 image


















    # with col1_2:
    #     st.subheader(textHeader1)
    #     st.markdown(resultOutput1)
    # with col2_2:
    #     st.subheader(textHeader2)
    #     st.markdown(resultOutput2)
    # with col_3_2:
    #     st.subheader(textHeader3)
    #     st.markdown(resultOutput3)
