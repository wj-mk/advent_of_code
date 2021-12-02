data = open("1_data.txt", "r")

measurements = []

for number in data:
    measurements.append(int(number))

increases = 0
for i, measure in enumerate(measurements):
    if measure > measurements[i-1]:
        increases += 1
    
print(increases)

# Answer returned is 1400

data.close()