from match import Match
from legue import League

league = League()

match1 = Match("Persija", "Arema", 2, 1)
match2 = Match("Persebaya", "Persib", 1, 1)
match3 = Match("Persija", "Persib", 0, 3)
match4 = Match("Arema", "Persebaya", 1, 2)

# Input ke liga
for m in [match1, match2, match3, match4]:
    league.add_match(m)

league.show_leaderboard()