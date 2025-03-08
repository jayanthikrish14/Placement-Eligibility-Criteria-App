import streamlit as st
import pandas as pd
import PlacementElgibiltyQueries as pq

st.title('Placement Eligibility Criteria')

option = st.selectbox( "Select Placement Eligibility Criteria ",
                        ("Problems Solved", "Project Score",
                        "Mini Projects","Soft Skills Score"),
                        index= None
                     )


if option == "Problems Solved":

    text_input = st.text_input("Enter Number of Problems >=: ")

    if text_input:

        data,col_names = pq.runQuery(pq.Eligibility1,(text_input,))
       
        df = pd.DataFrame(data, columns=col_names)

        st.dataframe(df)

if option == "Project Score":

    text_input = st.text_input("Enter Project Score >=:")

    if text_input:
         
        data,col_names = pq.runQuery(pq.Eligibility2,(text_input,))
      
        df = pd.DataFrame(data, columns=col_names)

        st.dataframe(df)

if option == "Mini Projects":

    text_input = st.text_input("Enter Number of Mini Projects >=:")

    if text_input:
        
        data,col_names = pq.runQuery(pq.Eligibility3,(text_input,))
        
        df = pd.DataFrame(data, columns=col_names)

        st.dataframe(df)

if option == "Soft Skills Score":

    text_input = st.text_input("Enter Soft Skill Score >=:")

    if text_input:
        
        data,col_names = pq.runQuery(pq.Eligibility4,(text_input,))
      
        df = pd.DataFrame(data, columns=col_names)

        st.dataframe(df)        
