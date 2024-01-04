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