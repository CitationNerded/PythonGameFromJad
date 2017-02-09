"""sprites.py - module contains sprite classes."""
import pygame


class SectorSprite(pygame.sprite.Sprite):
    """SectorSprite - display sector object."""

    def __init__(self, sector, group=None):
        """Initialise SectorSprite object."""
        pygame.sprite.Sprite.__init__(self, group)
        self.image = pygame.Surface((132, 132))
        self.image.fill((0, 255, 128))
        self.rect = self.image.get_rect()
        self.sector = sector


class CharacterSprite(pygame.sprite.Sprite):
    """CharacterSprite - display Character Object."""

    def __init__(self, group=None):
        """Initialise CharacterSprite object."""
        pygame.sprite.Sprite.__init__(self, group)
        characterSurf = pygame.Surface((64, 64))
        pygame.draw.rect(characterSurf, (0, 255, 128), ((0, 0), (64, 64)))
        pygame.draw.circle(characterSurf, (255, 0, 0), (32, 32), 32)
        self.image = characterSurf
        self.rect = characterSurf.get_rect()
        self.moveTo = None

    def Update(self):
        """Update CharacterSprite object."""
        if self.moveTo:
            self.rect.center = self.moveTo
            self.moveTo = None
