import requests
from bs4 import Beautifulsoup

response = requests.get("http://www.naver.com")
html = response.text
soup = Beautifulsoup(html,'html.parser')
word = soup.select_one("#NM_set_home_btn")
print(html)
