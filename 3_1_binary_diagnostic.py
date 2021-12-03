"""Advent of Code Day 3 Binary Diagnostic Part 1"""

# prepare data
data = open('3_test_data.txt', 'r')
binaries = [line.rstrip('\n') for line in data.readlines()]
data.close()

# numberr of binary numbers in binaries
bin_num = len(binaries)
# how many bits in each binary number 
bits = len(binaries[0])

gamma_rate = ''
epsilon_rate = ''

# iterate through each bit of a binary
for i in range(bits):
    value = 0
    # sum the values of the same bit of each binary
    for binary in binaries: 
        value += int(binary[i])
    # find avarage value
    value /= bin_num
    # add appropraite bit to the gamma and epsilon rate
    if value >= 0.5:
        gamma_rate += ('1')
        epsilon_rate += ('0')
    else:
        gamma_rate += ('0')
        epsilon_rate += ('1')

power_consumption = int(gamma_rate,2) * int(epsilon_rate,2)

print(power_consumption)
# test data: power consumption = 198
# dataL: power consumption = 3549854

