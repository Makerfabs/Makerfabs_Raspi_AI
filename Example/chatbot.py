import requests

url = "http://api.brainshop.ai/get?bid=154007&key=UPVfPPgnrw29KBTk&uid=123456&msg="
url += "What time now?"

response = requests.request("GET", url)

print(response.text)