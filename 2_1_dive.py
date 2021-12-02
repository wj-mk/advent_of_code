"""Advent of Code 2021 Day 2 Dive, Problem 1"""

# get data and process
data = open("2_data.txt", "r")
movements = []
for line in data:
    # for each line split into direction and magitude
    direction, magnitude = line.split()
    # add as list to movements
    movements.append((direction,int(magnitude)))
data.close()

horizontal = 0
depth = 0

for movement in movements:
    
    direction = movement[0]
    magnitude = movement[1]
    
    if direction == 'forward':
        horizontal += magnitude
    elif direction == 'down':
        depth += magnitude
    elif direction == 'up':
        depth -= magnitude

print(horizontal*depth)