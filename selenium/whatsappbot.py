from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(10)

# Definir contatos e grupos e mensagem a ser enviada

contatos = ['Camila Irmã']
mensagem = 'Eu sou um robô feito pelo seu irmão, fico enviando mensagem para pessoas chatas... vai trabalhar chataaaaaa....'

# Buscar contatos/grupos


def buscar_contato(cont):
    campo_pesquisa = driver.find_element_by_xpath(
        '//div[contains(@class, "copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquisa.click()
    campo_pesquisa.send_keys(cont)
    campo_pesquisa.send_keys(Keys.ENTER)


def enviar_mensagem(msg):
    campo_mensagem = driver.find_elements_by_xpath(
        '//div[contains(@class, "copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(msg)
    campo_mensagem[1].send_keys(Keys.ENTER)


for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)
