import pandas as pd
import time
import json
import os 

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")

time.sleep(5)

options = webdriver.ChromeOptions()
options.add_argument('--headless') #Enable headless mode
options.add_argument('--disable-gpu') #Recommended for Windows
options.add_argument('--window-size=1920x1080') #Set window size

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=options)

#ul class="results"
#li class="row cp-search-result-item"
#div class="cp-search-result-item-content"
#h2 class = "cp-title" #Stores title
#span class="cp-by-author-block --block" #stores author
#div class="manifestation-item-format-info-wrap"


li_elements = driver.find_elements(By.CLASS_NAME, 'row cp-search-result-item')  #Find Li elements I am looking for
print(len(li_elements))
#results = []

#for li in li_elements:
    #title = driver.find_element(By.CLASS_NAME, 'cp-title')
    #author = driver.find_element(By.CLASS_NAME, 'cp-author-link')
    #year = li.find_element(By.CSS_SELECTOR, 'div.cp-format-year')