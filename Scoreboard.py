from turtle import Turtle


class Scoreboard (Turtle):

    def __init__(self):
        super().__init__()
        self.color('grey')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        print(self.r_score)
        self.update_scoreboard()



    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.r_score, align='center', font=('Courier', 80, 'normal'))

    def update_rscore(self):
        self.r_score += 1
        print(self.r_score)
        self.update_scoreboard()

    def update_lscore(self):
        self.l_score += 1
        self.update_scoreboard()

