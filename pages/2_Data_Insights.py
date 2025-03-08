import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import InsightsQueries as iq

st.title('Data Insights')

option = st.selectbox( "Select Data Insights",
                        ("Average programming performance per course batch",
                         "Students ready for Placement",
                         "Soft Skill scores distribution",
                         "Students Placed Per Course Batch",
                         "Students with Soft Skills Score >= 75%",
                         "Students Per Graduation Year Per Course Batch",
                         "Top 3 Courses Enrolled by Students",
                         "Number of Students per Programming Language",
                         "Placement Ready Students with Maximum cleared Interview rounds",
                         "Top 10 Students with Communication Skill Score > 90"),
                        index= None
                     )


if option == "Average programming performance per course batch":
    
    data,col_names = iq.runQuery(iq.insight1)
    df = pd.DataFrame(data, columns=col_names)
    st.dataframe(df)
    
if option == "Students ready for Placement":

    data,col_names = iq.runQuery(iq.insight2)
    
    df = pd.DataFrame(data, columns=col_names)
    st.dataframe(df)

if option == "Soft Skill scores distribution":
    
    data,col_names = iq.runQuery(iq.insight3)
  
    df = pd.DataFrame(data, columns=col_names)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.title(f'Soft Skills Scores Distribution', fontsize=12)
    plt.xlabel("Soft Skills Scores", fontsize=10)
    plt.ylabel('Density')
    
    sns.histplot(df, kde=True, bins=10, ax=ax)
    st.pyplot(fig)
    
if option == "Students Placed Per Course Batch":

    data,col_names = iq.runQuery(iq.insight4)
   
    df = pd.DataFrame(data, columns=col_names)

    st.dataframe(df)

if option == "Students with Soft Skills Score >= 75%":

    data,col_names = iq.runQuery(iq.insight5)
   
    df = pd.DataFrame(data, columns=col_names)

    st.dataframe(df)

if option == "Students Per Graduation Year Per Course Batch":

    data,col_names = iq.runQuery(iq.insight6)
   
    df = pd.DataFrame(data, columns=col_names)

    df['graduation_year'] = df['graduation_year'].astype(str)
    
    st.dataframe(df)

if option == "Top 3 Courses Enrolled by Students":

    data,col_names = iq.runQuery(iq.insight7)
   
    df = pd.DataFrame(data, columns=col_names)
       
    st.dataframe(df)

if option == "Number of Students per Programming Language":
    
    data,col_names = iq.runQuery(iq.insight8)
    
    df = pd.DataFrame(data, columns=col_names)

    st.dataframe(df)

if option == "Placement Ready Students with Maximum cleared Interview rounds":

    data,col_names = iq.runQuery(iq.insight9)
   
    df = pd.DataFrame(data, columns=col_names)

    st.dataframe(df)

if option == "Top 10 Students with Communication Skill Score > 90":

    data,col_names = iq.runQuery(iq.insight10)

    df = pd.DataFrame(data, columns=col_names)

    st.dataframe(df)
