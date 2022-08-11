from bokeh.plotting import figure
import numpy as np
import pandas as pd
import streamlit as st
import sqlite3
import pdfkit


con = sqlite3.connect('testing_1.db')


cur = con.cursor()

# last_row_1 = cur.execute('select * from roi').fetchall()[-1]
if "last_row_1" in st.session_state:
    st.session_state["last_row_1"]
    print(st.session_state["last_row_1"][0],"dawdawd")
    con.commit()
    intAnnualAccruedROI=0
    intTotalProcess=st.session_state["last_row_1"][0]
    intTotalEmployee=st.session_state["last_row_1"][1]
    intTotalTime=st.session_state["last_row_1"][2]/100
    intSalary=st.session_state["last_row_1"][3]
    intCostBot=st.session_state["last_row_1"][4]
    intMaintainanceCost=st.session_state["last_row_1"][5]
    ListCurrentCostFTE=[]
    ListHoursWeek =[]
    ListCostWeek=[]

    ListToatlBotCost=[]
    listNetROI=[]
    listAnnualAccruedROI=[]
    listBotCost=[]
    intCurrentCostFTE=intTotalEmployee*intSalary*intTotalTime
    intHoursWeek=40*intTotalEmployee*intTotalTime
    intCostWeek=(intTotalEmployee*intTotalTime*intSalary)/52
    intToatlBotCost=intCostBot*intTotalProcess
    intNetROI=intCurrentCostFTE-intToatlBotCost
    try:
        intAnnualAccruedROI=(intNetROI/intToatlBotCost)*100
    except ZeroDivisionError:
        pass

    ListToatlBotCost.append(intToatlBotCost)
    ListCurrentCostFTE.append(intCurrentCostFTE)
    ListHoursWeek.append(intHoursWeek)
    ListCostWeek.append(intCostWeek)
    listBotCost.append(intToatlBotCost)
    listNetROI.append(intNetROI)
    listAnnualAccruedROI.append(intAnnualAccruedROI)


    for i in range(4):
        intCurrentCostFTE=intCurrentCostFTE
        intHoursWeek=intHoursWeek
        intCostWeek=intCostWeek
        intToatlBotCost=intMaintainanceCost

        intNetROI=intCurrentCostFTE-intToatlBotCost
            
        listBotCost.append(intToatlBotCost)
        listNetROI.append(intNetROI)
        ListCurrentCostFTE.append(intCurrentCostFTE)
        ListHoursWeek.append(intHoursWeek)
        ListCostWeek.append(intCostWeek)
        ListToatlBotCost.append(intToatlBotCost)



        ROISUM=sum(listNetROI)
        ROISUM2=sum(listBotCost)
        try:
            intAnnualAccruedROI=(ROISUM/ROISUM2)*100
        except ZeroDivisionError:
            pass
        listAnnualAccruedROI.append(intAnnualAccruedROI)

    print(listNetROI,listAnnualAccruedROI)
    left_ind=[]

    for i in range(5):
        a="Year "+str(i+1)
        left_ind.append(a)
            # st.subheader(f"Year {(i+1)} - Net ROI is ${listNetROI[i]} - Net Accrued ROI is {round(listAnnualAccruedROI[i],2)}%, ---- {intCostWeek}")

    # with st.expander("Check ROI Result"):
    li_yr=['Year 1','Year 2','Year 3','Year 4','Year 5',]
    df = pd.DataFrame(list(zip(li_yr,ListCurrentCostFTE, ListHoursWeek, ListCostWeek, ListToatlBotCost,listNetROI, listAnnualAccruedROI)),
                        columns =['Year','Current Costs for FTEs', 'Hours Per week for FTEs', 'Cost per Week for FTEs','Total Annual Cost','Net ROI', 'Annual Accrued ROI'])
    st.table(df)

    part11, part22 = st.columns(2)
    with part11:
        # x = [1,2,3,4,5]
        # y = [462.5, 4225.0, 4387.5, 4550.0, 4712.5]
        x = [1, 2, 3, 4, 5]
        y = listAnnualAccruedROI
        p = figure(
            title='Annual Accrued ROI',
            x_axis_label='Year',
            y_axis_label='ROI %')

        p.line(x, y, legend_label='Trend', line_width=2)

        st.bokeh_chart(p, use_container_width=True)

        # st.table(df)
    with part22:
        x1 = [1, 2, 3, 4, 5]
        y1 = listNetROI
        # x1 = [1,2,3,4,5]
        # y1 = [462.5, 4225.0, 4387.5, 4550.0, 4712.5]
        p = figure(
            title='Net ROI ',
            x_axis_label='Year',
            y_axis_label='list Net ROI')

        p.line(x1, y1, legend_label='Trend', line_width=2)

        st.bokeh_chart(p, use_container_width=True)




