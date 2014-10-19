__author__ = 'Jonas'

# Implementation of classic arcade game Pong

import simpleguitk as simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [0, 0]
ball_vel = [0, 0]
paddle1_pos = 0
paddle2_pos = 0
paddle1_vel = 0
paddle2_vel = 0
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel  # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel = [random.randrange(2, 4), random.randrange(1, 2)]
    if direction is RIGHT:
        ball_vel[1] *= -1
    if direction is LEFT:
        ball_vel[1] *= -1
        ball_vel[0] *= -1


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(RIGHT)


def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1, "White")

    # update ball
    #Detect collision at top of screen
    if ball_pos[1] < BALL_RADIUS:
        ball_vel[1] *= -1
    #Detect collision at the bottom of screen
    if ball_pos[1] > HEIGHT - BALL_RADIUS:
        ball_vel[1] *= -1
    #Detect collision at the right gutter
    if ball_pos[0] > WIDTH - PAD_WIDTH - BALL_RADIUS:
        spawn_ball(LEFT)
    #Detect collision at the left gutter
    if ball_pos[0] < PAD_WIDTH + BALL_RADIUS:
        spawn_ball(RIGHT)
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'black', 'white')
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    #Draw the left paddle (paddle1)
    canvas.draw_polygon([[0, paddle1_pos], [PAD_WIDTH, paddle1_pos], [PAD_WIDTH, paddle1_pos + PAD_HEIGHT],
                         [0, paddle1_pos + PAD_HEIGHT]], 1, 'black', 'white')
    #Draw the right paddle (paddle2)
    canvas.draw_polygon([[WIDTH - PAD_WIDTH, paddle2_pos], [WIDTH, paddle2_pos], [WIDTH, paddle2_pos + PAD_HEIGHT],
                         [WIDTH - PAD_WIDTH, paddle2_pos + PAD_HEIGHT]], 1,
                        'black', 'white')
    # draw scores

def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -1
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = 1

    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = -1
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 1

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()

frame.start()
