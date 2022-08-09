import streamlit as st
import inspect
import textwrap
import time
import numpy as np

import pandas as pd
# from utils import show_code

import sqlite3


con = sqlite3.connect('testing_1.db')


cur = con.cursor()


# def TestMe():
#     print("press")
def roi_demo():
    part1, part2 = st.columns(2)
    with st.form("my_form"):
        with part1:
            intTotalProcess = st.number_input("Number of business process the RPA Bot will automate : ", min_value=0, format='%d')
            intTotalEmployee = st.number_input("How many FTEs currently work on the task(s) : ", min_value=0, format='%d')
            intTotalTime = st.number_input("What % of the FTE(s) daily time is spent on this task : ",min_value=0,format='%d')

        with part2:
            intSalary = st.number_input("What is the average fully loaded salary of the FTE(s) : ",min_value=0,format='%d')
            intCostBot = st.number_input("Est. Cost Per Bot implementation : ",min_value=0,format='%d')
            intMaintainanceCost = st.number_input("Estimated cost for the Maintenanceeeeee of each bot : ",min_value=0,format='%d')
        
        submitted = st.form_submit_button("Submit")
        if submitted:
            last_row_1=[intTotalProcess,intTotalEmployee,intTotalTime,intSalary,intCostBot,intMaintainanceCost]
            # cur.execute('''CREATE TABLE roi (intTotalProcess real, intTotalEmployee real, intTotalTime real, intSalary real, intCostBot real,intMaintainanceCost real)''')
            st.success('Data Submitted for processing')
            st.write("Check  your result at dashboard page")
            cur.execute("INSERT INTO roi VALUES (?,?,?,?,?,?)",(intTotalProcess,intTotalEmployee,intTotalTime,intSalary,intCostBot,intMaintainanceCost))
            st.session_state['last_row_1']=last_row_1
    # for row in cur.execute('SELECT * FROM roi'):
    #     print(row)
            con.commit()
            # print(len(str(intTotalProcess)))

    # st.button("Submit",on_click=TestMe())



st.set_page_config(page_title="ROI Calculator", page_icon="")

with open('pages\\style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
st.markdown("# ROI Calculator")
st.markdown("""---""")
# st.sidebar.header("Plotting Demo")
# st.write(
#     """This demo illustrates a combination of plotting and animation with
# Streamlit. We're generating a bunch of random numbers in a loop for around
# 5 seconds. Enjoy!"""
# )

roi_demo()
