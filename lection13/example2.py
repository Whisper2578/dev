from atf.ui import *
from controls import *


class CreateTaskBad(Region):

    add_button = ControlsButton()
    popup = ControlsPopup()

    def create_task(self):

        self.add_button.click()
        self.popup.select('Задача')


class CreateTaskGood(Region):

    add_button = ExtControlsDropdownAddButton()

    def create_task(self):

        self.add_button.select('Задача')
