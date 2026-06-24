import tkinter as tk
import requests
from datetime import datetime  

def get_weather():
    city = city_entry.get().strip()
    if not city or city == "Enter City Name":
        result_label.config(text="⚠️ Please enter a city name!")
        return

    result_label.config(text="🔍 Searching...")
    root.update_idletasks()

    url = f"https://wttr.in/{city}?format=j1"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        current = data['current_condition'][0]
        area = data['nearest_area'][0]
        
        temp_c = current['temp_C']
        desc = current['weatherDesc'][0]['value']
        humidity = current['humidity']
        wind_speed = current['windspeedKmph']
        region = area['region'][0]['value']
        country = area['country'][0]['value']

        
        current_date = datetime.now().strftime("%A, %B %d, %Y")

        weather_report = (
            f"🌍 {city.title()}, {region}\n"
            f"🏳️  {country}\n"
            f"📅 {current_date}\n" 
            f"---------------------------\n"
            f"🌡️  Temperature: {temp_c}°C\n"
            f"☁️  Condition: {desc}\n"
            f"💧 Humidity: {humidity}%\n"
            f"💨 Wind: {wind_speed} km/h"
        )
        result_label.config(text=weather_report)

    except requests.exceptions.HTTPError:
        result_label.config(text="❌ City not found.\nCheck spelling!")
    except requests.exceptions.ConnectionError:
        result_label.config(text="❌ No network connection!")
    except (KeyError, IndexError):
        result_label.config(text="❌ Server data error.\nTry again later.")


root = tk.Tk()
root.title("Weather App")
root.geometry("400x500") 
root.configure(bg="#2b2d42")

title_label = tk.Label(
    root, 
    text="Live Weather Forecast", 
    font=("Arial", 18, "bold"), 
    bg="#2b2d42", 
    fg="#edf2f4"
)
title_label.pack(pady=20)

city_entry = tk.Entry(
    root, 
    font=("Arial", 14), 
    width=22, 
    justify="center", 
    bd=0, 
    highlightthickness=2,
    highlightbackground="#8d99ae",
    highlightcolor="#ef233c"
)
city_entry.pack(pady=10)
city_entry.insert(0, "Enter City Name")

def clear_placeholder(event):
    if city_entry.get() == "Enter City Name":
        city_entry.delete(0, tk.END)

city_entry.bind("<FocusIn>", clear_placeholder)

search_btn = tk.Button(
    root, 
    text="Get Weather", 
    command=get_weather, 
    font=("Arial", 12, "bold"),
    bg="#ef233c", 
    fg="#ffffff", 
    activebackground="#d90429", 
    activeforeground="#ffffff",
    bd=0,
    padx=15,
    pady=5,
    cursor="hand2"
)
search_btn.pack(pady=15)

result_label = tk.Label(
    root, 
    text="Type a city and press search!", 
    font=("Arial", 13), 
    bg="#3d405b", 
    fg="#f4f1de",
    width=32,
    height=11, # Increased height slightly for a clean look
    relief="flat",
    justify="left",
    padx=15,
    pady=15
)
result_label.pack(pady=20)

root.mainloop()