# instalar o streamlit
# pip install streamlit

# importando a biblioteca
import streamlit as st 

st.write('Olá Mundo!')
st.write('Meu Nome é Karina')
st.write('Programação em Python')
st.text_input('digite seu peso')
st.text_input('digite sua altura')

if st.button("Send balloons!"):
    st.balloons()