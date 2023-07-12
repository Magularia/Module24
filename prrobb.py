import pytest
import time

from selenium.webdriver.common.by import By
from selenium import webdriver #подключение библиотеки

@pytest.fixture(autouse=True)
def driver():
   driver = webdriver.Chrome()
   # Переходим на страницу авторизации
   driver.get('https://petfriends.skillfactory.ru/login')

   yield driver

   driver.quit()


def test_search_example(driver):
    """ Поиск текста в google, далее делаем скриншот страницы. """

    # Открываем страницу для поиска:
    driver.get('https://google.com')

    time.sleep(10)  # небольшая задержка, чисто ради эксперимента

    # Поиск элемента для ввода текста:
    search_input = driver.find_element(By.NAME, 'q')

    # Очистка поля, далее ввод текста для поиска:
    search_input.clear()
    search_input.send_keys('second test')

    time.sleep(5)  # небольшая задержка, чисто ради эксперимента

    # Поиск элемента "кнопка", далее нажатие на кнопку:
    search_button = driver.find_element(By.NAME, "btnK")
    search_button.click()

    time.sleep(5)  # небольшая задержка, чисто ради эксперимента

    # Сохранение скриншота
    driver.save_screenshot('result.png')