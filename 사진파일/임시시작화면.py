from turtle import width
import pygame
import time
import sys

pygame.init()

white = (255, 255, 255)

titleImg = pygame.image.load("title.png")
startImg = pygame.image.load("starticon.png")
quitImg = pygame.image.load("quiticon.png")
clickStartImg = pygame.image.load("clickedStartIcon.png")
clickQuitImg = pygame.image.load("clickedQuitIcon.png")
vanillaImg = pygame.image.load("vanilla.png")
flip_vanillaImg = pygame.transform.flip(vanillaImg, True, False)
shotingstarImg = pygame.image.load("shotingstar.png")
flip_shotingstar = pygame.transform.flip(shotingstarImg, True, False)


display_width = 640
display_height = 480
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


# class Background(self, img_in, x, y, width, pygame.freetype.height, img_act):
    #background1 = gameDisplay.blit(vanillaImg, (20, 10))
    #background2 = gameDisplay.blit(shotingstarImg, (20, 370))
    # pygame.time.delay()(1000)
    #background1 = gameDisplay.blit(flip_vanillaImg, (20, 10))
    #background2 = gameDisplay.blit(flip_shotingstar, (20, 370))


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

        titletext = gameDisplay.blit(titleImg, (20, 190))
        background1 = gameDisplay.blit(vanillaImg, (20, 10))
        background2 = gameDisplay.blit(shotingstarImg, (20, 370))
        #backgroun1 = Background(vanillaImg, )
        startButton = Button(startImg, 510, 104, 60, 20,
                             clickStartImg, 510, 108, None)
        quitButton = Button(quitImg, 510, 370, 60, 20,
                            clickQuitImg, 510, 374, quitgame)
        pygame.display.update()
        clock.tick(15)
        pos = pygame.mouse.get_pos()
        print(pos)


mainmenu()
