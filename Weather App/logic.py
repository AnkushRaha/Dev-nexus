import requests

def get_input(): #gets input from user
   city = input("Enter A City : ").upper()
   return city

def fetch_data(user_input): #fetchs data from server
   api_key = '9b5dfb912fd0f9514325c4b3caaf034f'
   weather_data = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={user_input}&appid={api_key}&units=metric")
   return weather_data

def col_data(data): #collects important datas
   json_data = data.json()
   weather = json_data['weather'][0]['main']
   temp = json_data['main']['temp']
   wind = json_data['wind']['speed']
   humidity = json_data['main']['humidity']
   pressure = json_data['main']['pressure']
   return weather, temp, wind, humidity, pressure

def return_data(): #returns collected important data
    user_input = get_input()
    data = fetch_data(user_input)
    weather, temp, wind, humidity, pressure = col_data(data)
    return weather, temp, wind, humidity, pressure

def main(): # the main all in one function 
    weather, temp, wind, humidity, pressure = return_data()
    print("Weather:", weather)
    print("Temperature:", temp, "°C")
    print("Wind Speed:", wind)
    print("Humidity:", humidity)
    print("Pressure:", pressure)
