from atf.ui import *
from controls import *


class ContactsRegistry(Region):
    """Реестр контактов"""

    message_folders = ControlsTreeGridView(By.CSS_SELECTOR, '[name="grid"]', 'Папка сообщений')
    messages = ControlsListView(By.CSS_SELECTOR, '[data-qa="list"].Hint-ListWrapper_list', 'Сообщения')
    context_menu = ControlsPopup(By.CSS_SELECTOR, '.controls-Menu__popup-template', 'Контекстное меню')
    to_move = ControlsTreeGridView(By.CSS_SELECTOR, '[data-qa="list"].controls-Explorer__view', 'Куда переместить')
    bookmarks = ControlsTabsButtons(By.CSS_SELECTOR, '[name="wrapper"]', 'Закладки')
    chats = ControlsListView(By.CSS_SELECTOR, '.msg-CorrespondenceMaster', 'Чаты')
    tags_folder = ControlsListView(By.CSS_SELECTOR, '.tags-list', 'Папка для тэгов')
    chat_list = ControlsListView(By.CSS_SELECTOR, '[name="scrollWrapper"] [name="userContent"]', 'Список сообщений')
    select_marker = ControlsListView(By.CSS_SELECTOR, '.msg-tags-aggregate__scrollContainer', 'Выбор маркера')


    def check_load(self):
        """Проверка загрузки реестра"""

        self.message_folders.check_load()
        self.messages.check_load()
