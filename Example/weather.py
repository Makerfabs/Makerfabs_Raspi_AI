import requests

url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"lang":"en","units":"metric","q":"New York City"}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "47313e7efamshc596ab4201dc763p1c4275jsn3cdf6312f886"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)