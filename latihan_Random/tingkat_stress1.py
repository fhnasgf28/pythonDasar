def get_stress_ratings():
    ratings = {}
    try:
        ratings["work"] = int(input("Enter Your stress level rating for work (1-5): "))
        ratings["relationship"] = int(input("Enter Your stress level rating for relationships (1-5)"))
        ratings["health"] = int(input("Enter your stress level rating for health (1-5): "))
        return ratings
    except ValueError:
        pass


def calculate_stress_score(ratings):
    score = (ratings["work"] + ratings["relationship"] + ratings["health"]) / 3
    return score


def get_stress_category(score):
    if score <= 2:
        return "Low"
    elif score <= 3:
        return "Moderate"
    else:
        return "High"

# main program
ratings = get_stress_ratings()
score = calculate_stress_score(ratings)
category = get_stress_category(score)

print(f"Your overall stress level score is {score:.1f}")
print(f"You are experiencing {category} stress.")