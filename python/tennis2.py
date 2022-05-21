LOVE = 0
FIFTEEN = 1
THIRTY = 2
FORTY = 3

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
        if self.player1_points == self.player2_points and self.player1_points < FORTY:
            if self.player1_points == LOVE:
                result = "Love"
            if self.player1_points == FIFTEEN:
                result = "Fifteen"
            if self.player1_points == THIRTY:
                result = "Thirty"
            result += "-All"
        if self.player1_points == self.player2_points and self.player1_points > THIRTY:
            result = "Deuce"

        player1_res = ""
        player2_res = ""
        if self.player1_points > LOVE and self.player2_points == LOVE:
            if self.player1_points == FIFTEEN:
                player1_res = "Fifteen"
            if self.player1_points == THIRTY:
                player1_res = "Thirty"
            if self.player1_points == FORTY:
                player1_res = "Forty"

            player2_res = "Love"
            result = player1_res + "-" + player2_res
        if self.player2_points > LOVE and self.player1_points == LOVE:
            if self.player2_points == FIFTEEN:
                player2_res = "Fifteen"
            if self.player2_points == THIRTY:
                player2_res = "Thirty"
            if self.player2_points == FORTY:
                player2_res = "Forty"

            player1_res = "Love"
            result = player1_res + "-" + player2_res

        if self.player1_points > self.player2_points and self.player1_points <= FORTY:
            if self.player1_points == THIRTY:
                player1_res = "Thirty"
            if self.player1_points == FORTY:
                player1_res = "Forty"
            if self.player2_points == FIFTEEN:
                player2_res = "Fifteen"
            if self.player2_points == THIRTY:
                player2_res = "Thirty"
            result = player1_res + "-" + player2_res
        if self.player2_points > self.player1_points and self.player2_points <= FORTY:
            if self.player2_points == THIRTY:
                player2_res = "Thirty"
            if self.player2_points == FORTY:
                player2_res = "Forty"
            if self.player1_points == FIFTEEN:
                player1_res = "Fifteen"
            if self.player1_points == THIRTY:
                player1_res = "Thirty"
            result = player1_res + "-" + player2_res

        if self.player1_points > self.player2_points and self.player2_points >= FORTY:
            result = "Advantage " + self.player1_name

        if self.player2_points > self.player1_points and self.player1_points >= FORTY:
            result = "Advantage " + self.player2_name

        if (
            self.player1_points > FORTY
            and self.player2_points >= LOVE
            and (self.player1_points - self.player2_points) >= 2
        ):
            result = "Win for " + self.player1_name
        if (
            self.player2_points > FORTY
            and self.player1_points >= LOVE
            and (self.player2_points - self.player1_points) >= 2
        ):
            result = "Win for " + self.player2_name
        return result

    def player1_score(self):
        self.player1_points += 1

    def player2_score(self):
        self.player2_points += 1
