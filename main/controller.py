"""controller.py - contains controller classes."""

import pygame
from events import TickEvent
from events import QuitEvent


class KeyboardController:
    """KeyboardController - controls keyboard functions."""

    def __init__(self, evManager):
        """Init - initialise keyboard controller."""
        self.evManager = evManager
        self.evManager.RegisterListener(self)

    def Notify(self, event):
        """Notify event type."""
        if isinstance(event, TickEvent):
            for event in pygame.event.get():
                ev = None
                if event.type == pygame.QUIT:
                    ev = QuitEvent()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    ev = QuitEvent()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
                    direction = DIRECTION_UP
                    ev = CharacterMoveRequest(direction)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
                    direction = DIRECTION_DOWN
                    ev = CharacterMoveRequest(direction)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    direction = DIRECTION_LEFT
                    ev = CharacterMoveRequest(direction)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    direction = DIRECTION_RIGHT
                    ev = CharacterMoveRequest(direction)

                if ev:
                    self.evManager.Post(ev)


class CPUSpinnerController:
    """CPUPSpinnerController - controls CPU ticks."""

    def __init__(self, evManager):
        """Init - initialise CPU Spinner controller."""
        self.evManager = evManager
        self.evManager.RegisterListener(self)
        self.keepGoing = 1

    def Run(self):
        """Run - keep ticking."""
        while self.keepGoing:
            event = TickEvent()
            self.evManager.Post(event)

    def Notify(self, event):
        """Notify - kill program."""
        if isinstance(event, QuitEvent):
            #This will kill the loop
            self.keepGoing = 0
