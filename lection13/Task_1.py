from atf import *
from atf.ui import *
from pages.auth_page import AuthPage
from pages.task_page import ContactsRegistry


class TestRegistryTask(TestCaseUI):

    @classmethod
    def setUpClass(cls):
        AuthPage(cls.driver).auth(cls.config.get('USER_LOGIN'), cls.config.get('USER_PASSWORD'))
        cls.page = ContactsRegistry(cls.driver)

    def setUp(self):
        self.page.check_load()

    def test_move_task(self):
        log('Переместить запись в другую папку и проверить перемещение (убедиться в: наличии в папке и увеличении '
            'счётчика). И вернуть обратно.')
        letter_count = self.page.message_folders.item(contains_text='Папка для перемещения').text.split('\n')[-1]
        if letter_count.isdigit():
            letter_count = int(letter_count)
        else:
            letter_count = 0
        delay(1)
        self.page.messages.item(contains_text='Сообщение для перемещения').context_click()
        self.page.context_menu.select('Переместить')
        self.page.to_move.row(contains_text='Папка для перемещения').click()
        delay(1)
        assert letter_count + 1 == int(self.page.message_folders.item(contains_text='Папка для перемещения').text.split('\n')[-1]), \
            'Количество писем не совпадает'
        self.page.message_folders.item(contains_text='Папка для перемещения').click()
        delay(1)
        self.page.messages.item(contains_text='Сообщение для перемещения').context_click()
        self.page.context_menu.select('Переместить')
        self.page.to_move.row(contains_text='Все сообщения').click()
        self.page.message_folders.item(contains_text='Все сообщения').click()
        delay(2)

    def test_check_date(self):
        log('Проверить, что дата сообщения в реестре Диалоги совпадает с датой в Чатах')
        delay(1)
        message = self.page.messages.item(contains_text='Сообщение для перемещения')
        message_date = message.text.split('\n')[-3]
        self.page.bookmarks.select('Чаты')
        self.page.chats.item(contains_text='Сообщение для перемещения').click()
        delay(1)
        assert self.page.chat_list.item(contains_text='Сообщение для перемещения').text.split('\n')[-3] == message_date, \
            'Дата отличается'
        self.page.bookmarks.select('Диалоги')
        delay(2)

    def test_check_tag(self):
        log('Пометить сообщение эталонным тегом. Убедиться, что тег появился на сообщении, а счётчик тегов увеличился. '
            'Снять тег и проверить.')
        tag_message_count = self.page.tags_folder.item(contains_text='Эталонный тэг').text.split('\n')[-1]
        if tag_message_count.isdigit():
            tag_message_count = int(tag_message_count)
        else:
            tag_message_count = 0
        self.page.messages.item(contains_text='Сообщение для перемещения').context_click()
        self.page.context_menu.select('Пометить')
        self.page.select_marker.item(contains_text='Эталонный тэг').click()
        delay(1)
        assert tag_message_count + 1 == int(self.page.tags_folder.item(contains_text='Эталонный тэг').text.split('\n')[-1]), \
            'Счётчик не изменился'
        self.page.messages.item(contains_text='Сообщение для перемещения').context_click()
        self.page.context_menu.select('Пометить')
        self.page.select_marker.item(contains_text='Эталонный тэг').click()

