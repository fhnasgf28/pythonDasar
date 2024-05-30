with open('test.txt', 'r') as file:
    lines = file.readlines()

    # open new file in write mode

with open('new_file.txt', 'w') as fp:
    count =0

    for line in lines:
        if count == 4:
            count += 1
            continue
        else:
            fp.write(line)

        count += 1