import streamlit as st
c = st.number_input('celsius')
def compute(c):
    #coverting c to f
    #c = int(celsius)
    fahrenheit = (c * 1.8) + 32
    #print("fahrenheit : " , fahrenheit ,"F")
#     return fahrenheit
    st.write('Enter the temperature in celsius(C): ', fahrenheit)
# compute(input("Enter the temperature in celsius(C): "))

