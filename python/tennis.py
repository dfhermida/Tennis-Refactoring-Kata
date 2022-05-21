# -*- coding: utf-8 -*-
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
            return self.tie_score()
        elif self.is_advantage_or_win():
            return self.advantage_or_win_score()
        return self.regular_score()

    def regular_score(self):
        result = ""
        tempScore = 0
        for i in range(1, 3):
            if i == 1:
                tempScore = self.player1.points
            else:
                result += "-"
                tempScore = self.player2.points
            result += {
                LOVE: "Love",
                FIFTEEN: "Fifteen",
                THIRTY: "Thirty",
                FORTY: "Forty",
            }[tempScore]
        return result

    def advantage_or_win_score(self):
        minusResult = self.player1.points - self.player2.points
        if minusResult == 1:
            result = "Advantage " + self.player1.name
        elif minusResult == -1:
            result = "Advantage " + self.player2.name
        elif minusResult >= 2:
            result = "Win for " + self.player1.name
        else:
            result = "Win for " + self.player2.name
        return result

    def tie_score(self):
        return {
            LOVE: "Love-All",
            FIFTEEN: "Fifteen-All",
            THIRTY: "Thirty-All",
        }.get(self.player1.points, "Deuce")

    def is_advantage_or_win(self):
        return self.player1.points > FORTY or self.player2.points > FORTY

    def is_tie(self):
        return self.player1.points == self.player2.points


class TennisGame2:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.P1Score()
        else:
            self.P2Score()

    def score(self):
        result = ""
        if self.p1points == self.p2points and self.p1points < 3:
            if self.p1points == 0:
                result = "Love"
            if self.p1points == 1:
                result = "Fifteen"
            if self.p1points == 2:
                result = "Thirty"
            result += "-All"
        if self.p1points == self.p2points and self.p1points > 2:
            result = "Deuce"

        P1res = ""
        P2res = ""
        if self.p1points > 0 and self.p2points == 0:
            if self.p1points == 1:
                P1res = "Fifteen"
            if self.p1points == 2:
                P1res = "Thirty"
            if self.p1points == 3:
                P1res = "Forty"

            P2res = "Love"
            result = P1res + "-" + P2res
        if self.p2points > 0 and self.p1points == 0:
            if self.p2points == 1:
                P2res = "Fifteen"
            if self.p2points == 2:
                P2res = "Thirty"
            if self.p2points == 3:
                P2res = "Forty"

            P1res = "Love"
            result = P1res + "-" + P2res

        if self.p1points > self.p2points and self.p1points < 4:
            if self.p1points == 2:
                P1res = "Thirty"
            if self.p1points == 3:
                P1res = "Forty"
            if self.p2points == 1:
                P2res = "Fifteen"
            if self.p2points == 2:
                P2res = "Thirty"
            result = P1res + "-" + P2res
        if self.p2points > self.p1points and self.p2points < 4:
            if self.p2points == 2:
                P2res = "Thirty"
            if self.p2points == 3:
                P2res = "Forty"
            if self.p1points == 1:
                P1res = "Fifteen"
            if self.p1points == 2:
                P1res = "Thirty"
            result = P1res + "-" + P2res

        if self.p1points > self.p2points and self.p2points >= 3:
            result = "Advantage " + self.player1Name

        if self.p2points > self.p1points and self.p1points >= 3:
            result = "Advantage " + self.player2Name

        if (
            self.p1points >= 4
            and self.p2points >= 0
            and (self.p1points - self.p2points) >= 2
        ):
            result = "Win for " + self.player1Name
        if (
            self.p2points >= 4
            and self.p1points >= 0
            and (self.p2points - self.p1points) >= 2
        ):
            result = "Win for " + self.player2Name
        return result

    def SetP1Score(self, number):
        for i in range(number):
            self.P1Score()

    def SetP2Score(self, number):
        for i in range(number):
            self.P2Score()

    def P1Score(self):
        self.p1points += 1

    def P2Score(self):
        self.p2points += 1


class TennisGame3:
    def __init__(self, player1Name, player2Name):
        self.p1N = player1Name
        self.p2N = player2Name
        self.p1 = 0
        self.p2 = 0

    def won_point(self, n):
        if n == self.p1N:
            self.p1 += 1
        else:
            self.p2 += 1

    def score(self):
        if (self.p1 < 4 and self.p2 < 4) and (self.p1 + self.p2 < 6):
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            s = p[self.p1]
            return s + "-All" if (self.p1 == self.p2) else s + "-" + p[self.p2]
        else:
            if self.p1 == self.p2:
                return "Deuce"
            s = self.p1N if self.p1 > self.p2 else self.p2N
            return (
                "Advantage " + s
                if ((self.p1 - self.p2) * (self.p1 - self.p2) == 1)
                else "Win for " + s
            )
