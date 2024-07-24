# Selenium - Automatizando tarefas no navegador
from pathlib import Path
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/
# Doc Selenium
# https://selenium-python.readthedocs.io/locating-elements.html


# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver.exe'


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':
    TIME_TO_WAIT = 10
    DELAY = 0.5

    # Example
    # options = '--headless', '--disable-gpu',
    options = ()
    browser = make_chrome_browser(*options)


    browser.get('http://localhost/tela_login/public/login.php')


    time.sleep(1)  # Adiciona uma pausa de 1 segundo
    # Espere para encontrar o input
    email_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'email')
        )
    )
    email_input.click()
    time.sleep(DELAY)
    email_input.send_keys('rafael.costa@email.com') #digitar dentro do campo input
    time.sleep(DELAY)
    email_input.send_keys(Keys.ENTER) #enviar teclas


    pass_input = browser.find_element(By.NAME, 'senha')
    time.sleep(DELAY)
    pass_input.send_keys('123')
    time.sleep(DELAY)
    pass_input.send_keys(Keys.ENTER) #enviar teclas
    time.sleep(DELAY)
    adm_link = browser.find_element(By.ID, 'access')
    time.sleep(DELAY)
    adm_link.click()
    time.sleep(DELAY)
    exit_link = browser.find_element(By.ID, 'logout')
    time.sleep(DELAY)
    exit_link.click()

    # Dorme por 10 segundos
    time.sleep(TIME_TO_WAIT)