
import pygame
from HanoiTower import HanoiTower

pygame.init()
screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption('Ханойская башня')

honoyTower = HanoiTower(50, 250, 10, screen)

game = True
while game:

    honoyTower.draw_towers()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            honoyTower.move(int(x / 500 * 3))

        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            honoyTower.execute()

        if event.type == pygame.KEYDOWN and pygame.K_0 <= event.key <= pygame.K_9:
            honoyTower = HanoiTower(50, 250, event.key - 48, screen)
