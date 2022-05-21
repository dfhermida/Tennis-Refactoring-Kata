LOVE = 0
FIFTEEN = 1
THIRTY = 2
FORTY = 3


class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def won_point(self):
        self.points += 1

    def score(self):
        return {LOVE: "Love", FIFTEEN: "Fifteen", THIRTY: "Thirty", FORTY: "Forty",}[
            self.points
        ]


class TennisGame1:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def won_point(self, player_name):
        if player_name == self.player1.name:
            self.player1.won_point()
        else:
            self.player2.won_point()

    def score(self):
        if self.is_tie():
            return (
                self.player1.score() + "-All"
                if self.player1.points < FORTY
                else "Deuce"
            )
        if self.is_advantage():
            return "Advantage " + self.whos_winning().name
        if self.is_win():
            return "Win for " + self.whos_winning().name
        return self.player1.score() + "-" + self.player2.score()

    def whos_winning(self):
        difference = self.player1.points - self.player2.points
        if difference > 0:
            return self.player1
        else:
            return self.player2

    def points_difference(self):
        return abs(self.player1.points - self.player2.points)

    def is_advantage(self):
        if self.player1.points <= FORTY and self.player2.points <= FORTY:
            return False

        return self.points_difference() < 2

    def is_win(self):
        if self.player1.points <= FORTY and self.player2.points <= FORTY:
            return False

        return self.points_difference() >= 2

    def is_tie(self):
        return self.player1.points == self.player2.points
