
GET_COORDS_BY_IP = False
# if coords are None, the program get coordinates by ip
latitude = 60
longitude = 30


# you get api here: https://home.openweathermap.org/api_keys
API_KEY = '1c243b0216766c41fde8135d48342b06'

OPENWEATHER_URL = ('https://api.openweathermap.org/data/2.5/weather?'
                   'lat={latitude}&lon={longitude}'
                   '&appid=' + API_KEY + '&lang=ru&units=metric')

IPINFO_URL = 'http://ipinfo.io/json'
