# B"H

# https://pykit.org/python-api-requests-a-beginners-guide-on-api-python-2022/

import requests

URL = "https://random-word-api.herokuapp.com/word"

response = requests.get(url = URL)

word = response.text[2:len(response.text)-2]

print(word)