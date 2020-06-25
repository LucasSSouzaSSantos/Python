from selenium import webdriver

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get("https://www.facebook.com/")

email = driver.find_element_by_xpath("//input[@name='email']")
email.clear()
email.send_keys("Email_Do_Facebook")

senha = driver.find_element_by_xpath("//input[@name='pass']")
senha.clear()
senha.send_keys("senha")

entrar = driver.find_element_by_xpath("//*[@id='u_0_b']")
entrar.click()
