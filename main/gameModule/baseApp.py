#Base Application File used for running entire Application
#Designed to run in the same fashion as Spring Framework in Java

import pygame
from configparser import ConfigParser
from events import EventManager
from controller import KeyboardController
from controller import CPUSpinnerController
from view import PygameView
from models import Game

def main():
    """main - main function calls all components and runs
       the program """
    print("Base Application Running")
    evManager = EventManager()
    keybd = KeyboardController(evManager)
    spinner = CPUSpinnerController(evManager)
    pygameView = PygameView(evManager)
    game = Game(evManager)

    spinner.Run()
    return 0

if __name__ == '__main__':
    main()
