import streamlit as st

st.title('campusx')
col1,col2=st.columns(2)
with col1:
    st.image('wallpaperflare.com_wallpaper.jpg')
with col2:
    st.write("""
    campusx is an online learning plataform for data science """)

st.header('courses')
st.subheader("DSMP")
st.subheader("DAMP")
st.subheader('EDA')
st.subheader("DSA")


st.sidebar.title('menu')
st.sidebar.markdown("""
- Home 
- About 
- Contact 
- Career
- Login 
""")