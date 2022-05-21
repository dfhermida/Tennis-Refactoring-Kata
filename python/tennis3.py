LOVE = 0
FIFTEEN = 1
THIRTY = 2
FORTY = 3


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
        if self.is_regular_game():
            simple_score = ["Love", "Fifteen", "Thirty", "Forty"]
            result = simple_score[self.player1_points]
            if self.is_tie():
                result = result + "-All"
            else:
                result = result + "-" + simple_score[self.player2_points]
            return result
        else:
            if self.is_tie():
                return "Deuce"
            
            winning = self.whos_winning_name()
            
            if self.not_enough_advantage_to_win():
                return "Advantage " + winning 
            return "Win for " + winning

    def whos_winning_name(self):
        if self.player1_points > self.player2_points:
            return self.player1_name
        return self.player2_name

    def not_enough_advantage_to_win(self):
        return (self.player1_points - self.player2_points) * (
            self.player1_points - self.player2_points
        ) == 1

    def is_tie(self):
        return self.player1_points == self.player2_points

    def is_regular_game(self):
        return (self.player1_points <= FORTY and self.player2_points <= FORTY) and (
            self.player1_points != FORTY or self.player2_points != FORTY)
