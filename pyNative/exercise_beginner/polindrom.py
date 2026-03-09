def polindrom_number(number):
    print("Original Number", number)
    original_number = number

    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

#     check number
    if original_number == reverse_num:
        print('Given number polindrom')
    else:
        print("Given number is not polindrome")

polindrom_number(131)
polindrom_number(132)

