import pygame
from random import randint


class FlappyBoy:
    def __init__(self):
        # the name of the game and the icon
        pygame.display.set_caption("Flappy Boy")
        self.FlappyBoyIMG = pygame.image.load("utils/pers.png")
        pygame.display.set_icon(self.FlappyBoyIMG)

        # Display game window
        size = 700, 500
        self.window = pygame.display.set_mode(size, pygame.RESIZABLE)
        self.screen = pygame.display.get_surface()

        # background
        self.fond = pygame.image.load("utils/bg.png")

        # personage
        self.persIMG = pygame.image.load("utils/pers.png")

        # background music
        pygame.mixer.music.load("utils/background.mp3")

        # define colors
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.green = (0, 200, 0)
        self.red = (200, 0, 0)
        self.blue = (65, 111, 194)
        self.bright_green = (0, 255, 0)
        self.bright_red = (255, 0, 0)

        # variables initialisation
        self.x = 350
        self.y = 250
        self.x_speed = 0
        self.y_speed = 0
        self.ground = 477
        self.xloc = 700
        self.yloc = 0
        self.xsize = 70
        self.ysize = randint(0, 350)
        self.space = 150
        self.obspeed = 2.5
        self.score = 0
        return

    def obstacle(self, xloc, yloc, xsize, ysize):
        pygame.draw.rect(self.screen, self.blue, [xloc, yloc, xsize, ysize])
        pygame.draw.rect(self.screen, self.blue, [xloc, int(yloc + ysize + self.space), xsize, ysize + 500])
        return

    def game_score(self, score):
        font = pygame.font.SysFont(None, 75)
        text = font.render("Score:" + str(score), True, self.black)
        self.screen.blit(text, [0, 0])
        return

    def game_personage(self, x, y):
        self.window.blit(self.FlappyBoyIMG, (x, y))
        return

    def text_objects(self, text, font):
        textSurface = font.render(text, True, self.black)
        return textSurface, textSurface.get_rect()

    def gameover(self):
        font = pygame.font.SysFont(None, 75)
        text = font.render("GAME OVER", True, self.red)
        self.screen.blit(text, [200, 250])
        pygame.mixer.music.stop()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 150 + 120 > mouse[0] > 150 and 380 + 60 > mouse[1] > 380:
            pygame.draw.rect(self.screen, self.bright_green, (150, 380, 120, 60))

        else:
            pygame.draw.rect(self.screen, self.green, (150, 380, 120, 60))

        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textSurf1, textRect1 = self.text_objects("RESTART", smallText)
        textRect1.center = ((150 + (120 / 2)), (380 + (60 / 2)))
        self.screen.blit(textSurf1, textRect1)

        if 460 + 120 > mouse[0] > 460 and 380 + 60 > mouse[1] > 380:
            pygame.draw.rect(self.screen, self.bright_red, (460, 380, 120, 60))
            if click[0] == 1:
                pygame.quit()
        else:
            pygame.draw.rect(self.screen, self.red, (460, 380, 120, 60))
            if click[0] == 1:
                print("restart")

        textSurf2, textRect2 = self.text_objects("EXIT", smallText)
        textRect2.center = ((460 + (120 / 2)), (380 + (60 / 2)))
        self.screen.blit(textSurf2, textRect2)
        return

    def main_game(self):
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
            self.screen.blit(self.fond, (0, 0))

            self.obstacle(self.xloc, self.yloc, self.xsize, self.ysize)
            self.game_personage(self.x, self.y)
            self.game_score(self.score)

        return
