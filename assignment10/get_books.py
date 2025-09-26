import pandas as pd
import time
import re

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"

driver.get(url)

time.sleep(3)

#------------------------------TASK2-------------------------------------
#ul class="results"
#li class="row cp-search-result-item"
#div class="cp-search-result-item-content"
#span class="title-content" #Stores title
#span class="a.author-link" #stores author
#div class="manifestation-item-format-info-wrap"
#span class="display-info-primary"


#----------------------------TASK 3----------------------------------


li_elements = driver.find_elements(By.CSS_SELECTOR, "li.row.cp-search-result-item")  #Find Li elements I am looking for
#print(f"print {len(li_elements)}")

results = []


for li in li_elements:
    
    title = driver.find_element(By.CSS_SELECTOR, 'span.title-content').text
    
    authors = driver.find_elements(By.CSS_SELECTOR, 'a.author-link')
    join_author = "; ".join([author.text for author in authors])
    
    year = li.find_element(By.CSS_SELECTOR, 'span.display-info-primary').text
    pull_year = re.search(r'\d{4}', year)
    format_year = int(pull_year.group())

    dict = {
    "Title": title,
    "Author": join_author,
    "Year": format_year,
    }

    results.append(dict)

#print(results[0])

driver.quit()


#----------------------------- TASK 4 ----------------------------
df = pd.DataFrame(results)
print(df)

df.to_csv('get_books.csv', index=False)
get_books_json = "get_books.json"

df.to_json(get_books_json, orient='records', indent=4)
print(get_books_json)



