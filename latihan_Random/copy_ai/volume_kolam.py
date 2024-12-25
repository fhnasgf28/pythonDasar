def calculate_volume(length, width, height):
    return length * width * height

# input data from the user
length = float(input("Enter the length of the pool (in meters): "))
width = float(input("Enter the width of the pool (in meters): "))
height = float(input("Enter the height of the pool (in meters): "))

# calculate the volume of the pool
volume= calculate_volume(length, width, height)

# display the result
print("The volume of the pool is {:.2f} cubic meters.".format(volume))