import openweathermap
import spacex

owm_proxy = openweathermap.OpenWeatherMapProxy(api_key="e87bed4574e5ca084da3d4c8896eccce")
owm_data = owm_proxy.get_data()

spacex_proxy = spacex.SpaceXProxy()
spacex_data = spacex_proxy.get_data()

if owm_data and spacex_data:
    temp_kelvin = owm_data["main"]["temp"]
    temp_fa = (temp_kelvin - 273.15) * 9/5 + 32
    launch_name = spacex_data["name"]
    
    print(f"The current temperature at SpaceX's launchpad in Texas is {temp_fa:.1f} degrees Fahrenheit.")
    print(f"The latest SpaceX launch was called {launch_name}.")
else:
    print("Failed to get data from one or both APIs.")
