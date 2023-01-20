import openai
import streamlit as st
from streamlit_chat import message
# API KEY
# openai.api_key = "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"
# openai.api_key = "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"
openai.api_key = "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"

# GET RESPONSE
def openai_create(prompt):
    
    response = openai.Completion.create(
    # model="text-davinci-003",
    # model="davinci:ft-personal-2023-01-12-09-33-04",
    
    # model="davinci:ft-personal-2023-01-12-22-59-27",
    model="davinci:ft-personal-2023-01-19-06-42-18",
    prompt=prompt+"\n",
    # prompt=prompt+"\n\n###\n\n",
    temperature=0.3,
    max_tokens=2000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=1,
    stop=[" END"]
    # stop=[" Human:", " AI:"]
    )
    # print("======\n")
    print("Response ->"+response.choices[0].text)
    # 
    # print("======\n")
    return response.choices[0].text



def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return output, history

# Streamlit App
st.set_page_config(
    page_title="ChatBot - Demo",
    page_icon="::"
)
from PIL import Image
# image = Image.open('img/logo.png')
# st.sidebar.image(image, )
st.header("ChatGPT NTT Data Demo")

history_input = []


# create session - Initial run
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text 


user_input = get_text()


if user_input:
    output = chatgpt_clone(user_input, history_input)
    history_input.append([user_input, output])
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output[0])

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i),avatar_style="bottts")
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user',avatar_style="adventurer")