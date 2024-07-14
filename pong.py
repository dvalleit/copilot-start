import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Game objects
class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dy = 0

    def draw(self):
        glBegin(GL_QUADS)
        glVertex2f(self.x - 0.02, self.y + 0.15)
        glVertex2f(self.x + 0.02, self.y + 0.15)
        glVertex2f(self.x + 0.02, self.y - 0.15)
        glVertex2f(self.x - 0.02, self.y - 0.15)
        glEnd()

    def move(self):
        self.y += self.dy

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 0.01
        self.dy = 0.01

    def draw(self):
        glBegin(GL_QUADS)
        glVertex2f(self.x - 0.02, self.y + 0.02)
        glVertex2f(self.x + 0.02, self.y + 0.02)
        glVertex2f(self.x + 0.02, self.y - 0.02)
        glVertex2f(self.x - 0.02, self.y - 0.02)
        glEnd()

    def move(self, left_paddle, right_paddle):
        self.x += self.dx
        self.y += self.dy

        # Collision detection with the top and bottom of the screen
        if self.y >= 1 or self.y <= -1:
            self.dy *= -1

        # Collision detection with the paddles
        if (self.x - 0.02 <= left_paddle.x + 0.02 and
            left_paddle.y - 0.15 <= self.y <= left_paddle.y + 0.15) or \
           (self.x + 0.02 >= right_paddle.x - 0.02 and
            right_paddle.y - 0.15 <= self.y <= right_paddle.y + 0.15):
            self.dx *= -1

# Initialize Pygame and OpenGL
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
gluOrtho2D(-1, 1, -1, 1)

# Game objects
left_paddle = Paddle(-0.9, 0)
right_paddle = Paddle(0.9, 0)
ball = Ball(0, 0)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Input handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        left_paddle.dy = 0.05
    elif keys[pygame.K_s]:
        left_paddle.dy = -0.05
    else:
        left_paddle.dy = 0

    if keys[pygame.K_UP]:
        right_paddle.dy = 0.05
    elif keys[pygame.K_DOWN]:
        right_paddle.dy = -0.05
    else:
        right_paddle.dy = 0

    # Update game objects
    left_paddle.move()
    right_paddle.move()
    # Inside the game loop
    ball.move(left_paddle, right_paddle)

    # Collision detection and response
    if ball.y >= 1 or ball.y <= -1:
        ball.dy *= -1
    if (ball.x <= left_paddle.x + 0.02 and ball.y in range(left_paddle.y - 0.15, left_paddle.y + 0.15)) or \
       (ball.x >= right_paddle.x - 0.02 and ball.y in range(right_paddle.y - 0.15, right_paddle.y + 0.15)):
        ball.dx *= -1

    # Render
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    left_paddle.draw()
    right_paddle.draw()
    ball.draw()
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()