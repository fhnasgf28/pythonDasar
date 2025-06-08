class Match:
    def __init__(self, home_away, away_team, home_team, home_score, away_score):
        self.home_team = home_away
        self.away_team = away_team
        self.home_score = home_score
        self.home_team = home_team
        self.away_score = away_score
    
    def get_result(self):
        if self.home_score > self.away_score:
            return self.home_team
        elif self.home_score < self.away_score:
            return self.away_team
        else:
            return "draw"