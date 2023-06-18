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
    task_info = Element(By.CSS_SELECTOR, '[name="wrapper"]', 'Номер')
    task_target = Element(By.CSS_SELECTOR, '.controls-StackTemplate__content-area', 'Данные задачи')


class InboxMenu(Region):
    inbox_task = CustomList(By.CSS_SELECTOR, '.ws-flex-nowrap', 'Входящие')
    highlighted_marker = Element(By.CSS_SELECTOR, '.controls-StickyBlock__content', 'Маркер выделения')
    marker_red = Element(By.CSS_SELECTOR, '[data-qa="marker"].controls-ListView__baseline_font-size', 'Маркер')
    task_list = CustomList(By.CSS_SELECTOR, '[data-qa="list"].controls-air-m', 'Список задач')
    plus_button = Button(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"] span', 'Плюс')
    plus_button_menu = CustomList(By.CSS_SELECTOR, '.controls-Menu__content_baseline', 'Создать')
    name = TextField(By.CSS_SELECTOR, '.controls-InputBase__nativeField_caretFilled', 'Имя папки')
    folder = TextField(By.CSS_SELECTOR, '[data-qa="hint-Template__imageWrapper"]', 'Задачи0')
    del_folder = Button(By.CSS_SELECTOR, '.icon-Erase', 'Удалить')
    confirm_body = CustomList(By.CSS_SELECTOR, '.controls-ConfirmationTemplate__body', 'Потверждение')
    confirm = Button(By.CSS_SELECTOR, '[data-qa="controls-ConfirmationDialog__button-true"] .controls-BaseButton__wrapper','ДА')


class TestLection12(TestCaseUI):

    def test_task_1(self):
        """
        Авторизоваться на сайте https://fix-online.sbis.ru/
        Перейти в реестр Контакты
        Отправить сообщение самому себе
        Убедиться, что сообщение появилось в реестре
        Удалить это сообщение и убедиться, что удалили
        """
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
        """
        Авторизоваться на сайте https://fix-online.sbis.ru/
        Перейти в реестр Задачи на вкладку "В работе"
        Убедиться, что выделена папка "Входящие" и стоит маркер.
        Убедиться, что папка не пустая (в реестре есть задачи)
        Перейти в другую папку, убедиться, что теперь она выделена, а со "Входящие" выделение снято
        Создать новую папку и перейти в неё
        Убедиться, что она пустая
        Удалить новую папку, проверить, что её нет в списке папок
        """
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
        inbox_menu = InboxMenu(self.driver)
        inbox_menu.inbox_task.item(1).should_be(ExactText('Входящие'))
        inbox_menu.inbox_task.item(1).element(inbox_menu.highlighted_marker.should_be(Enabled))
        inbox_menu.inbox_task.item(1).element(inbox_menu.marker_red.should_be(Enabled))

        log('Убедиться, что папка не пустая (в реестре есть задачи)')
        inbox_menu.task_list.should_be(Visible)

        log('Перейти в другую папку, убедиться, что теперь она выделена, а со "Входящие" выделение снято)')
        inbox_menu.inbox_task.item(2).mouse_click()
        inbox_menu.inbox_task.item(2).element(inbox_menu.highlighted_marker.should_be(Enabled))
        inbox_menu.inbox_task.item(1).should_not_be(CssClass(inbox_menu.highlighted_marker))
        inbox_menu.folder.should_be(Visible)

        log('Создать новую папку и перейти в неё')
        inbox_menu.inbox_task.item(1).mouse_click()
        inbox_menu.plus_button.mouse_click()
        inbox_menu.plus_button_menu.item(2).mouse_click()
        inbox_menu.name.should_be(Visible)
        inbox_menu.name.type_in(' Новая Папка' + Keys.CONTROL + Keys.ENTER)
        inbox_menu.inbox_task.item(3).mouse_click()

        log('Убедиться, что она пустая')
        inbox_menu.folder.should_be(Visible)

        log('Удалить новую папку, проверить, что её нет в списке папок')
        inbox_menu.inbox_task.item(3).context_click()
        inbox_menu.del_folder.mouse_click()
        inbox_menu.confirm_body.should_be(Visible)
        inbox_menu.confirm.mouse_click()
        inbox_menu.inbox_task.item(3).should_not_be(Visible)

    def test_task_3(self):
        """
        Предварительные действия: Создайте эталонную задачу, заполнив обязательные поля
        Авторизоваться на сайте https://fix-online.sbis.ru/
        Откройте эталонную задачу по прямой ссылке в новом окне
        Убедитесь, что в заголовке вкладки отображается "Задача №НОМЕР от ДАТА", где ДАТА и НОМЕР - это ваши эталонные значения
        Проверьте, что поля: Исполнитель, дата, номер, описание и автор отображаются с эталонными значениями
        """
        sbis_site = self.config.get('SBIS_SITE')
        etalon_task = self.config.get('ETALON_TASK')
        number = '5'
        date = '15 июн, чт'
        executor = 'Секретарёв Т.Т.'
        description = 'Подготовить back-код к ревью.'
        autor = 'Админов А.А.'

        self.browser.open(sbis_site)
        log('Авторизоваться на сайте')
        user_login, user_password = self.config.get('USER_LOGIN'), self.config.get('USER_PASSWORD')
        auth_page = AuthPage(self.driver)
        auth_page.login.type_in(user_login + Keys.ENTER)
        auth_page.login.should_be(ExactText(user_login))
        auth_page.password.type_in(user_password + Keys.ENTER)

        main_page_online = MainPageOnline(self.driver)
        main_page_online.contacts_menu.should_be(Visible)

        log('Откройте эталонную задачу по прямой ссылке в новом окне')
        self.browser.create_new_tab(etalon_task)
        self.browser.switch_to_opened_window()

        log('Убедитесь, что в заголовке вкладки отображается "Задача №НОМЕР от ДАТА", где ДАТА и НОМЕР - это ваши эталонные значения')
        task_menu = TaskMenu(self.driver)
        task_menu.task_info.should_be(ExactText(f'Задача\n{date}\n№\n{number}'))

        log('Проверьте, что поля: Исполнитель, дата, номер, описание и автор отображаются с эталонными значениями')
        task_menu.task_target.should_be(ContainsText(executor), ContainsText(date), ContainsText(description), ContainsText(number), ContainsText(autor))
