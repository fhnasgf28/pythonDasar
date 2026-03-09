from match import Match

class League:
    def __init__(self):
        self.scores = {}
    
    def add_match(self, match: Match):
        for team in [match.home_team, match.away_team]:
            if team not in self.scores:
                self.scores[team] = 0
        
        result = match.get_result()

        if result == "draw":
            self.scores[match.home_team] += 1
            self.scores[match.away_team] += 1
        else:
            self.scores[result] += 3
    
    def get_leaderboard(self):
        return sorted(self.scores.items(), key=lambda x: x[1], reverse=True)
    
    def show_leaderboard(self):
        print("klasemen sementara:")
        for i, (team, points) in enumerate(self.get_leaderboard(), start=1):
            print(f"{i}. {team}: {points} point")
