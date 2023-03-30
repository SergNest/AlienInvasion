import  pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, ai_game):
        """Створити обєкт буллет у поточній позиціє корабля"""
        super().__init__()
        self.screen = ai_game.screen
        self.setting = ai_game.settings
        self.color = self.setting.bullet_color

        # Створити rect кулі у (0, 0) та задати правильну позицію
        self.rect = pygame.Rect(0,0, self.setting.bullet_width, self.setting.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)

    def update(self):
        """Посунути кулю нагору ераном"""
        # Оновити десяткову позицію кулі.
        self.y -= self.setting.bullet_speed
        # Оновити позицію rect
        self.rect.y = self.y
    def draw_bullet(self):
        """Намалювати кулю на екрані"""
        pygame.draw.rect(self.screen, self.color, self.rect)