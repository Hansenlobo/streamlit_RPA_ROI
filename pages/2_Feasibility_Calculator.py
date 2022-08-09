import streamlit as st
import sqlite3


con = sqlite3.connect('testing_1.db')


cur = con.cursor()

def fes_demo():
    with st.form("my_form"):
        with st.expander("Process Input"):
            input_percentage_scanned = st.selectbox(
            'What percentage of your input is in scanned format? ',
            ('0-15%', '16-30%','31-50%','51-80%','81-100%',))

            access_input = st.selectbox(
            'Do you have access to the scanned data in electronic format? ',
            ('Yes', 'No',))

            input_copy = st.selectbox(
            'What percentage of your input is electronic format which allows Ctrl C and Ctrl V? ',
            ('0-15%', '16-30%','31-50%','51-80%','81-100%',))

            input_unstructure = st.selectbox(
            'What percentage of your input is unstructered i.e. free flow text? ',
            ('0-15%', '16-30%','31-50%','51-80%','81-100%',))

            std_template = st.selectbox(
            'In case of structured data do we have standard Template/layout? ',
            ('Yes', 'No',))
            input_updates = st.selectbox(
            'Are there frequent updates in template?',
            ('Very Rare', 'Yearly','Quarterly','Monthly','Weekly',))

        with st.expander("Technical Feasibility"):
            input_citrix = st.selectbox(
            'Does Process involve working in Citirix? ',
            ('Yes', 'No',))

            input_citrix_1 = st.selectbox(
            'Can you do Ctrl+C  of the data field you want to read and do Ctrl+V on the application you want to move the data?',
            ('Yes', 'No',))

            input_citrix_2 = st.selectbox(
            'Can the data be extracted from any other system? ',
            ('Yes', 'No',))

            input_judmental_decision = st.selectbox(
            'Does the process include judgemental decision making, considering multiple criteria? ',
            ('Yes', 'No',))

            input_volumne_dependency = st.selectbox(
            'What Percentage of Volume has dependency on clarification from customer through calls/emails? ',
            ('Select','0-15%', '16-30%','31-50%','51-80%','81-100%',))
        submitted = st.form_submit_button("Submit Data")
        if submitted:
            last_row=[access_input,input_percentage_scanned,input_copy,input_unstructure,std_template,input_updates,input_judmental_decision,input_volumne_dependency,input_citrix,input_citrix_1,input_citrix_2]
            # cur.execute('''CREATE TABLE fesDb (access_input INTEGER, input_percentage_scanned TEXT, input_copy TEXT, input_unstructure TEXT, std_template INTEGER,input_updates TEXT,input_judmental_decision INTEGER,input_volumne_dependency TEXT,input_citrix INTEGER,input_citrix_1 INTEGER,input_citrix_2 INTEGER)''')
            st.success('Data Submitted for processing Fes')
            st.write("Check  your result at dashboard page")
            cur.execute("INSERT INTO fesDb VALUES (?,?,?,?,?,?,?,?,?,?,?)",(access_input,input_percentage_scanned,input_copy,input_unstructure,std_template,input_updates,input_judmental_decision,input_volumne_dependency,input_citrix,input_citrix_1,input_citrix_2))
            con.commit()
            st.session_state['last_row']=last_row

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

fes_demo()