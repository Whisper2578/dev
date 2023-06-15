# Создайте свой репозиторий (проект) на https://git.sbis.ru/ и на проверку теперь присылайте MR в свой репозиторий.

# Задание №1
# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

# Задание №2
# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Задачи на вкладку "В работе"
# Убедиться, что выделена папка "Входящие" и стоит маркер.
# Убедиться, что папка не пустая (в реестре есть задачи)
# Перейти в другую папку, убедиться, что теперь она выделена, а со "Входящие" выделение снято
# Создать новую папку и перейти в неё
# Убедиться, что она пустая
# Удалить новую папку, проверить, что её нет в списке папок
# Для сдачи задания пришлите код и запись с экрана прохождения теста

# Задание №3
# Предварительные действия (Создайте эталонную задачу, заполнив обязательные поля)
# Авторизоваться на сайте https://fix-online.sbis.ru/
# Откройте эталонную задачу по прямой ссылке в новом окне
# Убедитесь, что в заголовке вкладки отображается "Задача №НОМЕР от ДАТА",
# где ДАТА и НОМЕР - это ваши эталонные значения
# Проверьте, что поля: Исполнитель, дата, номер, описание и автор отображаются с эталонными значениями
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from atf import log
from atf.ui import *


class AuthPage(Region):
    login = TextField(By.CSS_SELECTOR, '[name="Login"]', 'логин')
    password = TextField(By.CSS_SELECTOR, '[name="Password"]', 'пароль')


class MainPageOnline(Region):
    contacts_menu = Button(By.CSS_SELECTOR, '[name="item-contacts"]', 'Меню контактов')
    contacts_submenu = Button(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle', 'Пункт контактов')


class MessageSend(Region):
    send_message = Button(By.CSS_SELECTOR, '.icon-RoundPlus', 'Отправка сообщения')
    choose_contact = Element(By.CSS_SELECTOR, '.controls-text-label.ws-align-self-center', 'Выбор контакта')
    destination_name = Element(By.CSS_SELECTOR, '[title="Секретарёв Тестер"]', 'Имя адресата')
    message_field = Element(By.CSS_SELECTOR, '.textEditor_Viewer__Paragraph', 'Поле ввода')
    message_text = "Привет!"


class MessageCheckDel(Region):
    message_list = CustomList(By.CSS_SELECTOR, '.msg-dialogs-detail__list', 'Реестр сообщений')
    open_message = Element(By.XPATH, '//p[contains(text(),MessageSend.message_text)]', 'Открыть сообщение')
    del_message = Button(By.CSS_SELECTOR, '.controls-Toolbar__item:nth-of-type(6) [tabindex] [tabindex]',
                         'Удалить сообщение')


class TaskMenu(Region):
    task_button = Button(By.XPATH, "//span[contains(text(),'Задачи')]", 'Задачи')
    task4me_button = Button(By.XPATH, "//span[contains(text(),'Задачи на мне')]", 'Задачи на мне')
    task4me_inprogress = Button(By.CSS_SELECTOR, '[title="В работе"]', 'В работе')
    inbox_tasks = Element(By.CSS_SELECTOR, '.controls-fontsize-l.controls-StickyBlock__content', 'Входящие')
    inbox_counter = Element(By.CSS_SELECTOR, "div[title='Входящие']  .controls-EditorList__additional-column.controls-fontsize-m.controls-text-label", 'Счётчик задач')



class TestLection12(TestCaseUI):

    def test_task_1(self):
        sbis_site = self.config.get('SBIS_SITE')

        self.browser.open(sbis_site)
        log('Авторизация')
        user_login, user_password = self.config.get('USER_LOGIN'), self.config.get('USER_PASSWORD')
        auth_page = AuthPage(self.driver)
        auth_page.login.type_in(user_login + Keys.ENTER)
        auth_page.login.should_be(ExactText(user_login))
        auth_page.password.type_in(user_password + Keys.ENTER)

        log('Открываем список контактов')
        main_page_online = MainPageOnline(self.driver)
        main_page_online.contacts_menu.scroll_into_view().click()
        main_page_online.contacts_submenu.click()

        log('Выбираем контакт')
        message_send = MessageSend(self.driver)
        message_send.send_message.click()
        message_send.choose_contact.click()

        log('Находим себя в списке контактов')
        message_send.destination_name.click()

        log('Ввод текста и отправка сообщения')
        message_send.message_field.type_in(MessageSend.message_text + Keys.CONTROL + Keys.ENTER)

        log('Проверяем, что наше сообщение есть в реестре сообщений')
        message_check_del = MessageCheckDel(self.driver)
        message_check_del.message_list.should_be(ContainsText(MessageSend.message_text))

        log('Открываем наше сообщение')
        message_check_del.open_message.click()

        log('Удаляем наше сообщение')
        message_check_del.del_message.mouse_click()

        log('Проверяем, что нашего сообщения нет в реестре сообщений')
        message_check_del.message_list.should_not_be(ContainsText(MessageSend.message_text))

    def test_task_2(self):
        sbis_site = self.config.get('SBIS_SITE')

        self.browser.open(sbis_site)
        log('Авторизоваться на сайте')
        user_login, user_password = self.config.get('USER_LOGIN'), self.config.get('USER_PASSWORD')
        auth_page = AuthPage(self.driver)
        auth_page.login.type_in(user_login + Keys.ENTER)
        auth_page.login.should_be(ExactText(user_login))
        auth_page.password.type_in(user_password + Keys.ENTER)

        log('Перейти в реестр Задачи на вкладку "В работе"')
        task_menu = TaskMenu(self.driver)
        task_menu.task_button.click()
        task_menu.task4me_button.click()
        task_menu.task4me_inprogress.click()

        log('Убедиться, что выделена папка "Входящие" и стоит маркер')
        task_menu.inbox_tasks.should_be(ContainsText('controls-StickyBlock__content'))

        log('Убедиться, что папка не пустая (в реестре есть задачи)')
        task_menu.inbox_tasks.should_be(Visible)
        #
        #
        #
        # log('Перейти в другую папку, убедиться, что теперь она выделена, а со "Входящие" выделение снято')
        #
        #
        #
        # log('Создать новую папку и перейти в неё')
        #
        #
        #
        # log('Убедиться, что она пустая')
        #
        #
        #
        # log('Удалить новую папку, проверить, что её нет в списке папок')



