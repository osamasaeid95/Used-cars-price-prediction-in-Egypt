import streamlit as st

def app():
   st.title("Used cars price prediction in Egypt Using machine learning")
   st.header("Epsilon AI istitute project")
   st.header("By : Osama Saeid")
   st.write("It is based on features from datasets")
   brand = st.radio("Select your brand", ["Hyundai", "Fiat", "Chevrolet"])
   model = st.selectbox("Choose the model", [])
   
app()
   