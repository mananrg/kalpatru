import requests

res=requests.get('https://en.wikipedia.org/wiki/Politics_of_the_United_States')

print(res.text)
