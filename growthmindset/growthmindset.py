import streamlit as st
import requests 

def Weather_App(city):
    BASE_URL = f"https://wttr.in/{city}?format=%C+%t"
    response = requests.get(BASE_URL)
    
    if response.status_code == 200:
        return response.text
    else:
        return "Sorry your request is not accepted"
    
    # Streamlit UI 

st.title("Weather_App")
st.write("Enter your city name and get updated weather")

user_input = st.text_input("Enter your city name")

if st.button("Click Here"):
    if user_input:
        result_weather = Weather_App(user_input)
        st.write(f"Weather In {user_input}: {result_weather}") 
    else:
        st.warning("Please enter a city name")
    