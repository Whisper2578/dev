from atf import *
from atf.ui import *
from pages.auth_page import AuthPage
from pages.task_page import TaskRegistry


class TestRegistryTask(TestCaseUI):

    @classmethod
    def setUpClass(cls):
        AuthPage(cls.driver).auth(cls.config.get('USER_LOGIN'), cls.config.get('USER_PASSWORD'))
        cls.page = TaskRegistry(cls.driver)

    def setUp(self):
        self.page.check_load()

    def test_01_check_task(self):

        log('Перейти в папку. Проверить количество задач в папке')
        self.page.folders.row(contains_text='Папка 1').click()
        self.page.tasks.check_rows_number(1)

        log('Раскрыть папку')
        self.page.folders.row(contains_text='Папка 2').expand_folder()
        self.page.folders.should_be(ContainsText('папка 3'))

    def test_02_search(self):

        task = 'тестовая задача для тестовой зоны'

        log('Поиск задачи')
        self.page.search_task(task)
        self.page.tasks.find_cell_by_column_number(task, 5).should_be(ContainsText('29.09.15'))

        log('Открыть задачу в новой вкладке')
        action = lambda: self.page.tasks.row(contains_text=task).select_menu_actions('Открыть в новой вкладке')
        self.browser.switch_to_new_window(action)

    def test_03_select(self):

        log('Отметить первые 3 задачи в реестре')
        for row in range(1, 4):
            self.page.tasks.row(row).select()

        log('Снять выделение задач')
        for row in range(1, 4):
            self.page.tasks.row(row).unselect()

    def test_04_delete_folder(self):

        folder = 'test_grid'

        log('Удалить папку')
        self.page.folders.row(contains_text=folder).select_menu_actions('Удалить папку')
        self.page.popup_confirmation.confirm()
        self.page.folders.should_not_be(ContainsText(folder))

    def test_05_check_tab(self):

        log('Переключиться на вкладку')
        self.page.select_tab('На контроле')

