import streamlit as st


st.title("Temperature Converter ")

c = st.number_input('Enter the celsius temperature ')

#coverting c to f
f = (c * 1.8) + 32

st.write('The Fahrenheit temperature is ', f )
d = int(f)
st.header("Temperature metric")

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", d , "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

