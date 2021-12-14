!pip3 install selenium==3.141
!apt-get update
!apt install chromium-chromedriver
!cp /usr/lib/chromium-browser/chromedriver /usr/bin


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--headless')        # Head-less 설정
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver', options=options)

driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")

elem = driver.find_element_by_name("q")
elem.send_keys("아이유")
elem.send_keys(Keys.RETURN)
cur = os.getcwd()
cur = cur +"/test/"
print("위치"+cur)
count = 1

images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
count = 1
for image in images:  
      image.click()
      time.sleep(2)
      imgUrl = images = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
      urllib.request.urlretrieve(imgUrl, cur+str(count) + ".jpg")
      count = count + 1

driver.close()