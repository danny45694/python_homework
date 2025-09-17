from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


driver.get("https://en.wikipedia.org/wiki/Web_scraping")

options = webdriver.ChromeOptions()
options.add_argument('--headless') #Enable headless mode
options.add_argument('--disable-gpu') # Optional, recommended for Windows
options.add_argument('--window-size=1920x1080') #Optional, set window size

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install(),options=options))