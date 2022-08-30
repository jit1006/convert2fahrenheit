import streamlit as st
celsius = st.number_input('Insert a number')
st.write('The current number is ',celsius)
def compute(celsius):
    #coverting c to f
    c = int(celsius)
    f = (c * 1.8) + 32
    st.dataframe(f)
    #print("fahrenheit : " , fahrenheit ,"F")
    #f = st.number_input('celsius')
#     st.write('The Temperature in (F): ', f)
    # compute(input("Enter the temperature in celsius(C): "))

