"""
File: bouncing.py
Name:
-------------------------
This file simulate the free ball dropping down and bouncing up.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

VY = 0

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
ball.filled = True
ball.fill_color = 'black'
window.add(ball, START_X, START_Y)
no_restart = False
count = 3

def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(bouncing)


def bouncing(e):
    global VX
    global VY
    global DELAY
    global REDUCE
    global GRAVITY
    global no_restart
    global count
    for i in range(count):
        while ball.x <= window.width and not no_restart:
            ball.move(VX, VY)
            VY = VY + GRAVITY
            if ball.y >= window.height:
                VY = -VY * REDUCE
            pause(DELAY)
        window.add(ball, START_X, START_Y)
    no_restart = True

















if __name__ == "__main__":
    main()
