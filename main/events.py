##events.py - used to hold event classes
import pygame
import extras

DIRECTION_UP = 0
DIRECTION_DOWN = 1
DIRECTION_LEFT = 2
DIRECTION_RIGHT = 3

class Event:
    """Event - superclass defines events that any objects that maybe
    called by the event manager"""
    def __init__(self):
        self.name = 'Generic Event'

class TickEvent(Event):
    """TickEvent - manage tick events while the program runs"""
    def __init__(self):
        self.name = 'CPU Tick Event'

class QuitEvent(Event):
    """QuitEvent - manage quit events"""
    def __init__(self):
        self.name = 'Program Quit Event'

class MapBuiltEvent(Event):
    """MapBuiltEvent - map building event"""
    def __init__(self, map):
        self.name = 'Map Built Event'
        self.map = map

class GameStartedEvent(Event):
    """GameStartedEvent - game starting event"""
    def __init__(self,game):
        self.name = 'Game Started Event'
        self.game = game

class CharacterMoveRequest(Event):
    def __init__(self,direction):
        self.name = 'Character Move Request'
        self.direction = direction

class CharacterPlaceEvent(Event):
    """CharacterPlaceRequest - Place Character - don't move from adjacent sector"""
    def __init__(self,character):
        self.name = 'Character Place Event'
        self.character = character

class CharacterMoveEvent(Event):
    def __init__(self,character):
        self.name = 'Character Move Event'
        self.character = character
#==============================================================================#
class EventManager:
    """
    This class is responsible for co-oridnating events across the mvc.
    """
    def __init__(self):
        from weakref import WeakKeyDictionary
        self.listeners = WeakKeyDictionary()
        self.eventQueue = []

    def RegisterListener(self, listener):
        self.listeners[listener] = 1

    def UnregisterListener(self, listener):
        if listener in self.listeners.keys():
            del self.listeners[listener]

    def Post(self,event):
        if not isinstance(event, TickEvent):
            Debug(event.name)
        for listener in self.listeners.keys():
            listener.Notify(event)
