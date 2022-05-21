class TennisGame2:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score()
        else:
            self.player2_score()

    def score(self):
        result = ""
        if self.player1_points == self.player2_points and self.player1_points < 3:
            if self.player1_points == 0:
                result = "Love"
            if self.player1_points == 1:
                result = "Fifteen"
            if self.player1_points == 2:
                result = "Thirty"
            result += "-All"
        if self.player1_points == self.player2_points and self.player1_points > 2:
            result = "Deuce"

        P1res = ""
        P2res = ""
        if self.player1_points > 0 and self.player2_points == 0:
            if self.player1_points == 1:
                P1res = "Fifteen"
            if self.player1_points == 2:
                P1res = "Thirty"
            if self.player1_points == 3:
                P1res = "Forty"

            P2res = "Love"
            result = P1res + "-" + P2res
        if self.player2_points > 0 and self.player1_points == 0:
            if self.player2_points == 1:
                P2res = "Fifteen"
            if self.player2_points == 2:
                P2res = "Thirty"
            if self.player2_points == 3:
                P2res = "Forty"

            P1res = "Love"
            result = P1res + "-" + P2res

        if self.player1_points > self.player2_points and self.player1_points < 4:
            if self.player1_points == 2:
                P1res = "Thirty"
            if self.player1_points == 3:
                P1res = "Forty"
            if self.player2_points == 1:
                P2res = "Fifteen"
            if self.player2_points == 2:
                P2res = "Thirty"
            result = P1res + "-" + P2res
        if self.player2_points > self.player1_points and self.player2_points < 4:
            if self.player2_points == 2:
                P2res = "Thirty"
            if self.player2_points == 3:
                P2res = "Forty"
            if self.player1_points == 1:
                P1res = "Fifteen"
            if self.player1_points == 2:
                P1res = "Thirty"
            result = P1res + "-" + P2res

        if self.player1_points > self.player2_points and self.player2_points >= 3:
            result = "Advantage " + self.player1_name

        if self.player2_points > self.player1_points and self.player1_points >= 3:
            result = "Advantage " + self.player2_name

        if (
            self.player1_points >= 4
            and self.player2_points >= 0
            and (self.player1_points - self.player2_points) >= 2
        ):
            result = "Win for " + self.player1_name
        if (
            self.player2_points >= 4
            and self.player1_points >= 0
            and (self.player2_points - self.player1_points) >= 2
        ):
            result = "Win for " + self.player2_name
        return result

    def set_player1_score(self, number):
        for i in range(number):
            self.player1_score()

    def set_player2_score(self, number):
        for i in range(number):
            self.player2_score()

    def player1_score(self):
        self.player1_points += 1

    def player2_score(self):
        self.player2_points += 1
