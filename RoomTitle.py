import pygame
import pygame.surface
import pygame.event
from pygame.locals import *
from iced.room import Room, RoomManager
from iced.game_object import Object
from iced.functions import *
from iced.instance import Instance
from Text import Text

pygame.init()

# TODO: the method do when continue text was clicked
def switch_continue():
    print("switch")

# TODO: the method do when new game text was clicked
def switch_new_game():
    print("new game")

# TODO: the method do when option text was clicked
def switch_option():
    print("option")

# TODO: the method do when new game text was clicked
def switch_rules():
    print("rules")

# TODO: the method do when new game text was clicked
def switch_exit():
    pygame.event.Event(QUIT)


class ContinueText(Text):
    def __init__(self):
        super().__init__()
        self.created = False

    def loop(self):
        if not self.created:
            self.create("Continue", 200, 70, 60, (0, 0, 0), (230, 230, 230))
            self.created = True
        if is_mouse_left_down(self):
            switch_continue()

class NewGameText(Text):
    def __init__(self):
        super().__init__()
        self.created = False

    def loop(self):
        if not self.created:
            self.create("New Game", 200, 70, 60, (0, 0, 0), (230, 230, 230))
            self.created = True
        if is_mouse_left_down(self):
            switch_new_game()

class OptionText(Text):
    def __init__(self):
        super().__init__()
        self.created = False

    def loop(self):
        if not self.created:
            self.create("Option", 200, 70, 60, (0, 0, 0), (230, 230, 230))
            self.created = True
        if is_mouse_left_down(self):
            switch_option()

class RulesText(Text):
    def __init__(self):
        super().__init__()
        self.created = False

    def loop(self):
        if not self.created:
            self.create("Rules", 200, 70, 60, (0, 0, 0), (230, 230, 230))
            self.created = True
        if is_mouse_left_down(self):
            switch_rules()

class ExitText(Text):
    def __init__(self):
        super().__init__()
        self.created = False

    def loop(self):
        if not self.created:
            self.create("Exit", 200, 70, 60, (0, 0, 0), (230, 230, 230))
            self.created = True
        if is_mouse_left_down(self):
            switch_exit()

text_title = Text()
text_title.create("Energy Game", 300, 70, 80, (0, 0, 0), (230, 230, 230))

text_continue = ContinueText()
text_new_game = NewGameText()
text_option = OptionText()
text_rules = RulesText()
text_exit = ExitText()

inst_text_title = Instance()
inst_text_continue = Instance()
inst_text_new_game = Instance()
inst_text_option = Instance()
inst_text_rules = Instance()
inst_text_exit = Instance()

inst_text_title.create(text_title, 375, 40)
inst_text_continue.create(text_continue, 425, 180)
inst_text_new_game.create(text_new_game, 425, 280)
inst_text_option.create(text_option, 425, 380)
inst_text_rules.create(text_rules, 425, 480)
inst_text_exit.create(text_exit, 425, 580)

room_title = Room()
room_title.add_instance(inst_text_title)
room_title.add_instance(inst_text_continue)
room_title.add_instance(inst_text_new_game)
room_title.add_instance(inst_text_option)
room_title.add_instance(inst_text_rules)
room_title.add_instance(inst_text_exit)

bgTitle = pygame.surface.Surface((1024, 688))
bgTitle.fill((230, 230, 230))
room_title.set_background(bgTitle)

RoomManager.add(room_title)
