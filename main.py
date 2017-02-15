from display import *
from draw import *

screen = new_screen()

color = [255, 0, 0]

'''
draw_line(screen, 0, 0, 300, 200, color)
draw_line(screen, 0, 0, 300, 450, color2)
'''

draw_line(screen, 200, 200, 200, 0, color) #vertical

y=0
while (y < 500):
    color[1] = color[1] + 30 % 256
    color[2] = color[2] + 20 % 256
    draw_line(screen, 200, 200, 250, y, color)
    y+=50

display(screen)
save_extension(screen, 'img.png')
