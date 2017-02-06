#view
import pygame
from events import TickEvent

class PygameView:
    """Pygame view class"""
    def __init__(self, evManager):
        self.evManager = evManager
        self.evManager.RegisterListener(self)

        pygame.init()
        self.window = pygame.display.set_mode((428,428))
        pygame.display.set_caption("Example Game")
        self.background = pygame.Surface(self.window.get_size())
        self.background.fill((0, 0, 0))

        self.backSprites = pygame.sprite.RenderUpdates()
        self.frontSprites = pygame.sprite.RenderUpdates()

    def ShowMap(self, map):
        squareRect = pygame.Rect((-128, 10, 128, 128))

        i = 0
        for sector in map.sectors:
            if i  < 3:
                squareRect = squareRect.move(138, 0)
            else:
                i = 0
                squareRect = squareRect.move(-(138 * 2), 138)
            i += 1
            newSprite = SectorSprite(sector, self.backSprites)
            newSprite.rect = squareRect
            newSprite = None

    def ShowCharacter(self,character):
        characterSprite = CharacterSprite(self.frontSprites)

        sector = character.sector
        sectorSprite = self.GetSectorSprite(sector)
        characterSprite.rect.centre = sectorSprite.rect.center

    def MoveCharacter(self,character):
        characterSprite = self.GetCharacterSprite(character)
        sector = character.sector

        sectorSprite = self.GetSectorSprite(sector)
        characterSprite.moveTo = sectorSprite.rect.center

    def GetCharacterSprite(self,character):
        for s in self.frontSprites.sprites():
            return s

    def GetSectorSprite(self,sector):
        for s in self.backSprites.sprites():
            if hasattr(s, 'sector') and s.sector == sector:
                return s

    def Notify(self, event):
        if isinstance(event, TickEvent):
            self.backSprites.clear(self.window, self.background)
            self.frontSprites.clear(self.window, self.background)

            self.backSprites.update()
            self.backSprites.update()

            dirtyRects1 = self.backSprites.draw(self.window)
            dirtyRects2 = self.frontSprites.draw(self.window)

            dirtyRects = dirtyRects1 + dirtyRects2
            pygame.display.update(dirtyRects)

        elif isinstance(event, MapBuiltEvent):
            map = event.map
            self.ShowMap(map)
        elif isinstance(event, CharacterPlaceEvent):
            self.ShowCharacter(event.character)
        elif isinstance(event, CharacterMoveEvent):
            self.MoveCharacter(event.character)
