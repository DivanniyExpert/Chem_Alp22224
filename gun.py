import pygame
from pygame.sprite import Sprite

class lazer(Sprite):

    def __init__(self, screen):
        #инициализация пушки

        super(lazer, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('image/Pushka.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False

    def output(self):
        #otrisovka
        self.screen.blit(self.image, self.rect)

    def update_gun(self):

        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 0.15

        if self.mleft and self.rect.left > 0:
            self.center -= 0.15
        
        self.rect.centerx = self.center
    
    def create_gun(self):
        self.center = self.screen_rect.centerx