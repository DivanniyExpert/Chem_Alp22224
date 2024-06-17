import pygame, controls
from gun import lazer
from pygame.sprite import Group
from stats import Stats
from scores import Scores



def run():
    pygame.init()
    screen = pygame.display.set_mode((300, 400))
    pygame.display.set_caption("Космические защитники")
    bg_color = (20, 62, 78)
    gun = lazer(screen)
    bullets = Group()
    inos = Group()
    controls.create_a(screen, inos)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, stats, sc, gun, inos, bullets)
            controls.update_bullets(screen, stats, sc, inos, bullets)
            controls.update_inos(stats, screen, sc, gun, inos, bullets)

run()