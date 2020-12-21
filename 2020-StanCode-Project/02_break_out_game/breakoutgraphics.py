"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause
import random


BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10      # Number of rows of bricks.
BRICK_COLS = 10       # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5      # Maximum initial horizontal speed for the ball.
NUM_LIVES = 3


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout',life = NUM_LIVES):


        # Create a graphical window, with some extra space.
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle.
        self.paddle = GRect(paddle_width,paddle_height,x=(self.window_width-paddle_width)/2,y=self.window_height-paddle_offset+paddle_height)
        self.paddle.filled = True
        self.paddle.color = '#53414E'
        self.paddle.fill_color = '#53414E'
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius*2,ball_radius*2,x=self.window_width/2-ball_radius,y=self.window_height/2-ball_radius)
        self.ball.filled = True
        self.ball.fill_color = '#FF7146'
        self.window.add(self.ball,self.window_width/2-ball_radius, self.window_height/2-ball_radius)

        # Default initial velocity for the ball.
        self.__dx = 0
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)

        # Initialize our mouse listeners.
        self.no_restart = False  # to switch on the game
        self.count = 0
        self.life = NUM_LIVES

        onmousemoved(self.move_paddle)
        onmouseclicked(self.move_ball)

        # Draw bricks.
        for i in range(brick_rows):
            for j in range(brick_cols):
                if j % 2 == 0:
                    self.brick = GRect(brick_width, brick_height,x= i*(brick_width+brick_spacing),y=brick_offset+j*(brick_height+brick_spacing))
                    self.brick.filled = True
                    self.brick.fill_color = '#B2CFD6'
                    self.window.add(self.brick)
                else:
                    self.brick = GRect(brick_width, brick_height,x= i*(brick_width+brick_spacing),y=brick_offset+j*(brick_height+brick_spacing))
                    self.brick.filled = True
                    self.brick.fill_color = '#AED690'
                    self.window.add(self.brick)

        #game over label
        self.over_label = GLabel('Game Over',x=self.window_width/2,y=self.window_height/2)
        self.over_label.color = 'black'

        #finish label
        self.brick_amount = int(brick_rows * brick_cols)
        self.finish_label = GLabel('Congrats',x=self.window_width/2,y=self.window_height/2)
        self.finish_label.color = 'red'

        #ball touch paddle
        self.ball_touch_paddle_1 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        self.ball_touch_paddle_2 = self.window.get_object_at(self.ball.x+self.ball.width, self.ball.y+self.ball.height)
        self.ball_touch_paddle_check = True

        #bounce
        self.ten_point = GOval(ball_radius*2, ball_radius*2)
        self.ten_point.filled = True
        self.ten_point.fill_color = 'black'

    def drop_ten_point(self):
        self.ten_point.move(0, 5)

    def get_ten_point(self):
        if self.ten_point.y + self.ten_point.height >= self.paddle.y and self.paddle.x <= self.ten_point.x <= self.paddle.width-self.ten_point.width:
            self.count += 10



    def move_paddle(self, mouse):
        if 0 <= mouse.x <= self.window.width-self.paddle.width:
            self.paddle.x = mouse.x
            self.paddle.y = self.paddle.y

    def move_ball(self, event):
        if 0 <= event.x <= self.window.width and 0 <= event.y <= self.window.height and not self.no_restart:
            self.no_restart = True

    def get_dx(self):  # getter: let breakout.py to get the dx
        return self.__dx

    def get_dy(self):  # getter: let breakout.py to get the dy
        return self.__dy

    def ball_outside_window(self):
        ball_outside_window = self.ball.y > self.window.height
        return ball_outside_window

    def bouncing_dx(self):
        self.__dx = -self.__dx
        return self.__dx

    def bouncing_dy(self):
        self.__dy = -self.__dy
        return self.__dy

    def ball_touch_wall(self):
        ball_touch_x_left_wall = self.ball.x <= 0
        ball_touch_x_right_wall = self.ball.x + self.ball.width >= self.window.width
        ball_touch_y_top = self.ball.y <= 0
        return ball_touch_x_left_wall or ball_touch_x_right_wall or ball_touch_y_top

    def ball_touch_paddle(self):
        ball_touch_x_paddle = self.paddle.x - self.ball.width <= self.ball.x <= self.paddle.x + self.paddle.width
        ball_touch_y_paddle = self.paddle.y <= self.ball.y + self.ball.height <= self.paddle.y + self.paddle.height
        return ball_touch_x_paddle and ball_touch_y_paddle

    def ball_in_window(self):
        ball_in_window_x = self.ball.x == self.window_width/2-self.ball.width
        return ball_in_window_x

    def reset_ball(self):
        self.set_ball_position()
        while self.ball_outside_window():
            self.set_ball_position()
        self.set_ball_velocity()
        self.window.add(self.ball)

    def set_ball_velocity(self):
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED

    def set_ball_position(self):
        self.window.add(self.ball,self.window_width/2-self.ball.width, self.window_height/2-self.ball.height)

    def remove_brick(self, obj):
        self.window.remove(obj)
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = -self.__dy

    def game_over(self):
        self.window.add(self.over_label, x=self.window_width/2, y=self.window_height/2)
        self.window.remove(self.ball)

    def finish_game(self):
        self.window.add(self.finish_label, x=self.window_width/2,y=self.window_height/2)

    def remove_ball_paddle(self):
        self.window.remove(self.ball)
        self.window.remove(self.paddle)

