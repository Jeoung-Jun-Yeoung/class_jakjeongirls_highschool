from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko")
elem = driver.find_element_by_name("q")
elem.send_keys("아이유")
elem.send_keys(Keys.RETURN)

SCROLL_PAUSE_TIME = 1
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
# 자바스크립을 통해 찾아서 브라우저에 높이를 얻는다.

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    #브라우저 끝까지 스크롤을 내린다. 0(시작부터 끝까지)
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    #스크롤을 내리고 로딩이 끝날동안 기다린다. 
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    #새로운 높이에 더해준다. 이때 새로운 높이랑 이전높이랑 같다면 다 로딩이 된것.
    #추가로 결과 더보기를 클릭하기 위해 밑에 트라이를 해준다. 이것도 f12로 볼것!
    if new_height == last_height:
        try:
            driver.find_element_by_css_selector(".mye4qd").click()
        except:
            break
        #클릭할것도 없고 높이도 같다면 모든 조건을 만족했기에 나간다.
    last_height = new_height

name = "아이유"
images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1
for image in images:
    try:
        image.click()
        time.sleep(2)
        imgUrl = driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img").get_attribute("src")
        opener=urllib.request.build_opener()
        opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(imgUrl, name+str(count)+".jpg")
        count = count + 1
    except:
        pass

driver.close()