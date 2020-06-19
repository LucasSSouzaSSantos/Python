from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='./chromedriver')
# Na linha de cima uma instância do chromedriver é criado e é passado
# o caminho aonde o chromedrive estar, usando o comando executable_path
driver.get("https://www.google.com/")
# o método driver.get navegará para uma página fornecida pelo url
assert "Google" in driver.title
# A próxima linha é uma afirmação para confirmar que o título tem
# a palavra "Google"
elem = driver.find_element_by_name("q")

# em seguida, estamos enviando teclas, mas é preciso limpar qualquer
# texto para não afetar o resultado.
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)


assert "No results found." not in driver.page_source
driver.close()
