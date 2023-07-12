import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from settings import valid_email, valid_password, user_name


@pytest.fixture(autouse=True)
def browser():
   driver = webdriver.Chrome()
   # Переходим на страницу авторизации
   driver.get('https://petfriends.skillfactory.ru/login')

   yield driver

   driver.close()

def test_show_my_pets(browser):
    # Вводим email
    browser.find_element(By.ID, 'email').send_keys('mag1@mail.ru')

    # Вводим пароль
    browser.find_element(By.ID, 'pass').send_keys('30052023N')

    # Нажимаем на кнопку входа в аккаунт
    submit_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[type="submit"]')))
    submit_button.click()

    # Проверяем, что мы оказались на главной странице пользователя
    assert browser.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    # Нажимаем на кнопку Мои питомцы
    submit_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'nav-link')))
    submit_button.click()

    # Проверяем, что мы оказались на главной странице пользователя
    assert browser.find_element(By.TAG_NAME, 'h2').text == user_name

    # Забираем цифру количества питомцев из статистики пользователя
    pet_info = browser.find_element(By.CSS_SELECTOR, 'div.left:nth-child(1)').text.split('\n')[1]
    number_of_pets = int("".join(filter(str.isdigit, pet_info)))

    # Проверяем, что количество строк таблицы соответствует количеству питомцев в блоке статистики пользователя
    assert len(browser.find_elements(By.CSS_SELECTOR, 'tbody tr')) == number_of_pets

    images = browser.find_elements(By.CSS_SELECTOR, 'tr th[scope=row] img')
    names = browser.find_elements(By.CSS_SELECTOR, 'td:nth-child(2)')
    descriptions = browser.find_elements(By.CSS_SELECTOR, 'td:nth-child(3)')
    age = browser.find_elements(By.CSS_SELECTOR, 'td:nth-child(4)')
    print(names)

    num_photos_pets = 0
    count_names = len(names)
    name_list = []
    age_list = []
    descriptions_list = []

    for i in range(count_names):
        assert names[i].text != ''
        name_list.append(names[i].text)
        if images[i].get_attribute('src'):
            num_photos_pets += 1
        assert descriptions[i].text != ''
        descriptions_list.append(descriptions[i].text)
        assert age[i].text != ''
        age_list.append(age[i].text)
        assert 0 <= int(age[i].text) < 100
        assert 0 < len(names[i].text) < 255
        assert 0 < len(descriptions[i].text) < 255

    # Проверка уникальности имен, возроста, породы
    assert len(name_list) == len(set(name_list))
    assert len(age_list) == len(set(age_list))
    assert len(descriptions_list) == len(set(descriptions_list))

    # Проверка, что хотя бы у половины питомцев есть фото (используестя тип данных float для сравнения)
    assert count_names / 2 <= float(num_photos_pets)