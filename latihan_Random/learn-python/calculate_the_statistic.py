numbers = [10, 3, 5, 9, 18, 3, 0, 7]


def calculate_statistic(input_list):
    max_value = max(input_list)
    sum_values = sum(input_list)
    mean_values = sum_values / len(input_list)
    return max_value, sum_values, mean_values


result = calculate_statistic(numbers)

print('Maximum Value:', result[0])
print('Sum Of Value:', result[1])
print('Mean Value:', result[2])
