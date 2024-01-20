import requests

city=input("Enter Your City --> ")
Api_Key = "9efa18a81de6877e01ee74e2e479bf90"

final_URL = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city,Api_Key)

result = requests.get(final_URL)
data = result.json()

temprature = data['main']['temp']
cordinatelon = data['coord']['lon']
cordinatelat = data['coord']['lat']

print(temprature,"K")
print(cordinatelat,"°N")
print(cordinatelon,'°E')