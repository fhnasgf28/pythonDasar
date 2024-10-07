monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30, 2462.61, 3890.45]

first_semester_total = 0
second_semester_total = 0

for index, expense in enumerate(monthly_spending):
    if index < 6:
        first_semester_total += expense
    else:
        second_semester_total += expense

first_semester_avg = first_semester_total / 6
second_semester_avg = second_semester_total / 6

print("Average expenses for the first semester \t:", first_semester_avg)
print("Average expenses for the first semester \t:", second_semester_avg)
