import requests
responses = requests.get("https://api.stackexchange.com/questions?fromdate=2022-11-19&order=desc&sort=activity&tagged=python&filter=default&site=stackoverflow").json()
for response in responses['items']:
    print(f"{response['owner']['display_name']} задает вопрос: {response['title']}. Ссылка на вопрос: {response['link']}")
    
