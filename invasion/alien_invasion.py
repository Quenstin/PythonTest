import sys

import pygame

from invasion.ship import Ship
from settings import Settings


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.setting = Settings()
        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        pygame.display.set_caption("小游戏")
        self.ship = Ship(self)

    def run_game(self):
        #
        while True:
            self._check_event()
            self._update_screen()

    def _check_event(self):
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event == pygame.KEYDOWN:
                if event == pygame.K_RIGHT:
                    self.ship.rect.x += 1

    def _update_screen(self):
        self.screen.fill(self.setting.screen_color)
        self.ship.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    # 初始化类需要带括号
    ai = AlienInvasion()
    ai.run_game()
