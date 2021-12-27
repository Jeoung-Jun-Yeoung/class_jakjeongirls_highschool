from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
elem = driver.find_element_by_name("q")
elem.send_keys("아이유")
elem.send_keys(Keys.RETURN)
driver.find_elements_by_css_selector(".rg_i.Q4LuWd")[1].click()
time.sleep(2)
imgUrl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")

openr = urllib.request.build_opener()
urllib.request.install_opener(openr)
urllib.request.urlretrieve(imgUrl, "test.jpg")
