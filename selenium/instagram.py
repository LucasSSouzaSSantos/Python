from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get("https://www.instagram.com/")

nome = driver.find_element_by_name("username", Keys.ARROW_DOWN)
nome.send_keys("#")

senha = driver.find_element_by_name("password", Keys.ARROW_DOWN)
senha.send_keys("#")


conectar = driver.find_element_by_xpath("")
conectar.click()
