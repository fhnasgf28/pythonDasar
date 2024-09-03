def read_data_from_file(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            name, age, gender = line.strip().split(',')
            data.append({'name': name, 'age': int(age), 'gender': gender})
            return data

# read the data from the file
path_txt = r'/mnt/7C7452557452126E/pythonDasar/latihan_Random/txt/data.txt'
data = read_data_from_file(path_txt)

# print the data:

for person in data:
    print(f"Name: {person['name']}, Age: {person['age']}, Gender: {person['gender']}")