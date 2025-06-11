import requests
import json

# API dan ma'lumot olish
javob = requests.get('https://jsonplaceholder.typicode.com/posts')
malumot = json.loads(javob.text)  # JSON ma'lumotini o'qiymiz
print(malumot)
