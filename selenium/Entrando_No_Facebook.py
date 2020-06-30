from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get("https://www.facebook.com/")

email = driver.find_element_by_xpath("//input[@name='email']")
email.clear()
email.send_keys("lucas210souza@gmail.com")

senha = driver.find_element_by_xpath("//input[@name='pass']")
senha.clear()
senha.send_keys("lucas123")

pensar = driver.find_element_by_xpath("placeholder-jjrv")
pensar.clear()
pensar.send_keys("")


sleep(2)
driver.close()

entrar = driver.find_element_by_xpath("//*[@id='u_0_b']")
entrar.click()
