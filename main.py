import time
from selenium.webdriver.common.by import By
# Создать файл settings.py с двумя параметрами:
# valid_email = "ваше мыло"
# valid_password = "ваш логин"
from settings import valid_email, valid_password


def test_petfriends(web_browser):
    # Open PetFriends base page:
    web_browser.get("https://petfriends.skillfactory.ru/")

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

    # click on the new user button
    btn_newuser = web_browser.find_element(By.XPATH, "//button[@onclick=\"document.location='/new_user';\"]")
    btn_newuser.click()

    # нажатие на кнопку - у меня уже есть аккаунт
    btn_exist_acc = web_browser.find_element(By.PARTIAL_LINK_TEXT, u"У меня уже есть аккаунт")
    btn_exist_acc.click()

    # add email
    field_email = web_browser.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys(valid_email)

    # add password
    field_pass = web_browser.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys(valid_password)
# click submit button
    btn_submit = web_browser.find_element(By.XPATH, "//button[@type='submit']")
    btn_submit.click()

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

    assert web_browser.current_url == 'https://petfriends.skillfactory.ru/all_pets', "login error"


# pytest -v --driver Chrome --driver-path /Users/deniszutaev/PycharmProjects/Skillfactory/chromedriver_mac_arm64/chromedriver test_selenium_petfriends.py