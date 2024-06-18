import requests

def get_weather_data(city_name):
    # Replace 'YOUR_API_KEY' with your actual API key from OpenWeatherMap
    api_key = "ee653a2d8999d8237402737cc277778e"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    
    # Use the `params` argument to dynamically build the query string
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'  # Optional: Adds units parameter to get temperature in Celsius
    }
    
    response = requests.get(base_url, params=params)
    weather_data = response.json()
    print(weather_data)
    
    if weather_data["cod"] != "404":
        main_data = weather_data["main"]
        temperature = main_data["temp"]
        pressure = main_data["pressure"]
        humidity = main_data["humidity"]
        weather_description = weather_data["weather"][0]["description"]
        
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature} Kelvin")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_description}")
    else:
        print("City not found.")

# Example usage
get_weather_data("Helsinki")