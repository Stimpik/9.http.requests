import requests

base_url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/'
all = '/all.json'
names = []
respone = requests.get(base_url + all)
for name in respone.json():
    if name['name'] in ['Hulk', 'Captain America', 'Thanos']:
        names.append(name)
print('Самый умный:', sorted(names, key=lambda x: x["powerstats"]["intelligence"], reverse=True)[0]['name'])
