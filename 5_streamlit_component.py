import streamlit as st  #파이썬 간단 프론트엔드

#st.balloons()
#1.'헤더', '타이틀' 같은 큰 글씨 적용하기
# st.title("스트림릿 타이틀")
# st.header("이것은 헤더입니다.")
# st.subheader('서브헤더입니다.')

#2.'텍스트'를 입력하는 방법
#1.text
# 단순한 문자열, 포매팅 없음, 고정된 형식
# st.text("고정된 형식의 문자를 표시")

# #2. write 
# #유연한 표현, 입력 데이터에 따라 자동으로
# #적절한 형식을 지정해 줘야 할 때. 
# #데이터프레임도 표시 가능, 문자열, 리스트..
# color = 'red'
# st.write(color)

# #3. 마크다운(.md) 
# #코랩, README.md
# st.markdown("https://naver.com")
# st.markdown('[naver](https://naver.com)')

# #4. HTML 
# html_page = """
# <div style="background-color:blue;padding:50px">
# 	<p style="color:yellow;font-size:5'px">Enjoy Streamlit!</p>
# </div>
# """
# #markdown에다가 html코드를 직접 삽입, unsafe_allow_html을 적용
# st.markdown(html_page, unsafe_allow_html=True)

#-------
#5. 반응
# st.success("성공!")
# st.warning('주의하세요')
# st.error('에러가 발생함')
# st.info('정보 전달')

#6. 미디어 연결
#이미지, 오디오, 유튜브 연결
#PIL(pillow 라이브러리)
from PIL import Image 

#Image.open(이미지가 있는 경로)
# C:/User/
# C:\User\
# img = Image.open("./peng.jpg")
# #st.image(이미지 객체, width=너비, caption=그림설명)
# st.image(img, width=300, caption='hi!')

#비디오 파일 소장->경로로 연결

#open(미디어의 위치, 이 미디어로 무슨작업?)
#r(read) , w(write) 
#rb -> read binary
# video_file = open('./시나리오2 최종본.mp4', 'rb')
# video_binary = video_file.read()
# st.video(video_binary)

# #유튜브 주소!(영상주소)
# st.video('https://www.youtube.com/watch?v=8ib4Qnh2HFE')

# #오디오 파일 연결
# audio_file = open('경로', 'rb')
# audio_binary = audio_file.read()
# st.audio(audio_binary)

#=====================================
#상호작용
#1.버튼 누르기
#if를 사용해서 버튼이 눌리면 할 동작 지정
# if st.button("눌러줘요"):
#     st.balloons()

# #2. 체크박스
# if st.checkbox("체크해주세요"):
#     st.info('동의합니다.')

# #3. 라디오박스 -> 선택지가 여러개일 때, 하나를 고르게 함
# radio_button = st.radio('선택하세요', ['쉬기', '공부하기'])
# if radio_button == '쉬기':
#     st.success('쉬세요!')
# else:
#     st.warning('정말로?')
#     st.button('버튼을 다시 한 번 눌러주세요.')

# #4. select box
# city = st.selectbox('거주지를 고르세요', 
#                     ['영등포구', '강서구', '구로구'])
# #다중 선택
# job = st.multiselect('희망 직무를 선택하세요', 
#                      ['데이터분석', '인공지능개발', 'Ax자동화'])

#-----------------------------------
#텍스트 입력
#1. text_input : 한 줄 입력 / 이름, 이메일 주소, 짧은 입력
# email = st.text_input("메일주소를 입력하세요...",
#               placeholder='jeongeunswd@gmail.com')

# if st.button('입력'):
#     st.write(email)

# #2. test_area : 여러 줄 입력 / 댓글, 설명, 피드백 긴 글
# reply = st.text_area('댓글을 달아주세요', 
#                      placeholder='예시) 추천합니다..')

# #number_input옵션의 min_value, max_value, step은 모두 같은 자료형
# number = st.number_input('숫자를 입력하세요.',
#                          min_value=0.0,
#                          max_value=100.0,
#                          step=0.5)

#슬라이더~~~
# val = st.slider('값을 선택하시오.', 0, 10)
# st.write(val)

# #시간표시
# import datetime 
# import time 

# #datetime.datetime.now() 현재시각표시 함수
# today = st.date_input('Today is', datetime.datetime.now())
# st.write(today)

# from datetime import datetime
# #시간입력
# hour = st.time_input('the time is', datetime.now())

# ---- 그래프 그리기-------------------
# import pandas as pd 
# import matplotlib.pyplot as plt 
# import seaborn as sns 

# #공유드라이브 '머신러닝' 할 때 썼던 파일 중
# #1.기초데이터분석 -> 2.데이터분석 기초 ->  데이터 gapminder.tsv
# df = pd.read_csv('./gapminder.tsv', sep='\t')
# #st.dataframe(df)

# #https://docs.streamlit.io/develop/api-reference/charts
# #sns, plt 그림을 그린 뒤 변수 저장
# bar = sns.barplot(df, x='country', y='pop')
# #plt.show() 역할을 st.pyplot()
# st.pyplot()

# #streamlit으로 그림 그리기
# #streamlit이 가진 '그래프 함수' 활용, seaborn라이브러리처럼 그림
# st.bar_chart(df, x='country', y='pop')

#================== 블로그 ===== /티스토리, 노션, github pages
#JSON 
data = {'name': 'john', 'surname': 'wick'}
st.json(data)

codes = '''  
import os

path = os.path.join(origin, 'train.csv')
 '''
st.code(codes, language='python')

#progress bar(UI/UX) -> tqdm
import time
# my_bar = st.progress(0)
# for v in range(100):
#     time.sleep(1)
#     my_bar.progress(v+1)

with st.spinner("기다려주세요..."):
    time.sleep(10)
st.success('완료되었습니다!')