from turtle import Turtle
FONT = ("Impact", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self, player1, player2):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.name1 = player1
        self.name2 = player2
        self.update_scores()

    def write_start(self):
        self.goto(0, 0)
        self.write("PRESS \"ENTER\" TO START THE GAME", align="center", font=FONT)
        self.clear()

    def update_scores(self):
        self.clear()
        self.goto(-100, 240)
        self.write(f"{self.name1}: {self.l_score}", align="center", font=FONT)
        self.goto(100, 240)
        self.write(f"{self.name2}: {self.r_score}", align="center", font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scores()

    def r_point(self):
        self.r_score += 1
        self.update_scores()
