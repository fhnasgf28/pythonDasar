scores = [('Mike', 10), ('Mike', 8), ('Mike', 6), ('John', 7), ('John', 8), ('John', 5), ('John', 8), ('Tom', 8), ('Tom', 9)]

total_scores = {}
for player, score in scores:
    if player in total_scores:
        total_scores[player] += score
    else:
        total_scores[player] = score
print("Total Scores", total_scores)