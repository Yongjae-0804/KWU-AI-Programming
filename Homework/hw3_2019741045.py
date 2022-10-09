import wordcloud as wc
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.by import By

# import selenium
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait

address = 'https://namu.wiki/w/KBO%20%EB%A6%AC%EA%B7%B8'

driver = webdriver.Chrome() #드라이버에 연결???
#경로가 같은 파일이 아니면 인자에 executable_path= '드라이버 경로' 입력

driver.get(url=address) #페이지 열기????
web = driver.find_elements(By.XPATH, '//*[@id="jWZtJ8Cjb"]/div[2]/div/div/div/div') #선택하기???? html 들어가서 우클릭 카피 누르면 xpath 뜸



data = "" #빈 문자열 생성 because 워드 크라우드는 str에서 작동?????
for i in web:
    data += i.text #텍스트를 뽑는 메서드를 활용 계속 집어 넣어준다.?????

s_words = wc.STOPWORDS.union({'one', 'two', 'three', 'year', 'first', 'second','있다','월'}) #쓸모없는 단어

image = wc.WordCloud(font_path='C:/WINDOWS/FONTS/MALGUNSL.TTF', 
width = 1000, height = 700, stopwords = s_words).generate(data) # 워드크라우드 생성

plt.figure(figsize = (40,30)) #파이플롯
plt.imshow(image)
plt.show()

driver.close() #창 닫기
driver.quit() # 드라이버 종료