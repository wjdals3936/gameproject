from turtle import Screen
import pygame

pygame.init()  # 초기화
screen = pygame.display.set_mode((600, 800))  # 화면 사이즈
clock = pygame.time.Clock()

while True:
    screen.fill((0, 0, 0))  # 검정색 화면

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    pygame.display.update()
    clock.tick(30)  # 30 프레임으로

pygame.quit()
