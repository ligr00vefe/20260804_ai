from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

# 웹페이지로 이동
driver.get('https://www.naver.com/')
time.sleep(1)

# 버튼 찾아 클릭
button = driver.find_element(By.CLASS_NAME, 'MyView-module__link_login___HpHMW')
button.click()

# 데이터 로드까지 대기
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'loadedData'))
    )
finally:
    driver.quit()

# 데이터 추출
data = element.text
