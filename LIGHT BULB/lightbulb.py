import pygame
from pygame.locals import *
from math import *
import time


# Degrees to Radians
def dtr(x):
    return (x*pi)/180


def fill(surface, position, fill_color):
    fill_color = surface.map_rgb(fill_color)  # Convert the color to mapped integer value.
    surf_array = pygame.surfarray.pixels2d(surface)  # Create an array from the surface.
    current_color = surf_array[position]  # Get the mapped integer color value.

    frontier = [position]
    while len(frontier) > 0:
        x, y = frontier.pop()
        try:  # Add a try-except block in case the position is outside the surface.
            if surf_array[x, y] != current_color:
                continue
        except IndexError:
            continue
        surf_array[x, y] = fill_color
        # Then we append the neighbours of the pixel in the current position to our 'frontier' list.
        frontier.append((x + 1, y))  # Right.
        frontier.append((x - 1, y))  # Left.
        frontier.append((x, y + 1))  # Down.
        frontier.append((x, y - 1))  # Up.

    pygame.surfarray.blit_array(surface, surf_array)


# Program to draw a light bulb
pygame.init()

size = [728, 600]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Light Bulb")
 
### Colors
WHITE = (255, 255, 255)
GREY = (126, 126, 126)
LIGHT_GREY = (221, 221, 221)
BLACK = (0, 0, 0)
YELLOW = (252, 247, 157)
LIGHT = (254, 214, 49)

screen.fill(WHITE)

done = False
clock = pygame.time.Clock()

 
clock.tick(10)
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        done=True

### Base 

# Screw
pygame.draw.polygon(screen, LIGHT_GREY, [[295, 431], [295+137, 431], [295+137, 460-14], [295, 460]], 0)
pygame.draw.polygon(screen, BLACK, [[295, 431], [295+137, 431], [295+137, 460-14], [295, 460]], 1)
pygame.draw.polygon(screen, LIGHT_GREY, [[300, 459], [300, 470], [300+127, 470-12], [427, 446]], 0)
pygame.draw.polygon(screen, BLACK, [[300, 459], [300, 470], [300+127, 470-12], [427, 446]], 1)
pygame.draw.polygon(screen, LIGHT_GREY, [[300, 479], [300, 490], [300+127, 490-12], [427, 467]], 0)
pygame.draw.polygon(screen, BLACK, [[300, 479], [300, 490], [300+127, 490-12], [427, 467]], 1)
pygame.draw.polygon(screen, LIGHT_GREY, [[300, 499], [300, 510], [300+127, 510-12], [427, 487]], 0)
pygame.draw.polygon(screen, BLACK, [[300, 499], [300, 510], [300+127, 510-12], [427, 487]], 1)
pygame.draw.polygon(screen, LIGHT_GREY, [[300, 519], [300+127, 519], [427, 507]], 0)       
pygame.draw.polygon(screen, BLACK, [[300, 519], [300+127, 519], [427, 507]], 1)
pygame.draw.arc(screen, BLACK, [[296, 470], [10, 11]], dtr(90), dtr(270))
pygame.draw.arc(screen, BLACK, [[296, 490], [10, 11]], dtr(90), dtr(270))
pygame.draw.arc(screen, BLACK, [[296, 510], [10, 11]], dtr(90), dtr(270))
pygame.draw.arc(screen, BLACK, [[421, 457], [10, 11]], dtr(270), dtr(90))
pygame.draw.arc(screen, BLACK, [[421, 477], [10, 11]], dtr(270), dtr(90))
pygame.draw.arc(screen, BLACK, [[421, 498], [10, 11]], dtr(270), dtr(90))

# Foot Contact
pygame.draw.arc(screen, BLACK, [[300, 475], [130, 81]], dtr(186), dtr(249), 1)
pygame.draw.arc(screen, BLACK, [[298, 475], [130, 81]], dtr(298), dtr(354), 1)
pygame.draw.line(screen, BLACK, [336, 550], [336+58, 550])
pygame.draw.arc(screen, GREY, [[327, 499], [76, 64]], dtr(215), dtr(325), 1)

# Outer Bulb
pygame.draw.arc(screen, BLACK, [[287, 366], [25, 68]], dtr(180), dtr(255))      # Bulb to base left
pygame.draw.arc(screen, BLACK, [[417, 366], [25, 68]], dtr(285), dtr(5))        # Bulb to base right
pygame.draw.arc(screen, BLACK, [[237, 326], [51, 126]], dtr(350), dtr(65))      # Bulb body arc left
pygame.draw.arc(screen, BLACK, [[440, 326], [51, 126]], dtr(115), dtr(195))     # Bulb body arc right
pygame.draw.line(screen, BLACK, [227, 273], [227+45, 273+58])                   # Bulb body line left
pygame.draw.line(screen, BLACK, [502, 273], [502-47, 273+58])                   # Bulb body line right
pygame.draw.arc(screen, BLACK, [[204, 29], [322, 322]], dtr(329), dtr(213), 1)  # Bulb body

# Inner Bulb
pygame.draw.rect(screen, GREY, [[343, 337], [43, 94]])                      # Filament Base
pygame.draw.rect(screen, GREY, [[356, 260], [17, 77]])                      # Filament Rod
pygame.draw.rect(screen, GREY, [[352, 250], [25, 10]])                      # Filament Tip
pygame.draw.line(screen, BLACK, [314, 189], [314+32, 189+148])              # Filament Outer Left
pygame.draw.line(screen, BLACK, [416, 189], [416-32, 189+148])              # Filament Outer Right
pygame.draw.line(screen, BLACK, [342, 181], [342+13, 181+69])               # Filament Inner Left
pygame.draw.line(screen, BLACK, [387, 181], [387-13, 181+69])               # FIlament Inner Right
pygame.draw.arc(screen, GREY, [[287, 165], [56, 24]], dtr(268), dtr(345))   # Tungsten Left
pygame.draw.arc(screen, GREY, [[331, 155], [71, 31]], dtr(225), dtr(315))   # Tungsten Middle
pygame.draw.arc(screen, GREY, [[385, 165], [56, 24]], dtr(200), dtr(277))   # Tungsten Right

### Color

# Base
fill(screen, (301, 475), LIGHT_GREY)
fill(screen, (301, 496), LIGHT_GREY)
fill(screen, (301, 516), LIGHT_GREY)
fill(screen, (340, 540), LIGHT_GREY)
fill(screen, (340, 552), GREY)

pygame.display.flip()

### Animation

# Bulb
time.sleep(1)
fill(screen, (320, 100), YELLOW)
fill(screen, (320, 200), YELLOW)
fill(screen, (345, 190), YELLOW)
fill(screen, (390, 190), YELLOW)

# Light
for i in range(1, 350):
    pygame.draw.arc(screen, LIGHT, [[204-i, 29-i], [322+i*2, 322+i*2]], dtr(329), dtr(213), 1)
    pygame.draw.aaline(screen, LIGHT, [227-i, 273+i/2], [227+45-i, 273+58+i*5])
    pygame.draw.aaline(screen, LIGHT, [502+i, 273+i/2], [502-47+i, 273+58+i*5])
    time.sleep(0.01)
    pygame.display.flip()

pygame.event.clear()
while True:
    event = pygame.event.wait()
    if event.type == KEYDOWN:
        pygame.quit()
