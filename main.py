import streamlit as st

celsius = st.number_input('Enter the celsius temperature ')
def compute(celsius):
    #coverting c to f
    f = (c * 1.8) + 32
    d = float(f)
    st.write('The Fahrenheit temperature is ', d )
#     return f
    #print("fahrenheit : " , fahrenheit ,"F")
    # compute(input("Enter the temperature in celsius(C): "))

