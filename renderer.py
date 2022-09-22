import pygame
import sys
from pygame.locals import *
from gme.box import Box
from gme.bfs import BreadhFirstSearch
from time import sleep


class Renderer:
    WIDTH = 800
    HEIGHT = 600
    ROW = 50
    COL = 50
    MENU_PERCENT = 0.25

    def __init__(self) -> None:
        self.run = True
        pygame.init()
        self.DISPLAYSURF = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("BFS")
        self.WINDOW_BOX = Box(
            self.WIDTH - (self.WIDTH * self.MENU_PERCENT),
            self.HEIGHT,
            self.ROW,
            self.COL,
            self.DISPLAYSURF,
            pygame,
        )
        self.WINDOW_BOX.create_block()
        self.src = None
        self.dest = None
        self.bfs = BreadhFirstSearch(self.WINDOW_BOX)

    def setup(self):
        pass

    def loop(self):
        while self.run:
            self.DISPLAYSURF.fill("Black")
            self.WINDOW_BOX.update_block(self.DISPLAYSURF, pygame)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if pygame.mouse.get_pressed()[0]:
                    cur_pos = pygame.mouse.get_pos()
                    # print(cur_pos)
                    self.WINDOW_BOX.select_block(*cur_pos)
                if pygame.mouse.get_pressed()[1]:
                    if self.src and self.dest:
                        self.bfs.find_path(self.src, self.dest)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        src_id = self.WINDOW_BOX.get_id(*pygame.mouse.get_pos())
                        self.src = self.WINDOW_BOX.block_list[src_id]
                        self.WINDOW_BOX.set_source(self.src)
                    if event.key == pygame.K_d:
                        dest_id = self.WINDOW_BOX.get_id(*pygame.mouse.get_pos())
                        self.dest = self.WINDOW_BOX.block_list[dest_id]
                        self.WINDOW_BOX.set_dest(self.dest)

                # if pygame.mouse.get_pressed()[2]:
                #     cur_pos = pygame.mouse.get_pos()
                #     # print(cur_pos)
                #     self.WINDOW_BOX.select_block(*cur_pos)

            pygame.display.update()


if __name__ == "__main__":
    renderer = Renderer()
    renderer.loop()
