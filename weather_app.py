import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for API
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
        temperature = data['main']['temp']
        weather = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        print(f"\n🌍 Weather in {city_name.title()}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {weather.capitalize()}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("\n❌ Error fetching weather data. Check the city name or API key.")

if __name__ == "__main__":
    print("🌤️ Welcome to Weather App 🌤️")
    api_key = input("Enter your OpenWeatherMap API Key: ").strip()
    city = input("Enter city name: ").strip()
    get_weather(city, api_key)
