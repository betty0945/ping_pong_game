from scoreboard import Scoreboard
from paddle import Paddle
from turtle import Screen
from ball import Ball
import keyboard
import game_art as gm
import random

print(gm.art)
print("WELCOME TO THE GAME OF PONG\n\n The rules are simple:\n"
      "* To move the paddles up and down, players should press the keys \"w\", \"s\" and the arrows \"UP\", \"DOWN\","
      "respectively \n"
      "* To quit the game press the \"Esc\" key")

name1 = input("\nEnter the first player's name (they will play on the left): ")
name2 = input("Enter the second player's name (they will play on the right): ")
print(f"THE GAME IS ON! SWITCH THE WINDOWS\n\n\t\t{gm.luck}\n\n")

screen = Screen()
scoreboard = Scoreboard(name1, name2)


def colors():
    """Changes the background color every time the ball hits a wall"""

    colors_list = ["#458B74", "#9C661F", "#A52A2A", "#EEC591", 	"#CDC9A5", "#EEA2AD",
                   "#458B00", "#FF7256", "#9932CC", "#8FBC8F", "#EEB422", 	"#607B8B",
                   "#8470FF", "#CDCD00"]
    rand_color = random.choice(colors_list)
    return rand_color


# Setting up the screen
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

# Positioning paddles
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
l_paddle.color("blue")
r_paddle.color("blue")

# Connecting keys to "UP", "DOWN" functions
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, key="w")
screen.onkey(l_paddle.down, key="s")

# Setting up the ball
ball = Ball()
ball.color("white")
game_is_on = True

# Makes sure the game doesn't start before the player is ready
while not keyboard.is_pressed("enter"):
    scoreboard.write_start()
scoreboard.update_scores()

while game_is_on:
    screen.update()
    ball.move_ball()

    # Detect collision with the wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
        ball.change_color(1)
        random_color = colors()
        screen.bgcolor(random_color)

    # Detect collision with the right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_x()
        ball.change_color(1)

    # Detect collision with the left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
        ball.change_color(1)

    # Detects if the ball goes out of bounds Right Player
    if ball.xcor() > 390:
        ball.reset_position()
        scoreboard.l_point()

    # Detects if the ball goes out of bounds Left Player
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.r_point()

    if keyboard.is_pressed("escape"):
        game_is_on = False


def the_end():
    player1_score = scoreboard.l_score
    player2_score = scoreboard.r_score
    dif = abs(player1_score - player2_score)

    if dif <= 3:
        print("WOW!!! THAT WAS A CLOSE ONE!")
    else:
        print("THAT WAS A GREAT PLAY!!")
    print(f"\nPlayer scores are:\n{name1}: {player1_score}\n{name2}: {player2_score}")
    print(gm.game_over)


the_end()

