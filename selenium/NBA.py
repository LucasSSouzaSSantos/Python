import time
import requests
import pandas as pd
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

# pegar conteúdo HTML a partir da URL
url = 'https://stats.nba.com/players/traditional/?sort=PTS&dir=-1'

# instanciar o firefox
option = Options()
option.headless = True
driver = webdriver.Firefox(executable_path='./geckodriver')

driver.get(url)

time.sleep(5)

driver.find_element_by_xpath("//div[@class='nba-stat-table']//table//thead//tr//th[@data-field='PTS']").click()

driver.quit()
