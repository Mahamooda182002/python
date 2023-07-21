import requests

def get_weather(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] == "404":
        print("City not found.")
    else:
        weather_info = {
            "Temperature": data["main"]["temp"],
            "Description": data["weather"][0]["description"],
            "Humidity": data["main"]["humidity"],
            "Wind Speed": data["wind"]["speed"],
        }
        return weather_info

def main():
    api_key = "YOUR_API_KEY"
    city = input("Enter the name of the city: ")

    weather_info = get_weather(api_key, city)
    if weather_info:
        print(f"Weather information for {city}:")
        for key, value in weather_info.items():
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()
