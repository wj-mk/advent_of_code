
# geting data ready
data = open("1_data.txt", "r")
measurements = []
for number in data:
    measurements.append(int(number))

# performing three-measurement slding window additions to make new list
measurement_sums = []
for i, measure in enumerate(measurements):
    measurement_sums.append(sum(measurements[i:i+3]))
        
increases = 0
for i, measure in enumerate(measurement_sums):
    if measure > measurement_sums[i-1]:
        increases += 1
    
print(increases)

# Answer returned is 1429

data.close()