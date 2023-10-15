import turtle

FONT = ('Courier', 14, 'normal')

class Scoreboard(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as file:
            self.high_score = int(file.read())
            print(self.high_score)
        self.penup()
        self.color('PaleTurquoise')
        self.ht()
        self.update_scoreborad()

    def update_scoreborad(self):
        self.goto(0, 260)
        self.reset_scoreboard()
        self.write(arg=f"Your Score : {self.score}  High Score : {self.high_score}", move=False, align='center', font=FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(str(self.high_score))
                print(self.high_score)


    def game_over(self):
        self.score = 0
        self.clear()
        self.update_scoreborad()
        self.goto(0, 0)
        self.write(arg=f"GAME OVER!", move=False, align='center', font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreborad()
        self.reset_scoreboard()
