# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep

sbis_site = 'https://sbis.ru/'
sbis_title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'
tensor_about = 'https://tensor.ru/about'
driver = webdriver.Chrome()
try:
    driver.get(sbis_site)
    driver.maximize_window()
    sleep(1)
    assert driver.current_url == sbis_site, 'Открыт не верный сайт'
    assert driver.title == sbis_title, 'Заголовок сайта не соответствует шаблону'

    sleep(1)
    contacts_btn = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item-1')
    assert contacts_btn.is_displayed(), 'Исследуемая кнопка не отображается на странице'
    assert contacts_btn.text == 'Контакты', 'Текст кнопки отличается от шаблона'
    contacts_btn.click()

    sleep(1)
    tensor_banner = driver.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor')
    assert tensor_banner.get_attribute('title') == 'tensor.ru', 'Заголовок баннера отличается от шаблона'
    assert tensor_banner.is_displayed(), 'Исследуемый баннер не отображается на странице'
    tensor_banner.click()

    sleep(1)
    driver.switch_to.window(driver.window_handles[1])
    strength_in_people = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content.tensor_ru-Index__card')

    sleep(2)
    ActionChains(driver).scroll_to_element(strength_in_people).perform()

    sleep(2)
    assert strength_in_people.is_displayed(), 'Исследуемая новость не отображается на странице'
    assert 'Сила в людях' in str(strength_in_people.get_attribute('textContent')), 'Искомый текст не найден в блоке'

    sleep(1)
    sip_more = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content.tensor_ru-Index__card p a')
    assert sip_more.is_displayed()
    assert sip_more.text == 'Подробнее', 'Текст ссылки подробностей отличается от шаблона'
    sip_more.click()

    assert driver.current_url == tensor_about, 'Выполнено перенаправление на неверный URL-адрес'

    sleep(3)
    print('Тест успешно пройден')

finally:
    driver.quit()