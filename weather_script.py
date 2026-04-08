#fetch weather data from OpenWeatherMap API
import requests
def get_weather(city):
    api_key = "2ff29e7b80e3769f00b367f9b4dc0e2a"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    if data["cod"] != "404":
        main = data["main"]
        temperature = main["temp"]
        humidity = main["humidity"]
        weather_desc = data["weather"][0]["description"]
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather description: {weather_desc}")
    else:
        print("City Not Found") 
if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
    
