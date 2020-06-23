from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get("https://www.instagram.com/")

nome = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/span', Keys.ARROW_DOWN)
nome.send_keys("#")

senha = driver.find_element_by_xpath()('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/span//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/span', Keys.ARROW_DOWN)
senha.send_keys("#")


conectar = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button')
conectar.click()
