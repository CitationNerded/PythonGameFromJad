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
            print("NAME: %s" %(event.name))
        for listener in self.listeners.keys():
            listener.Notify(event)


class Game:
    """Game Class - model that looks after the Game"""
    STATE_PREPARING = 0
    STATE_RUNNING = 1
    STATE_PAUSED = 2

    def __init__(self, evMananger):
        self.evMananger = evMananger
        self.evMananger.RegisterListener(self)

        self.state = Game.STATE_PREPARING

        self.players = [Player(evMananger)]
        self.map = Map(evMananger)

    def Start(self):
        self.map.Build()
        self.state = Game.STATE_RUNNING
        ev = GameStartedEvent(self)
        self.evMananger.Post(ev)

    def Notify(self,event):
        if isinstance(event, TickEvent):
            if self.state == Game.STATE_PREPARING:
                self.Start()

class Player:
    """Manages players class"""
    def __init__(self,evMananger):
        self.evMananger = evMananger
        #self.evManager.RegisterListener(self)
        self.characters = [Character(evMananger)]

class Character:
    """Manages Character Class"""
    def __init__(self,evMananger):
        self.evMananger = evMananger
        self.evMananger.RegisterListener(self)
        self.sector = None

    def Move(self, direction):
        if self.sector.MovePossible(direction):
            newSector = self.sector.neighbours[direction]
            self.sector = newSector
            ev = CharacterMoveEvent(self)
            self.evMananger.Post(ev)

    def Place(self, sector):
        self.sector = sector
        ev = CharacterPlaceEvent(self)
        self.evMananger.Post(ev)

    def Notify(self, event):
        if isinstance(event, GameStartedEvent):
            map = event.game.map
            self.Place(map.sectors[map.startSectorIndex])

        elif isinstance(event, CharacterMoveRequest):
            self.Move(event.direction)

class Map:
    """Manages Map Class"""
    def __init__(self,evMananger):
        self.evMananger = evMananger
        #self.evMananger.RegisterListener(self)

        self.sectors = list(range(9))
        self.startSectorIndex = 0

    def Build(self):
        for i in list(range(9)):
            self.sectors[i] = Sector(self.evMananger)

        self.sectors[3].neighbors[DIRECTION_UP] = self.sectors[0]
        self.sectors[4].neighbors[DIRECTION_UP] = self.sectors[1]
        self.sectors[5].neighbors[DIRECTION_UP] = self.sectors[2]
        self.sectors[6].neighbors[DIRECTION_UP] = self.sectors[3]
        self.sectors[7].neighbors[DIRECTION_UP] = self.sectors[4]
        self.sectors[8].neighbors[DIRECTION_UP] = self.sectors[5]

        self.sectors[0].neighbors[DIRECTION_DOWN] = self.sectors[3]
        self.sectors[1].neighbors[DIRECTION_DOWN] = self.sectors[4]
        self.sectors[2].neighbors[DIRECTION_DOWN] = self.sectors[5]
        self.sectors[3].neighbors[DIRECTION_DOWN] = self.sectors[6]
        self.sectors[4].neighbors[DIRECTION_DOWN] = self.sectors[7]
        self.sectors[5].neighbors[DIRECTION_DOWN] = self.sectors[8]

        self.sectors[1].neighbors[DIRECTION_LEFT] = self.sectors[0]
        self.sectors[2].neighbors[DIRECTION_LEFT] = self.sectors[1]
        self.sectors[4].neighbors[DIRECTION_LEFT] = self.sectors[3]
        self.sectors[5].neighbors[DIRECTION_LEFT] = self.sectors[4]
        self.sectors[7].neighbors[DIRECTION_LEFT] = self.sectors[6]
        self.sectors[8].neighbors[DIRECTION_LEFT] = self.sectors[7]

        self.sectors[0].neighbors[DIRECTION_RIGHT] = self.sectors[1]
        self.sectors[1].neighbors[DIRECTION_RIGHT] = self.sectors[2]
        self.sectors[3].neighbors[DIRECTION_RIGHT] = self.sectors[4]
        self.sectors[4].neighbors[DIRECTION_RIGHT] = self.sectors[5]
        self.sectors[6].neighbors[DIRECTION_RIGHT] = self.sectors[7]
        self.sectors[7].neighbors[DIRECTION_RIGHT] = self.sectors[8]

        ev = MapBuiltEvent(self)
        self.evMananger.Post(ev)

    class Sector:
        """Sector Management Class"""
        def __init__(self,evMananger):
            self.evMananger = evMananger
            #self.evMananger.RegisterListener(self)
            self.neighbors = list(range(4))
            self.neighbors[DIRECTION_UP] = None
            self.neighbors[DIRECTION_DOWN] = None
            self.neighbors[DIRECTION_LEFT] = None
            self.neighbors[DIRECTION_RIGHT] = None

        def MovePossible(self, direction):
            if self.neighbors[direction]:
                return 1
