def calculate_average(scores):
    total_score = 0
    for score in scores:
        total_score += score
    average = total_score / len(scores)
    return average


scores = [75, 82, 91, 68, 96]
average_score = calculate_average(scores)
print(f"Rata-rata nilai ujian: {average_score: .2f}")
