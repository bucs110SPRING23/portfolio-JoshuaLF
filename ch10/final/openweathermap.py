import requests

class OpenWeatherMapProxy:
    def __init__(self, api_key):
        self.url = f"https://api.openweathermap.org/data/2.5/weather?lat=25.9973164&lon=-97.1572994&appid={api_key}"
    
    def get_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            return None