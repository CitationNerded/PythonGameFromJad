#Controller
import pygame
import events

class KeyboardController:
    """KeyboardController - controls keyboard functions """
    def __init__(self,evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)

    def Notify(self, event):
        """ notify event type"""
        if isinstance(event, TickEvent):
            for event in pygame.event.get():
                ev = None
                if event.type == pygame.QUIT:
                    ev = QuitEvent()
                elif event.type == pygame.KEYDOWN and event.key == K_ESCAPE:
                    ev = QuitEvent()
                elif event.type == KEYDOWN and event.key = K_UP:
                    direction = DIRECTION_UP
                    ev = CharacterMoveRequest(direction)
                elif event.type == KEYDOWN and event.key = K_DOWN:
                    direction = DIRECTION_DOWN
                    ev = CharacterMoveRequest(direction)
                elif event.type == KEYDOWN and event.key = K_LEFT:
                    direction = DIRECTION_LEFT
                    ev = CharacterMoveRequest(direction)
                elif event.type == KEYDOWN and event.key = K_RIGHT:
                    direction = DIRECTION_RIGHT
                    ev = CharacterMoveRequest(direction)

                if ev:
                    self.evManager.Post(ev)

class CPUSpinnerController:
    """CPUPSpinnerController - controls CPU ticks"""
