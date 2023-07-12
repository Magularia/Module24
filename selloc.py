import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def driver():
   driver = webdriver.Chrome()
   # Переходим на страницу авторизации
   driver.get('https://petfriends.skillfactory.ru/login')

   yield driver

   driver.quit()

from selenium.webdriver.common.by import By

def test_show_my_pets(driver):
   # Вводим email
   driver.find_element(By.ID, 'email').send_keys('mag1@mail.ru')
   # Вводим пароль
   driver.find_element(By.ID, 'pass').send_keys('30052023N')
   # Нажимаем на кнопку входа в аккаунт
   driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"