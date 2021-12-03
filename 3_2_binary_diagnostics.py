"""Advent of Code Day 3 Part 2"""

data = open('3_data.txt', 'r')
binary_data = [line.rstrip('\n') for line in data.readlines()]
data.close()

def bit_criteria(binaries, bit_position, common_value):

    value = 0
    # sum the values of the same bit of each binary
    for binary in binaries: 
        value += int(binary[bit_position])
    # find avarage value
    value /= len(binaries)
    # return bit_criteria
    
    if common_value == 'most':
        if value >= 0.5:
            bit_critera = 1
        else:
            bit_critera = 0
    elif common_value == 'least':
        if value >= 0.5:
            bit_critera = 0
        else:
            bit_critera = 1
    
    return str(bit_critera)

def find_rating(binary_list, common_value):

    # make copy of input data as it should be changed
    binaries = binary_list[:]
    #iterate through the different bits in a binary
    for i in range(len(binaries[0])):
        # iterate though each binary in the binaries
        j = 0
        criteria = bit_criteria(binaries, i, common_value)
        while j < len(binaries):
            if binaries[j][i] != criteria:
                del binaries[j]
                if len(binaries) == 1:
                    return binaries[0]
            else:
                j += 1

o_rating = int(find_rating(binary_data, 'most'),2)
co2_rating = int(find_rating(binary_data, 'least'),2)

print(f'oxygen generator rating: {o_rating}')
print(f'CO2 scrubber rating: {co2_rating}')
print(f'Life Support Rating: {o_rating * co2_rating}')

# test data = 230
# data = 3765399