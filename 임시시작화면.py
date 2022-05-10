import pygame
import time
import sys

pygame.init()

white = (255, 255, 255)

titleImg = pygame.image.load("/Users/junhuckjung/Desktop/시작화면/title.png") # 아직 os를 사용안해서 직접 자신의 이미지 파일 경로를 입력해야함
startImg = pygame.image.load("/Users/junhuckjung/Desktop/시작화면/starticon.png") # 아직 os를 사용안해서 직접 자신의 이미지 파일 경로를 입력해야함
quitImg = pygame.image.load("/Users/junhuckjung/Desktop/시작화면/quiticon.png") # 아직 os를 사용안해서 직접 자신의 이미지 파일 경로를 입력해야함
clickStartImg = pygame.image.load(
    "/Users/junhuckjung/Desktop/시작화면/clickedStartIcon.png") # 아직 os를 사용안해서 직접 자신의 이미지 파일 경로를 입력해야함
clickQuitImg = pygame.image.load(
    "/Users/junhuckjung/Desktop/시작화면/clickedQuitIcon.png") # 아직 os를 사용안해서 직접 자신의 이미지 파일 경로를 입력해야함

display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("제목")

clock = pygame.time.Clock()


class Button:
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y:
            gameDisplay.blit(img_act, (x_act, y_act))
            if click[0] and action != None:
                time.sleep(1)
                action()
        else:
            gameDisplay.blit(img_in, (x, y))


def quitgame():
    pygame.quit()
    sys.exit()


def mainmenu():

    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.fill(white)

        titletext = gameDisplay.blit(titleImg, (220, 150))
        startButton = Button(startImg, 280, 260, 60, 20,
                             clickStartImg, 273, 258, None)
        quitButton = Button(quitImg, 445, 260, 60, 20,
                            clickQuitImg, 440, 258, quitgame)
        pygame.display.update()
        clock.tick(15)


mainmenu()
