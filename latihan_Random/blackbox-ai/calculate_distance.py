def calculate_distance(speed, time):
    distance = speed * time
    return distance

speed = float(input("Enter speed (km/h): "))
time = float(input("Enter time(hours): "))

# calculate and display the distance
distance = calculate_distance(speed, time)
print("The distance traveled is {: .2f}km.".format(distance))
print('nama saya ffarhan assegaf')