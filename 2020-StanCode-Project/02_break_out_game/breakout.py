"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.gui.events.mouse import onmousemoved,onmouseclicked,onmousedragged
from campy.graphics.gobjects import GLabel
import random


FRAME_RATE = 1000 / 60 # 120 frames per second.
NUM_LIVES = 3
count = 0
score_label = GLabel('Score:'+str(count))
score_label.font = '-30'
graphics = BreakoutGraphics(life=NUM_LIVES)


def main():
    onmouseclicked(start_move_ball)
    graphics.window.add(score_label, 0, score_label.height+10)


def start_move_ball(event):
    global count
    while 0 <= event.x <= graphics.window.width and 0 <= event.y <= graphics.window.height \
            and count < graphics.brick_amount and not graphics.no_restart and graphics.life >= 0:
        pause(FRAME_RATE)
        graphics.ball.move(graphics.get_dx(), graphics.get_dy())
        obj1 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
        obj2 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y)
        obj3 = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height)
        obj4 = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                             graphics.ball.y + graphics.ball.height)
        if obj1 is not None:
            if obj1 is not graphics.paddle and obj1 is not score_label:
                graphics.remove_brick(obj1)
                count += 1
                score_label.text = 'Score: ' + str(count)
            elif obj1 is graphics.paddle and obj1 is not score_label and graphics.ball_touch_paddle_check:
                graphics.bouncing_dy()
                graphics.ball_touch_paddle_check = False
            if graphics.ball.y >= graphics.window.height/2:
                graphics.ball_touch_paddle_check = True

        elif obj2 is not None:
            if obj2 is not graphics.paddle and obj2 is not score_label:
                graphics.remove_brick(obj2)
                count += 1
                score_label.text = 'Score: ' + str(count)
            elif obj2 is graphics.paddle and obj2 is not score_label:
                graphics.bouncing_dy()
                graphics.ball_touch_paddle_check = False
            if graphics.ball.y >= graphics.window.height / 2:
                graphics.ball_touch_paddle_check = True

        elif obj3 is not None:
            if obj3 is not graphics.paddle and obj3 is not score_label:
                graphics.remove_brick(obj3)
                count += 1
                score_label.text = 'Score: ' + str(count)
            elif obj3 is graphics.paddle and obj3 is not score_label:
                graphics.bouncing_dy()
                graphics.ball_touch_paddle_check = False
            if graphics.ball.y >= graphics.window.height / 2:
                graphics.ball_touch_paddle_check = True

        elif obj4 is not None:
            if obj4 is not graphics.paddle and obj4 is not score_label:
                graphics.remove_brick(obj4)
                count += 1
                score_label.text = 'Score: ' + str(count)
            elif obj4 is graphics.paddle and obj4 is not score_label:
                graphics.bouncing_dy()
                graphics.ball_touch_paddle_check = False
            if graphics.ball.y >= graphics.window.height / 2:
                graphics.ball_touch_paddle_check = True

        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.bouncing_dx()
        if graphics.ball.y <= 0:
            graphics.bouncing_dy()
        if count == graphics.brick_amount:
            graphics.finish_game()
            graphics.remove_ball_paddle()
        if graphics.ball_outside_window():
            graphics.life -= 1
            graphics.set_ball_position()
            if graphics.life <= 0:
                graphics.game_over()
                graphics.no_restart = True
            break




    # return life






if __name__ == '__main__':
    main()
