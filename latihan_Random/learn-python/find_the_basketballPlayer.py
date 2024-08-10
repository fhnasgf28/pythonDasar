football_players = {"Eve", "Tom", "Richard", "Peter"}
volleyball_players = {"Jack", "Hugh", "Peter", "Sam"}
basketball_players = {"Eve", "Richard", "Jessica", "Sam", "Michael"}

basketball_only_players = basketball_players - (football_players | volleyball_players)
print("Basketball Only Players\t:", basketball_only_players)