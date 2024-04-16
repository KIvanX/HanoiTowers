
import pygame
from HanoiTower import HanoiTower

pygame.init()
screen = pygame.display.set_mode((500, 300))
pygame.display.set_caption('Ханойская башня')

hanoyTower = HanoiTower(50, 250, 5, screen)

game = True
while game:

    hanoyTower.draw_towers()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            hanoyTower.move(int(x / 500 * 3))

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            hanoyTower.execute()

        if event.type == pygame.KEYDOWN and pygame.K_0 <= event.key <= pygame.K_9:
            hanoyTower = HanoiTower(50, 250, event.key - 48, screen)
