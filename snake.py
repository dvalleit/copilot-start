import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random

# Game objects
class Snake:
    def __init__(self):
        self.positions = [(0, 0)]  # Initial position
        self.length = 1
        self.direction = (0, 1)  # Moving up
        self.grow = False

    def draw(self):
        glBegin(GL_QUADS)
        for pos in self.positions:
            x, y = pos
            glVertex2f(x - 0.05, y + 0.05)
            glVertex2f(x + 0.05, y + 0.05)
            glVertex2f(x + 0.05, y - 0.05)
            glVertex2f(x - 0.05, y - 0.05)
        glEnd()

    def move(self):
        if self.grow:
            self.length += 1
            self.grow = False
        new_head = (self.positions[0][0] + self.direction[0] * 0.1, self.positions[0][1] + self.direction[1] * 0.1)
        self.positions.insert(0, new_head)
        if len(self.positions) > self.length:
            self.positions.pop()

    def eat(self, food_pos):
        if self.positions[0] == food_pos:
            self.grow = True
            return True
        return False

    def check_collision(self):
        # Check wall collision
        if not -1 < self.positions[0][0] < 1 or not -1 < self.positions[0][1] < 1:
            return True
        # Check self collision
        if self.positions[0] in self.positions[1:]:
            return True
        return False

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.spawn()

    def spawn(self):
        self.position = (random.randint(-9, 9) / 10.0, random.randint(-9, 9) / 10.0)

    def draw(self):
        glBegin(GL_QUADS)
        glVertex2f(self.position[0] - 0.05, self.position[1] + 0.05)
        glVertex2f(self.position[0] + 0.05, self.position[1] + 0.05)
        glVertex2f(self.position[0] + 0.05, self.position[1] - 0.05)
        glVertex2f(self.position[0] - 0.05, self.position[1] - 0.05)
        glEnd()

# Initialize Pygame and OpenGL
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
gluOrtho2D(-1, 1, -1, 1)

# Game objects
snake = Snake()
food = Food()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Input handling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        snake.direction = (0, 1)
    elif keys[pygame.K_DOWN]:
        snake.direction = (0, -1)
    elif keys[pygame.K_LEFT]:
        snake.direction = (-1, 0)
    elif keys[pygame.K_RIGHT]:
        snake.direction = (1, 0)

    # Update game objects
    snake.move()
    if snake.eat(food.position):
        food.spawn()
    if snake.check_collision():
        running = False  # End game on collision

    # Render
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    snake.draw()
    food.draw()
    pygame.display.flip()
    pygame.time.wait(100)

pygame.quit()