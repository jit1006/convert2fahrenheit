import streamlit as st
c = st.number_input('celsius')

f = compute( c )
st.write('Enter the temperature in celsius(C): ', f)

def compute():
    #coverting c to f
    #c = int(celsius)
    fahrenheit = (c * 1.8) + 32
    #print("fahrenheit : " , fahrenheit ,"F")
    return fahrenheit

# compute(input("Enter the temperature in celsius(C): "))

