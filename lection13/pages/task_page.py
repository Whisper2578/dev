from atf.ui import *
from controls import *


class TaskRegistry(Region):
    """Реестр Задач"""

    folders = ControlsTreeGridView(By.CSS_SELECTOR, '.controls-MasterDetail_master .controls-Grid', 'Папки')
    tasks = ControlsTreeGridView(By.CSS_SELECTOR, '.brTasksOnMe .controls-Grid', 'Задачи в работе')
    task_ctrl = ControlsTreeGridView(By.CSS_SELECTOR, '.brTasksCtrl .controls-Grid', 'Задачи на контроле')
    search = ControlsSearchInput()
    tabs = ControlsTabsButtons()

    def check_load(self):
        """Проверка загрузки реестра"""

        self.folders.check_load()
        self.tasks.check_load()

    def search_task(self, task):
        """Поиск задачи"""

        self.search.search(task, search_btn_click=True)
        self.tasks.row(contains_text=task).should_be(Displayed)

    def select_tab(self, tab):
        """Переключение по вкладкам"""

        self.tabs.select(tab)
        self.task_ctrl.check_load()
