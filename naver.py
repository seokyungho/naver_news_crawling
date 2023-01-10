import requests
from bs4 import BeautifulSoup #Beutifulsoup 의 s는 대문자여야함


#header = {'User-agent' : 'Mozila/2.0'}
#naver 서버에 대화 시도
response = requests.get("https://sports.news.naver.com/index")


html = response.text
soup = BeautifulSoup(html,'html.parser')


titles = soup.select(".link_today") #id는 맨앞에 # 붙혀야함
for title in titles:
    print(title.text.strip())