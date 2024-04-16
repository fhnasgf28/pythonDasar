john_monthly_spending = [2689.56, 2770.38, 2394.04, 2099.91, 3182.20, 3267.12, 1746.83, 2545.72, 3328.20, 3147.30,
                         2462.61, 3890.45]

sam_monthly_spending = [1969.62, 3939.37, 2241.59, 3968.27, 3068.80, 1755.02, 3885.66, 2491.67, 3828.49, 3171.32,
                        2771.32, 3380.37]

month_john_spent_more = 0

for i in range(len(john_monthly_spending)):
    if john_monthly_spending[i] > sam_monthly_spending[i]:
        month_john_spent_more += 1

print("Number of month John spent more money than sam\t:", month_john_spent_more)