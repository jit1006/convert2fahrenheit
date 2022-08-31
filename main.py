import streamlit as st

c = st.number_input('Enter the celsius temperature ')

#coverting c to f
f = (c * 1.8) + 32
d = float(f)
st.write('The Fahrenheit temperature is ', d )

