import pygame
import Logic

pygame.init()

#Screen
screen = pygame.display.set_mode((800, 600))
def set_screen():
    screen.fill((0,0,0))
    pygame.display.set_caption("Pong")
    icon = pygame.image.load('Pong Icon.png')
    pygame.display.set_icon(icon)

#Background
def background():
    background = pygame.image.load('Background.png')
    screen.blit(background, (0,0))

#Players
class Players:
    def __init__(self, image, player):
        self.player_image = pygame.image.load(image)
        self.p = player

    def show_player(self):
        screen.blit(self.player_image, (self.p.x, self.p.y))

player1 = Players('Paddle 1.png', Logic.p1)
player2 = Players('Paddle 2.png', Logic.p2)

#Ball
def ball(x, y):
    ball_image = pygame.image.load("Pong ball.png")
    screen.blit(ball_image, (x, y))

#Score
def show_score(score, x, y):
    font = pygame.font.Font('freesansbold.ttf', 32)
    txt = font.render(str(score), True, (255, 255, 255))
    screen.blit(txt, (x, y))

#Initialize Game
def start_game():
    font = pygame.font.Font('freesansbold.ttf', 50)
    txt = font.render('Welcome to Pong!', True, (0, 255, 255))
    screen.blit(txt, (200, 100))
    font = pygame.font.Font('freesansbold.ttf', 32)
    txt1 = font.render('Click SPACE to continue', True, (0, 255, 255))
    screen.blit(txt1, (200, 250))

def show_rules():
    font = pygame.font.Font('freesansbold.ttf', 16)
    txt1 = font.render('Pong is a two player game.', True, (0, 255, 255))
    txt2 = font.render('Move the paddles up and down to hit the ball and score points', True, (0, 255, 255))
    txt3 = font.render('Use "W" and "S" for the pink paddle', True, (0, 255, 255))
    txt4 = font.render('Use UP and DOWN arrow keys for the blue paddle', True, (0, 255, 255))
    txt5 = font.render('First player to 10 points wins!', True, (0, 255, 255))
    screen.blit(txt1, (200, 100))
    screen.blit(txt2, (200, 150))
    screen.blit(txt3, (200, 200))
    screen.blit(txt4, (200, 250))
    screen.blit(txt5, (200, 300))
    font = pygame.font.Font('freesansbold.ttf', 32)
    txt = font.render('Click SPACE to begin', True, (0, 255, 255))
    screen.blit(txt, (200, 500))

def choose_speed():
    font = pygame.font.Font('freesansbold.ttf', 32)
    txt = font.render('Press 1, 2, or 3 to choose a speed', True, (0, 255, 255))
    screen.blit(txt, (150, 300))

def start_play():
    font = pygame.font.Font('freesansbold.ttf', 50)
    txt = font.render('Press SPACE to start', True, (0, 255, 255))
    screen.blit(txt, (150, 300))

#End Game
def end_game():
    font = pygame.font.Font('freesansbold.ttf', 50)
    if Logic.score1 > Logic.score2:
        txt = font.render('Player 1 wins!', True, (255, 0, 255))
        screen.blit(txt, (200, 100))
    else:
        txt = font.render('Player 2 wins!', True, (0, 255, 255))
        screen.blit(txt, (200, 100))
    font = pygame.font.Font('freesansbold.ttf', 32)
    txt1 = font.render('Click SPACE to play again', True, (255, 255, 255))
    screen.blit(txt1, (200, 250))
