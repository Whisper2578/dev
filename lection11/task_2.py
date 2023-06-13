# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from time import sleep

fix_online = 'https://fix-online.sbis.ru/'
message_xpath = '//p[contains(text(),"Привет!")]'
driver = webdriver.Chrome()
try:
    print('Входим на сайт https://fix-online.sbis.ru/')
    driver.get(fix_online)

    print('Вводим логин')
    sleep(2)
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys('edi_antonov_secretary', Keys.ENTER)

    print('Вводим пароль')
    sleep(2)
    assert login.get_attribute('value') == 'edi_antonov_secretary'
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys('09876qwE', Keys.ENTER)

    print('Открываем меню "Контакты"')
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, '[name="item-contacts"]').click()

    print('Выбираем пункт "Контакты"')
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle.NavigationPanels-SubMenu__title-with-separator').click()

    print('Открываем меню отправки сообщений')
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, '.icon-RoundPlus').click()

    print('Выбираем контакт')
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, '.controls-text-label.ws-align-self-center').click()

    print('Находим себя в списке контактов')
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, '[title="Секретарёв Тестер"]').click()

    print('Пишем и отправляем сообщение')
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, '[data-slate-node="element"]').send_keys('Привет!', Keys.CONTROL + Keys.ENTER)

    print('Проверяем, что наше сообщение есть в реестре сообщений')
    sleep(2)
    assert driver.find_element(By.XPATH, message_xpath)

    print('Открываем наше сообщение')
    sleep(2)
    driver.find_element(By.XPATH, message_xpath).click()

    print('Удаляем наше сообщение')
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, '.controls-Toolbar_content.controls-Toolbar_content-vertical > div[title="Удалить"]').click()

    print('Проверяем что наше сообщение отсутствует в реестре сообщений')
    sleep(2)
    assert driver.find_element(By.XPATH, message_xpath), 'Сообщения нет в списке'

    print('Тест успешно пройден')
    sleep(5)

finally:
    driver.quit()