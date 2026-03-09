paul_friends = ["Mary", "Tim", "Mike", "Henry"]
tina_friends = ["Tim", "Susan", "Mary", "Josh"]

common_friends = []
for friend in paul_friends:
    if friend in tina_friends:
        common_friends.append(friend)

print("Common Friends\t:", common_friends)