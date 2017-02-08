"""baseApp module - all classes are initialised here."""

from events import EventManager
from controller import KeyboardController
from controller import CPUSpinnerController
from view import PygameView
from models import Game


def Main():
    """main - main function calls all components and run the program."""
    print("Base Application Running")
    evManager = EventManager()
    keybd = KeyboardController(evManager)
    spinner = CPUSpinnerController(evManager)
    pygameView = PygameView(evManager)
    game = Game(evManager)

    spinner.Run()


if __name__ == '__main__':
    Main()
