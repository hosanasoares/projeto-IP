import streamlit as st

st.title('Conversão')

temp = st.number_input('digite uma temperatura:')

if st.button('conversão'):
    fa = 32 + temp*32
    st.text('resultado:')
    st.title(fa)
    