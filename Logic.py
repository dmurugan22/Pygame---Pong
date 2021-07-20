import random

#Players
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def up(self):
        self.y -= 5
        if self.y <= 0:
            self.y = 0
        
    def down(self):
        self.y += 5
        if self.y >= 500: 
            self.y = 500

    def move(self, dir):
        if dir == 'up':
            self.up()
        elif dir == 'down':
            self.down()

p1 = Player(10, 250)
p2 = Player(770, 250)

#Ball
ready = False
ballX = 370
ballY = 270

#Speed
ballX_change = 5
ballY_change = 5*random.randint(-300, 300) / 800

def set_speed(num):
    global ballX_change, ballY_change
    ballX_change *= num
    ballY_change *= num

#Ball Movement
def startBall():
    global ready
    ready = False

    global ballX, ballY, ballX_change, ballY_change
    ballX = 370
    ballY = 270
    ballY_change = ballX_change * random.randint(-300, 300) / 800

def hit(ballX, ballY, playerX, playerY):
    return abs((ballX+16) - (playerX+12)) <= 28 and abs((ballY+16)-(playerY+50)) <= 50

def moveBall():
    global ballX, ballY, ballX_change, ballY_change
    ballX += ballX_change
    ballY += ballY_change
    if ballY <= 0 or ballY >= 570: 
        ballY_change *= -1
    
    hit1 = hit(ballX, ballY, p1.x, p1.y)
    hit2 = hit(ballX, ballY, p2.x, p2.y)
    if hit1 or hit2:
        ballX_change *= -1

#Score
score1 = score2 = 0

def score_pt():
    global score1, score2
    if ballX <= 0 or ballX >= 770:
        if ballX <= 0:
            score2 += 1
        elif ballX >= 770:
            score1 += 1
        startBall()

def checkEnd():
    global score1, score2
    if score1 == 10 or score2 == 10:
        return True
    return False

def reset():
    global score1, score2
    score1 = score2 = 0

    global ballX_change, ballY_change
    ballX_change = 5
    ballY_change = 5*random.randint(-300, 300) / 800