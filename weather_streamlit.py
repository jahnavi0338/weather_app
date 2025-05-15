import streamlit as st
import requests

st.title("Weather App")

city = st.text_input("Enter city name")

if st.button("Get Weather"):
    api_key = "57f99a618fe6a0857a83f6cf50bfaf39"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        st.write(f"Weather: {weather}")
        st.write(f"Temperature: {temp} °C")
    else:
        st.error("City not found.")
