from iced.game import Game
from iced.settings import settings
from RoomTitle import room_title

settings.window.size = (1024, 688)

my_game = Game()
my_game.main(room_title)