#create a sphere using opengl
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def sphere(radius, slices, stacks):
    #draw the sphere using the given radius, slices, and stacks
    for i in range(slices):
        theta = i * math.pi * 2.0 / slices
        theta2 = (i + 1) * math.pi * 2.0 / slices
        glBegin(GL_QUAD_STRIP)
        for j in range(stacks):
            phi = j * math.pi / stacks
            x = math.cos(theta) * math.sin(phi)
            y = math.sin(theta) * math.sin(phi)
            z = math.cos(phi)
            glVertex3f(radius * x, radius * y, radius * z)
            x = math.cos(theta2) * math.sin(phi)
            y = math.sin(theta2) * math.sin(phi)
            z = math.cos(phi)
            glVertex3f(radius * x, radius * y, radius * z)
        glEnd()

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        sphere(1, 30, 30)
        pygame.display.flip()
        pygame.time.wait(10)

main()
# The sphere function takes three arguments: radius, slices, and stacks. The radius is the size of the sphere, while slices and stacks determine the number of divisions in the horizontal and vertical directions, respectively. The sphere is drawn using a series of quad strips, with each strip representing a slice of the sphere. The vertices of each quad strip are calculated using spherical coordinates, and the resulting points are scaled by the radius to create the final sphere shape. The main function sets up the OpenGL environment and continuously rotates and displays the sphere. The user can close the window by clicking the close button, which will exit the program.
#
# This code snippet demonstrates how to create a 3D sphere using OpenGL in Python. The sphere function generates the vertices of the sphere based on the specified radius, slices, and stacks. The main function sets up the OpenGL environment, creates a window, and continuously rotates and displays the sphere. The user can close the window by clicking the close button, which will exit the program.
#
