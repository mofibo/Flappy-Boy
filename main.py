import pygame
from random import randint
import numpy as np

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 200, 0)
red = (200, 0, 0)
blue = (65, 111, 194)
bright_green = (0, 255, 0)
bright_red = (255, 0, 0)

pygame.init()

# Display pygame window
size = pygame.display.Info().current_w, pygame.display.Info().current_h  # 700, 500
window = pygame.display.set_mode(size, pygame.RESIZABLE)
screen = pygame.display.get_surface()

# the name of the game and the icon
pygame.display.set_caption("Flappy Boy")
iconIMG = pygame.image.load("utils/pers.png")
pygame.display.set_icon(iconIMG)

# background
fond = pygame.image.load("utils/bg.png")
fond = pygame.transform.scale(fond, size)

# personage
persIMG = pygame.image.load("utils/pers.png")
persIMG = pygame.transform.scale(
    persIMG, tuple((5 * (np.array(list(size)) / np.array(list(persIMG.get_size())))).astype(int))
)

# background music
pygame.mixer.music.load("utils/background.mp3")

done = False
clock = pygame.time.Clock()


# Text
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


# build personage
def ball(x, y):
    window.blit(persIMG, (x, y))
    # pygame.draw.circle(screen,black,[x,y],20)


# gameover
def gameover():
    font = pygame.font.SysFont(None, 200)
    text = font.render("GAME OVER", True, red)
    text_rect = text.get_rect(center=(size[0] / 2, size[1] / 4))
    screen.blit(text, text_rect)
    pygame.mixer.music.stop()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    smallText = pygame.font.Font("freesansbold.ttf", 80)

    textSurf1, textRect1 = text_objects("RESTART", smallText)
    restart_rect = textSurf1.get_rect(center=(size[0] / 3, size[1] / 1.5))
    textRect1.center = (size[0] / 3, size[1] / 1.5)
    screen.blit(textSurf1, textRect1)

    textSurf2, textRect2 = text_objects("EXIT", smallText)
    exit_rect = textSurf2.get_rect(center=(size[0] / 1.5, size[1] / 1.5))
    textRect2.center = (size[0] / 1.5, size[1] / 1.5)

    if restart_rect.left <= mouse[0] <= restart_rect.right and restart_rect.top <= mouse[1] <= restart_rect.bottom:
        pygame.draw.rect(screen, bright_green, restart_rect)  # (150, 380, 120, 60))
        screen.blit(textSurf1, textRect1)

    else:
        pygame.draw.rect(screen, green, restart_rect)  # (150, 380, 120, 60))
        screen.blit(textSurf1, textRect1)

    if exit_rect.left <= mouse[0] <= exit_rect.right and exit_rect.top <= mouse[1] <= exit_rect.bottom:
        pygame.draw.rect(screen, bright_red, exit_rect)  # (460, 380, 120, 60))
        screen.blit(textSurf2, textRect2)
        if click[0] == 1:
            pygame.quit()
    else:
        pygame.draw.rect(screen, red, exit_rect)  # (460, 380, 120, 60))
        screen.blit(textSurf2, textRect2)


# obstacles
def obstacle(xloc, yloc, xsize, ysize):
    pygame.draw.rect(screen, blue, [xloc, yloc, xsize, ysize])
    pygame.draw.rect(screen, blue, [xloc, int(yloc + ysize + space), xsize, ysize + 500])


# score
def Score(score):
    font = pygame.font.SysFont(None, 75)
    text = font.render("Score:" + str(score), True, black)
    screen.blit(text, [0, 0])


# variables initialisation
x = size[0] / 2
y = size[1] / 2
x_speed = 0
y_speed = 0
ground = 477
xloc = size[0]
yloc = 0
xsize = size[0] / 10
ysize = randint(0, size[1] / 1.5)
space = 150
obspeed = 2.5
score = 0

if __name__ == "__main__":
    # start background music
    pygame.mixer.music.play()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_speed = -10

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    y_speed = 5

        # background fond
        screen.blit(fond, (0, 0))

        obstacle(xloc, yloc, xsize, ysize)
        ball(x, y)
        Score(score)

        # copyrights
        fontt = pygame.font.SysFont(None, 35)
        text2 = fontt.render("FIBO Copyrights 2017-..", True, black)
        screen.blit(text2, [size[0] / 1.25, size[1] / 1.1])

        y += y_speed
        xloc -= obspeed
        if y > ground:
            gameover()
            y_speed = 0
            obspeed = 0
        if xloc < -80:
            xloc = 700
            size = randint(0, 350)
        if x + 20 > xloc and y - 20 < ysize and x - 15 < xsize + xloc:
            gameover()
            obspeed = 0
            y_speed = 0

        if x + 20 > xloc and y + 20 > ysize + space and x - 15 < xsize + xloc:
            gameover()
            obspeed = 0
            y_speed = 0

        if xloc <= 80:
            xloc = 700
            ysize = randint(0, 350)
        if xloc < x < xloc + 3:
            score = score + 1

        # screen
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
