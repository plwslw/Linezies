from display import *
import math 

def draw_line(screen, x0, y0, x1, y1, color):
    dx = x1 - x0
    dy = y1 - y0

    if (dx < 0):
        dx, dy = -1*dx, -1*dy
    if (math.fabs(dx) > math.fabs(dy)):
        if (dy > 0):
            octant1( screen, x0, y0, x1, y1, color )
        else:
            octant8( screen, x0, y0, x1, y1, color )

    else:
        if (dy > 0):
            octant2( screen, x0, y0, x1, y1, color )
        else:
            octant7( screen, x0, y0, x1, y1, color )
            
def octant1( screen, x0, y0, x1, y1, color ):
    A = y1 - y0
    B = -(x1 - x0)
    
    x = x0
    y = y0
    d = 2*A + B

    while x <= x1:
        plot (x, y, color, screen)
        if d>0:
            y+=1
            d+=2*B
        x+=1
        d+=2*A

def octant2( screen, x0, y0, x1, y1, color):
    A = y1 - y0
    B = -(x1 - x0)
    
    x = x0
    y = y0
    d = A + 2*B

    while y <= y1:
        plot( screen, color, x, y)
        if d<0:
            x+=1
            d+=2*A
        y+=1
        d+=2*B

def octant7( screen, x0, y0, x1, y1, color):
    A = y1 - y0
    B = -(x1 - x0)
    
    x = x0
    y = y0
    d = A - 2*B

    while y >= y1:
        plot( screen, color, x, y)
        if d>0:
            x+=1
            d+=2*A
        y-=1
        d-=2*B
        
def octant8( screen, x0, y0, x1, y1, color ):
    A = y1 - y0
    B = -(x1 - x0)
    
    x = x0
    y = y0
    d = 2*A - B

    while x <= x1:
        plot( screen, color, x, y)
        if d<0:
            y-=1
            d-=2*B
        x+=1
        d+=2*A
