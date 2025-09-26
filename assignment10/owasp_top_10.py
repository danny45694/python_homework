import time
import csv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))



try:
    url = "https://owasp.org/www-project-top-ten/"
    driver.get(url)
    time.sleep(3)

    #test = driver.find_elements(By.XPATH, '/html/body/main/div/div[1]/section[1]/ul[2]/li')


    elements = driver.find_elements(By.XPATH, '//*[@id="sec-main"]/ul[2]/li')
    top10 = []
    for li in elements:
        a = li.find_element(By.TAG_NAME, "a")
        title = a.find_element(By.TAG_NAME, "strong").text
        link = a.get_attribute("href")
        
        #print(a.find_element(By.TAG_NAME, "strong").text, a.get_attribute("href"))

        dict = {"title": title,
                "link": link}

        top10.append(dict)
        
    with open("owasp_top_10.csv", "w", newline="") as csvfile:
        fieldnames = ["title", "link"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for item in top10:
            writer.writerow(item)


    #sec-main > ul:nth-child(13) > li:nth-child(1) > a > strong
finally:
    driver.quit()