if "last_row" in st.session_state:
    st.session_state["last_row"]
# last_row = cur.execute('select * from fesDb').fetchall()[-1]
    if st.session_state["last_row"][0]==1:
        access=True
    else:
        access=False
    if access:
        if st.session_state["last_row"][1]=="0-15%":
            val_1=5
        elif st.session_state["last_row"][1]=="16-30%":
            val_1=5
        elif st.session_state["last_row"][1]=="31-50%":
            val_1=3
        elif st.session_state["last_row"][1]=="51-80%":
            val_1=1
        else:
            val_1=1
    else:
        if st.session_state["last_row"][1]=="0-15%":
            val_1=5
        elif st.session_state["last_row"][1]=="16-30%":
            val_1=4
        elif st.session_state["last_row"][1]=="31-50%":
            val_1=1
        elif st.session_state["last_row"][1]=="51-80%":
            val_1=1
        else:
            val_1=1
        
    if st.session_state["last_row"][2]=="0-15%":
        val_2=1
    elif st.session_state["last_row"][2]=="16-30%":
        val_2=2
    elif st.session_state["last_row"][2]=="31-50%":
        val_2=3
    elif st.session_state["last_row"][2]=="51-80%":
        val_2=4
    else:
        val_2=5
        
    if st.session_state["last_row"][3]=="0-15%":
        val_3=5
    elif st.session_state["last_row"][3]=="16-30%":
        val_3=5
    elif st.session_state["last_row"][3]=="31-50%":
        val_3=4
    elif st.session_state["last_row"][3]=="51-80%":
        val_3=1
    else:
        val_3=1



    print(val_1)


    if st.session_state["last_row"][4]==1:
        access=True
    else:
        access=False
    if access:
        if st.session_state["last_row"][5]=="Very Rare":
            val_4=5
        elif st.session_state["last_row"][5]=="Yearly":
            val_4=5
        elif st.session_state["last_row"][5]=="Quarterly":
            val_4=3
        elif st.session_state["last_row"][5]=="Monthly":
            val_4=1
        else:
            val_4=1
    else:
        if st.session_state["last_row"][5]=="Very Rare":
            val_4=1
        elif st.session_state["last_row"][5]=="Yearly":
            val_4=1
        elif st.session_state["last_row"][5]=="Quarterly":
            val_4=1
        elif st.session_state["last_row"][5]=="Monthly":
            val_4=1
        else:
            val_4=1


    if st.session_state["last_row"][6]=="Yes":
        input_judmental=True
    else:
        input_judmental=False
    if input_judmental==True:
        val_6=1
    else:
        val_6=5

    if st.session_state["last_row"][7]=="0-15%":
        val_7=5
    elif st.session_state["last_row"][7]=="16-30%":
        val_7=4
    elif st.session_state["last_row"][7]=="31-50%":
        val_7=3
    elif st.session_state["last_row"][7]=="51-80%":
        val_7=2
    else:
        val_7=1
        
    if st.session_state["last_row"][8]==1:
        input_citrix=True
    else:
        input_citrix=False

    if st.session_state["last_row"][9]==1:
        input_citrix_1=True
    else:
        input_citrix_1=False

    if st.session_state["last_row"][10]==1:
        input_citrix_2=True
    else:
        input_citrix_2=False


    if input_citrix==True and input_citrix_1==True and input_citrix_2 ==False:
        val_5=5
    elif input_citrix==True and input_citrix_1==False and input_citrix_2 ==False:
        val_5=1
    elif input_citrix==True and input_citrix_1==False and input_citrix_2 ==True:
        val_5=3
    else:
        val_5=5
        
    total_sum=val_1+val_2+val_3+val_4+val_5+val_6+val_7
    print(total_sum)

        # st.balloons()
        # st.snow()
        # st.write(total_sum)
    if total_sum>=29 and total_sum<=35:
        ca="Good for automation - High - Score "+str(total_sum)
    elif total_sum>=15 and total_sum<=28:
        print(total_sum)
        ca="Automation is possible but with some challenges - Medium - Score "+str(total_sum)
    elif total_sum>=0 and total_sum<=14:
        ca="It is not a good candidate for Automation -  Low - Score "+str(total_sum)
    st.markdown("""---""")
    # with st.expander("Check Feasibility Result"):
        # st.write("updating soon")
    # st.metric(label="Feasiblity Matrix", value=ca)
    st.text(ca)
    # pdfkit.from_url('http://localhost:8501/Dashboard_Result', 'out1.pdf')
