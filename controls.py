import pygame, sys
from bullet import Bullet
from ino import Ino
import time


def events(screen, gun, bullets):

    for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_d:
                      gun.mright = True
                elif event.key == pygame.K_a:
                      gun.mleft = True
                elif event.key == pygame.K_s:
                     new_bullet = Bullet(screen, gun)
                     bullets.add(new_bullet)
            
            elif event.type == pygame.KEYUP:

                if event.key == pygame.K_d:
                      gun.mright = False
                elif event.key == pygame.K_a:
                      gun.mleft = False

                     


def update(bgc, screen, stats, sc, gun, inos, bullets):
     #obnova
    screen.fill(bgc)
    sc.show_score
    for bullet in bullets.sprites():
         bullet.draw_bullet()
    gun.output()
    inos.draw(screen)
    pygame.display.flip()

def update_bullets(screen, stats, sc, inos, bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, inos, True, True)
    if collisions:
        for inos in collisions.values():
            stats.score += 10 * len(inos)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_guns()
    if len(inos) == 0:
        bullets.empty()
        create_a(screen, inos)

def gun_kill(stats, screen, sc,  gun, inos, bullets):
     if stats.guns_left > 0:
         stats.guns_left -= 1
         inos.empty()
         bullets.empty()
         create_a(screen, inos)
         gun.create_gun()
         time.sleep(2)
     else:
          stats.run_game = False
          print("Game over!")
          ded = (151, 19, 19)
          screen.fill(ded)
          background = pygame.image.load("image/GO.png")                
          background = pygame.transform.scale(background, (300, 400)) 
          all_sprites = pygame.sprite.Group()
          screen.blit(background,(0,0))                                           
          all_sprites.draw(screen)          
          pygame.display.update()
          time.sleep(3)
          sys.exit()


def update_inos(stats, screen, sc, gun, inos, bullets):
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        gun_kill(stats, screen, sc,  gun, inos, bullets)
    inos_check(stats, screen, sc, gun, inos, bullets)

def inos_check(stats, screen, sc,gun, inos, bullets):
     screen_rect = screen.get_rect()
     for ino in inos.sprites():
          if ino.rect.bottom >= screen_rect.bottom:
               gun_kill(stats, screen, gun, inos, bullets)
               break

def create_a(screen, inos):
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((300 - 2 * ino_width) / ino_width)
    ino_height = ino.rect.height
    number_ino_y = int((400 - 32 - 2 * ino_height) / ino_height)

    for row_number in range(number_ino_y - 2):
    
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + ino_width * ino_number
            ino.y = ino_height + ino_height * row_number
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + ino.rect.height * row_number
            inos.add(ino)

def check_high_score(stats, sc):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('highscore.txt', 'w') as f:
            f.write(str(stats.high_score))