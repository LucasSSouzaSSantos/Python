from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get("file:///home/lucas/Documentos/GitHub/HTML5-Aulas/_Segundo_Site/contato.html")
# os comando acima acessa a página inicial do google chrome

# 3.1 Interagindo com a página
nome = driver.find_element_by_name("fnome")
nome.clear()
nome.send_keys("Fernando")

telefone = driver.find_element_by_name("ffone")
telefone.clear()
telefone.send_keys("(81) 98456-7896")

email = driver.find_element_by_name("fEmail")
email.clear()
email.send_keys("fernandoGod@Vaiestudar.com")

cep = driver.find_element_by_name("fCep")
cep.clear()
cep.send_keys("54045-909")

modulo = driver.find_element_by_name("fModulo")
modulo.clear()
modulo.send_keys(5)

horario = driver.find_element_by_name("fHorario")
horario.clear()
horario.send_keys("10:30")

cor = driver.find_element_by_name("fCor")
cor.clear()
cor.send_keys("#00ff00")

nascimento = driver.find_element_by_name("fNascimento")
nascimento.clear()
nascimento.send_keys("21/02/1992")

sleep(4)
driver.close()
