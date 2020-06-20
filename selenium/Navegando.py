from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get("url da página")
# os comando acima acessa a página inicial do google chrome

# 3.1 Interagindo com a página
# nome = driver.find_element_by_name("fnome")
nome = driver.find_element_by_xpath("//input[@name='fnome']")
nome.send_keys("Fernando")

telefone = driver.find_element_by_name("ffone")
telefone.clear()
telefone.send_keys("(81) 98456-7896", Keys.ARROW_DOWN)

email = driver.find_element_by_name("fEmail")
email.clear()
email.send_keys("fernandoGod@Vaiestudar.com", Keys.ARROW_DOWN)

cep = driver.find_element_by_name("fCep")
cep.clear()
cep.send_keys("54045-909", Keys.ARROW_DOWN)

modulo = driver.find_element_by_name("fModulo")
modulo.clear()
modulo.send_keys(5, Keys.ARROW_DOWN)

horario = driver.find_element_by_name("fHorario")
horario.clear()
horario.send_keys("10:30", Keys.ARROW_DOWN)

cor = driver.find_element_by_name("fCor")
cor.clear()
cor.send_keys("#00ff00", Keys.ARROW_DOWN)

nascimento = driver.find_element_by_name("fNascimento")
nascimento.clear()
nascimento.send_keys("21/02/1992", Keys.ARROW_DOWN)

enviar = driver.find_element_by_xpath("//input[@name='fenviar']")
enviar.click()

sleep(4)
driver.close()
