import time

import pygame


class HanoiTower(object):
    def __init__(self, x, y, k, screen):
        self.x, self.y = x, y
        self.screen = screen
        self.color = (150, 110, 10)
        self.k = k
        self.selected = 0
        self.run = False
        self.a = [[k - i for i in range(k)], [], []]

    def draw_towers(self):
        self.screen.fill((200, 200, 200))

        pygame.draw.rect(self.screen, self.color, (self.x, self.y, 400, 20), border_radius=8)
        pygame.draw.rect(self.screen, self.color, (self.x + 62, self.y - 190, 15, 200), border_radius=8)
        pygame.draw.rect(self.screen, self.color, (self.x + 194, self.y - 190, 15, 200), border_radius=8)
        pygame.draw.rect(self.screen, self.color, (self.x + 326, self.y - 190, 15, 200), border_radius=8)

        for i in range(3):
            h = self.y - 20
            for hi, e in enumerate(self.a[i]):
                dh = h - 20 * hi - 30 if self.selected == i + 1 and hi == len(self.a[i]) - 1 else 0
                color = (170, 130, 10) if e % 2 else (100, 70, 0)
                pygame.draw.rect(self.screen, color, (self.x + 50 - 5 * e + i * 132, h - 20 * hi - dh,
                                                      40 + 10 * e, 20), border_radius=10)

        if self.run:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    self.run = False

        pygame.display.flip()

    def move(self, n):
        if self.a[n] and not self.selected:
            self.selected = n + 1
        elif self.selected and (not self.a[n] or self.a[n][-1] >= self.a[self.selected - 1][-1]):
            self.a[n].append(self.a[self.selected - 1].pop(-1))
            self.selected = 0

    def execute(self):
        self.run = True
        for i in range(self.k, 0, -1):
            self._request(i, 2)
        self.run = False

    def _request(self, k, move_to):
        move_from = [i for i in range(3) if k in self.a[i]][0]

        if move_from == move_to:
            return 0

        while not (k == self.a[move_from][-1] and (not self.a[move_to] or self.a[move_to][-1] >= k)):
            if not self.run:
                return 0

            if k != self.a[move_from][-1]:
                self._request(self.a[move_from][self.a[move_from].index(k) + 1], 3 - move_to - move_from)

            if self.a[move_to] and self.a[move_to][-1] < k:
                self._request([e for e in self.a[move_to] if e < k][0], 3 - move_to - move_from)

        self.selected = move_from + 1
        self.move(move_to)
        self.draw_towers()
        time.sleep(0.03)
