# Импортируем библиотеку pygame
import pygame
from pygame.locals import *

#Объявляем переменные
WIN_WIDTH = 800 #Ширина создаваемого окна
WIN_HEIGHT = 600 # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT) # Группируем ширину и высоту в одну переменную
BACKGROUND_COLOR = "#004400"
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"
cage = pygame.image.load('image/cage.bmp')
background = [[cage, cage, cage, cage, cage, cage, cage, cage],
              [cage, cage, cage, cage, cage, cage, cage, cage],
              [cage, cage, cage, cage, cage, cage, cage, cage],
              [cage, cage, cage, cage, cage, cage, cage, cage],
              [cage, cage, cage, cage, cage, cage, cage, cage],
              [cage, cage, cage, cage, cage, cage, cage, cage]]
def main():
    pygame.init() # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY) # Создаем окошко
    pygame.display.set_caption("Песочница военных действий") # Пишем в шапку
    while True:
        for event in pygame.event.get():
            if event.type == QUIT or (
                                      event.type == KEYDOWN and (
                                      event.key == K_ESCAPE or
                                      event.key == K_q
                                     )):
                pygame.quit()
                quit()
        for a in range(len(background)):
            b = a * 100
            for i in range(len(background[a])):
                screen.blit(background[a][i], (i*100, b))
        pygame.display.update()

main()
