class TennisGame3:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_points += 1
        else:
            self.player2_points += 1

    def score(self):
        if (self.player1_points < 4 and self.player2_points < 4) and (
            self.player1_points + self.player2_points < 6
        ):
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            s = p[self.player1_points]
            return (
                s + "-All"
                if (self.player1_points == self.player2_points)
                else s + "-" + p[self.player2_points]
            )
        else:
            if self.player1_points == self.player2_points:
                return "Deuce"
            s = (
                self.player1_name
                if self.player1_points > self.player2_points
                else self.player2_name
            )
            return (
                "Advantage " + s
                if (
                    (self.player1_points - self.player2_points)
                    * (self.player1_points - self.player2_points)
                    == 1
                )
                else "Win for " + s
            )
