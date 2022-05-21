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
        if self.is_tie_in_regular():
            result = self.tie_in_regular_score()
        if self.is_tie_in_advantage():
            result = "Deuce"

        player1_res = ""
        player2_res = ""
        if self.only_player1_has_points():
            player1_res = self.player1_simple_score()

            player2_res = "Love"
            result = player1_res + "-" + player2_res
        if self.only_player2_has_points():
            player2_res = self.player2_simple_score()

            player1_res = "Love"
            result = player1_res + "-" + player2_res

        if self.is_player1_winning_in_regular() or self.is_player2_winning_in_regular():
            player1_res = self.player1_simple_score()
            player2_res = self.player2_simple_score()
            result = player1_res + "-" + player2_res

        if self.is_player1_winning_in_advantage():
            result = "Advantage " + self.player1_name

        if self.is_player2_winning_in_advantage():
            result = "Advantage " + self.player2_name

        if self.has_player1_won_game():
            result = "Win for " + self.player1_name
        if self.has_player2_won_game():
            result = "Win for " + self.player2_name
        return result

    def player2_simple_score(self):
        player2_res = ""
        if self.player2_points == LOVE:
            player2_res = "Love"
        if self.player2_points == FIFTEEN:
            player2_res = "Fifteen"
        if self.player2_points == THIRTY:
            player2_res = "Thirty"
        if self.player2_points == FORTY:
            player2_res = "Forty"
        return player2_res

    def player1_simple_score(self):
        player1_res = ""
        if self.player1_points == LOVE:
            player1_res = "Love"
        if self.player1_points == FIFTEEN:
            player1_res = "Fifteen"
        if self.player1_points == THIRTY:
            player1_res = "Thirty"
        if self.player1_points == FORTY:
            player1_res = "Forty"
        return player1_res

    def has_player2_won_game(self):
        return (
            self.player2_points > FORTY
            and (self.player2_points - self.player1_points) >= 2
        )

    def has_player1_won_game(self):
        return (
            self.player1_points > FORTY
            and (self.player1_points - self.player2_points) >= 2
        )

    def is_player2_winning_in_advantage(self):
        return (
            self.player2_points > self.player1_points and self.player1_points >= FORTY
        )

    def is_player1_winning_in_advantage(self):
        return (
            self.player1_points > self.player2_points and self.player2_points >= FORTY
        )

    def is_player2_winning_in_regular(self):
        return (
            self.player2_points > self.player1_points and self.player2_points <= FORTY
        )

    def is_player1_winning_in_regular(self):
        return (
            self.player1_points > self.player2_points and self.player1_points <= FORTY
        )

    def only_player2_has_points(self):
        return self.player2_points > LOVE and self.player1_points == LOVE

    def only_player1_has_points(self):
        return self.player1_points > LOVE and self.player2_points == LOVE

    def is_tie_in_advantage(self):
        return (
            self.player1_points == self.player2_points and self.player1_points > THIRTY
        )

    def tie_in_regular_score(self):
        if self.player1_points == LOVE:
            result = "Love"
        if self.player1_points == FIFTEEN:
            result = "Fifteen"
        if self.player1_points == THIRTY:
            result = "Thirty"
        result += "-All"
        return result

    def is_tie_in_regular(self):
        return (
            self.player1_points == self.player2_points and self.player1_points < FORTY
        )

    def player1_score(self):
        self.player1_points += 1

    def player2_score(self):
        self.player2_points += 1
