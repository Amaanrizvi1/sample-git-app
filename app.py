import streamlit as st

st.title('campusx an online platform')
col1,col2=st.columns(2)
with col1:
    st.image('wallpaperflare.com_wallpaper.jpg')
with col2:
    st.write("""
    campusx is an online learning plataform for data science """)

st.sidebar.selectbox( "select one",['teacher','student'])
st.sidebar.button('select')