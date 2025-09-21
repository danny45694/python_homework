import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "https://owasp.org/www-project-top-ten/"

driver.get(url)
time.sleep(3)

#test = driver.find_elements(By.XPATH, '/html/body/main/div/div[1]/section[1]/ul[2]/li')


unsecure_risks = driver.find_elements(By.XPATH, '//*[@id="sec-main"]/ul[2]/li')

for item in unsecure_risks:
    risk = driver.find_element(By.CSS_SELECTOR, 'a > strong').text
    print(risk)

    #sec-main > ul:nth-child(13) > li:nth-child(1) > a > strong