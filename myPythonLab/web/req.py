import requests
import sys

def getWeather():
    url = 'http://api.worldweatheronline.com/premium/v1/weather.ashx'
    city = sys.argv[1]
    params = { 'key': '68608138c44e4eeab98161340241405',
            'q': city,
            'format': 'json',
            'num_of_days': 2,
            'lang': 'ru'}
    r = requests.post(url, params=params)
    weather = r.json()
    if 'data' in weather:
        if 'current_condition' in weather['data']:
            try:
                return weather['data']['current_condition'][0]
            except(IndexError, TypeError):
                return "Server error"
    return "Server error"

if __name__ == '__main__':
    weather = getWeather()
    print(f'Погода: {weather["temp_C"]}, ощущается как {weather["FeelsLikeC"]}')
