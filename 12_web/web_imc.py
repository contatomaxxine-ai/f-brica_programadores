#autor: Karina Sousa
#projeto: IMC com streamlit


# importando a biblioteca
import streamlit as st 


st.title('Calculadora de IMC')
peso = st.number_input('Digite seu peso (kg):')
altura = st.number_input('Digite sua altura:')

# ação do botão
st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #6495EDcc;
    color: white;
}
div.stButton > button:first-child:hover {
    background-color: #004d99;
    color: white;
}
</style>
""", unsafe_allow_html=True)
if st.button('Calcular IMC', type="primary"):
   
   # verifica se o usuário digitou valor > que zero
   if peso > 0 and altura > 0:
      imc = peso / (altura ** 2)
      st.warning(f"Seu IMC é: {imc:.2f}")
      if imc <= 18.5:
         st.warning('Abaixo do peso',icon="⚠️")
      elif imc <= 24.9:
         st.sucess('Peso normal!', icon="✅")
      elif imc <= 29.9:
         st.warning('Sobrepeso',icon="⚠️")
      elif imc <= 34.9:
         st.warning('Obesidade Grau I',icon="⚠️")
      elif imc <= 39.9:
         st.warning('Obesidade Grau II',icon="⚠️")
      else:
         st.error('Obesidade Grau III',icon="🚨")
   else:
      st.warning('Digite um valor válido',icon="⚠️")




