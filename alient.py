import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс що представляє собою прибульця з флоту"""
   
    def __init__(self, ai_game):
        "Ініціалізувати прибульця та задати його початкову позицію."
        super().__init__()
        self.screen = ai_game.screen
        
        # self.settings = ai_game.settings
        # self.screen_rect = ai_game.screen.get_rect()

        # Завантажити зображення корабля та отримати його rect
        self.image = pygame.transform.scale(pygame.image.load('images/PngItem_3021934_solo.png').convert_alpha() , (50,90))
        self.rect = self.image.get_rect()

        # Створювати кожен новий корабель внизу єкрана по центру
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

       # зберегти десяткове значення для позиції корабля по горизонталі
        self.x = float(self.rect.x)

        # індикатори руху
        # self.moving_right = False
        # self.moving_left = False