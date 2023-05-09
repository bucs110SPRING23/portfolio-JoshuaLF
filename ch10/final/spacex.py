import requests

class SpaceXProxy:
    def __init__(self):
        self.url = "https://api.spacexdata.com/v4/launches/latest"
    
    def get_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            return None