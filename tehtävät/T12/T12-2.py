import json
import requests

pyynto = "http://api.openweathermap.org/data/2.5/forecast?id=524901&appid=cc32af8722007c1903789ef6e9a55d23"
vastaus = requests.get(pyynto).json()
print(json.dumps(vastaus, indent=2))