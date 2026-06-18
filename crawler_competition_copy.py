# 인터넷에 대한 요청 -> requests
import requests
# 정적 웹페이지 크롤링 -> bs
from bs4 import BeautifulSoup
# 동적 웹페이지 크롤링(들어오는 사람에 따라 바뀌는 닉네임같은거)
from selenium import webdriver


# 시간 라이브러리, 시간 재는거
import time
# 진행률을 보여주는 라이브러리 + for 문이랑 같이 씀.
from tqdm import tqdm

# 크롤링한 내용을 엑셀파일로 저장하기 위해.
# xlsx -> openpyxl(파이썬으로 엑센 컨트롤 근데 무거워서 그냥 판다스로 csv로 저장해서 씀)
import pandas as pd

# 국민청원사이트 이런곳은 수정을 잘 안해서 테스트로 쓰기 좋아서 씀.
# requests 라이브러리를 사용해서 웹페이지를 읽어와라(get)
number = 3
url =f'https://www.cheongwon.go.kr/portal/petition/open/view?pageIndex={number}'
response = requests.get(url)
#print(response)


# 웹페이지를 분해할 bs4 객체생성
# 파싱 = 어떤 정보 덩어리에서 원하는 정보를 추출하는것
soup = BeautifulSoup(response.text, 'html.parser')
#print(response.text)

# soup라는 파싱 객체가, 'span'이라는 양식의 class를 찾아서
# class=category라고 적힌 내요을 카테고리라는 변수 이름에 저장
category = soup.find_all('span', class_ ='category')
subject = soup.find_all('span', class_ = 'subject')
petition = soup.find_all('span', class_ ='text')
#print(category, subject, petition)

# 위에 크롤링한 결과물을 보기 쉬운 형태로 변환해주자
corpus = []
for c, s, t in zip(category, subject, petition):
    corpus.append([c.text, s.text, t.text])

time.sleep(2) # 2초 정도 정지

df= pd.DataFrame(corpus, columns=['카테고리','제목','청원내용'])
#print(df.head())
df.to_csv('./crawling_sample.csv', index=False, encoding='utf-8-sig')
