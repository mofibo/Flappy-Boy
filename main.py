import pygame
from random import randint

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 200, 0)
red = (200, 0, 0)
blue = (65, 111, 194)
bright_green = (0, 255, 0)
bright_red = (255, 0, 0)

pygame.init()

# Display pygame window
size = 700, 500
window = pygame.display.set_mode(size)
screen = pygame.display.get_surface()

# the name of the game and the icon
pygame.display.set_caption("Flappy Boy")
iconIMG = pygame.image.load("utils/pers.png")
pygame.display.set_icon(iconIMG)

# background
fond = pygame.image.load("utils/bg.png")

# personage
persIMG = pygame.image.load("utils/pers.png")

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
    font = pygame.font.SysFont(None, 75)
    text = font.render("GAME OVER", True, red)
    screen.blit(text, [200, 250])
    pygame.mixer.music.stop()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if 150 + 120 > mouse[0] > 150 and 380 + 60 > mouse[1] > 380:
        pygame.draw.rect(screen, bright_green, (150, 380, 120, 60))

    else:
        pygame.draw.rect(screen, green, (150, 380, 120, 60))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf1, textRect1 = text_objects("RESTART", smallText)
    textRect1.center = ((150 + (120 / 2)), (380 + (60 / 2)))
    screen.blit(textSurf1, textRect1)

    if 460 + 120 > mouse[0] > 460 and 380 + 60 > mouse[1] > 380:
        pygame.draw.rect(screen, bright_red, (460, 380, 120, 60))
        if click[0] == 1:
            pygame.quit()
    else:
        pygame.draw.rect(screen, red, (460, 380, 120, 60))
        if click[0] == 1:
            print("restart")

    textSurf2, textRect2 = text_objects("EXIT", smallText)
    textRect2.center = ((460 + (120 / 2)), (380 + (60 / 2)))
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
x = 350
y = 250
x_speed = 0
y_speed = 0
ground = 477
xloc = 700
yloc = 0
xsize = 70
ysize = randint(0, 350)
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
        fontt = pygame.font.SysFont(None, 25)
        text2 = fontt.render("FIBO Copyrights 2017", True, black)
        screen.blit(text2, [500, 480])

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
