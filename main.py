import pandas
import streamlit as st

col1, col2= st.columns(2)

with col1:
    st.image("Images\Pic.jpg")

with col2:
    st.title("Saumya Agarwal")
    content = """
    Hi, I am Saumya Agarwal. I am pursuing my B.Tech degree in Computer
    Science Engineering with a specialisation in AI and Robotics from Vellore 
    Institute of Technology, Chennai. I am very passionate about coding and 
    software development.
    """
    st.info(content)

content2= """
Below you can find some of the apps I have built in Python. 
Feel free to contact me!
"""
st.write(content2)

col3, col4 = st.columns(2)
df=pandas.read_csv("data.csv")

with col3:
    for index, row in df[0:1].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("Images/"+row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[1:2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("Images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
