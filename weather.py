import requests

def Weather(city):
    api_ = "http://api.openweathermap.org/data/2.5/weather?appid=acf5bed35524c8f8c44b21162250cf93&q="

    url_ = api_ + 'city'
    json_data = requests.get(url_).json()
    format_add = json_data['main']

    return format_add

# api_ = "http://api.openweathermap.org/data/2.5/weather?appid=acf5bed35524c8f8c44b21162250cf93&q="
#
# city = input('City Name :')

# url = api_ + city
# json_data = requests.get(url).json()
# format_add = json_data['main']

# print(format_add)
# print(json_data)
# print(format_add['temp'])

# print("The weather is just {0} but feels like {1} and the mininum temperature is {2} and the maximum temperature is {3}".format(round(format_add['temp'] - 273), int(format_add['feels_like'] - 273), int(format_add['temp_min'] - 273), int(format_add['temp_max'] - 273)))
