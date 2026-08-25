"""
Weather Lookup Tool (Day 8)
---------------------------
Takes a city's latitude and longitude, queries an external REST API,
checks response status codes, and handles timeout/connection errors safely.
"""
import requests

def get_weather(latitude, longitude, city_name="location"):
    #Open-meteo public API endpoint
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"

    try:
        #Set a 5-second timeout to prevent hanging execution
        response = requests.get(url, timeout=5)

        #Raise HTTPError for 4xx or 5xx status codes
        response.raise_for_status()

        data = response.json()
        current = data.get("current_weather",{})
        temp = current.get("temperature")
        windspeed = current.get("windspeed")

        return f"Current weather on {city_name}: {temp}C with wind speed of {windspeed} km/h."
    except requests.exceptions.Timeout: 
        return f"Error: Request to weather service for {city_name} timed out"
    except requests.exceptions.HTTPError as http_err:
        status_code = http_err.response.status_code if http_err.response else "Unknown"
        return f"HTTP error occurred: {http_err}(Status Code: {response.status_code})"
    except requests.exceptions.RequestException as req_err:
        return f"Network or connection error: {req_err}"

if __name__ == "__main__":
    #Test coordinates(e.g: london: 51.5074, -0.1278)
    print(get_weather(51.5074, -0.1278, "London"))