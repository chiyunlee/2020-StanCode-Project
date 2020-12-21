"""
File: draw_line.py
Name:
-------------------------
This file shows how to use campy mouse event to
draw GLine and GOval
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10
window = GWindow()
count = 0
f_x = 0
f_y = 0
click1 = GOval(SIZE,SIZE)
click1.color = 'black'

def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(point)


def point(a):
    global count
    global f_x
    global f_y
    global click1
    count += 1
    if count % 2 == 1:
        window.add(click1, x=a.x - click1.width / 2, y=a.y - click1.height / 2)
        f_x = a.x
        f_y = a.y
    else:
        b_line = GLine(f_x, f_y, a.x, a.y)
        b_line.color = 'black'
        window.add(b_line)
        window.remove(click1)




















if __name__ == "__main__":
    main()
