poll_result = ["Python", "Java", "Javascript", "Python", "Javascript", "Python", "C", "Python", "Python", "C", "Javascript"]

vote_tally = {}
for language in poll_result:
    if language in vote_tally:
        vote_tally[language] += 1
    else:
        vote_tally[language] = 1
print("vote Tally\t:", vote_tally)