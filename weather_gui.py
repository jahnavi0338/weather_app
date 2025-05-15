import tkinter as tk
import requests

def get_weather():
    city = city_entry.get()
    api_key = "57f99a618fe6a0857a83f6cf50bfaf39"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        result_label.config(text=f"Weather: {weather}\nTemperature: {temp} °C")
    else:
        result_label.config(text="City not found.")

app = tk.Tk()
app.title("Weather App")

tk.Label(app, text="Enter city name:").pack()

city_entry = tk.Entry(app)
city_entry.pack()

tk.Button(app, text="Get Weather", command=get_weather).pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
