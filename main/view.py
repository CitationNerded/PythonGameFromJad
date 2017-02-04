#view
import pygame

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

    
