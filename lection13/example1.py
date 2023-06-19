from atf.ui import *
from controls import *


class TaskRegistryBad(Region):
    """Реестр Задачи"""

    tasks = CustomList(By.CSS_SELECTOR, '.controls-MasterDetail_details .controls-Grid__row', 'Задачи')
    settings = CustomList(By.CSS_SELECTOR, '.controls-Menu__row', 'Опции')
    settings_css = '.icon-SettingsNew'

    def select_setting(self, task: str, setting: str):
        """Выбор операции над записью"""

        task_item = self.tasks.item(contains_text=task)
        task_item.mouse_over()
        task_item.element(self.settings_css).click()
        self.settings.item(contains_text=setting).click()


class TaskRegistryGood(Region):
    """Реестр Задачи"""

    tasks = ControlsTreeGridView()

    def select_setting(self, task: str, setting: str):
        """Выбор операции над записью"""

        self.tasks.row(contains_text=task).select_menu_actions(setting)
