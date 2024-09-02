# Define a function to get the stress level ratings from the user
def get_stress_ratings():
    ratings = {}
    try:
        # Get the stress level ratings for work, relationships, and health
        ratings["work"] = int(input("Enter your stress level rating for work (1-5): "))
        ratings["relationships"] = int(input("Enter your stress level rating for relationships (1-5): "))
        ratings["health"] = int(input("Enter your stress level rating for health (1-5): "))
        return ratings
    except ValueError:
        # (TO DO: handle the error and prompt the user to try again)
        pass

# Define a function to calculate the overall stress level score
def calculate_stress_score(ratings):
    score = (ratings["work"] + ratings["relationships"] + ratings["health"]) / 3
    return score

# Define a function to determine the stress level category
def get_stress_category(score):
    if score <= 2:
        return "low"
    elif score <= 3:
        return "moderate"
    else:
        return "high"

# Main program
ratings = get_stress_ratings()
score = calculate_stress_score(ratings)
category = get_stress_category(score)
print(f"Your overall stress level score is {score:.1f}")
print(f"You are experiencing {category} stress.")