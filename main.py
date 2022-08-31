import streamlit as st


st.title("Temperature Converter ")

c = st.number_input('Enter the celsius temperature ')

#coverting c to f
f = (c * 1.8) + 32
# d = float(f)
st.write('The Fahrenheit temperature is ', f )

st.header("Display the metric")

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", f ,"°F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

st.header("Temperature Chart ")

chart_data = f.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
