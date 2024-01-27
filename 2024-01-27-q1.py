import random

master_array = random.sample([num for num in range(100)], 50)

def is_cross(array):
    length = len(array)
    if length < 4:
        return False
    for i in range(3, length):
        if i-5 >= 0:
            if array[i] + array[i-4] >= array[i-2] and \
            array[i-1] + array[i-5] >= array[i-3] and \
            array[i-2] >= array[i-4] and \
            array[i-3] >= array[i-1]:
                return True
        if i-4 >= 0:
            if array[i] + array[i-4] >= array[i-2] and array[i-1] == array[i-3]:
                return True
        if i-3 >= 0:
            if array[i] >= array[i-2] and array[i-1] <= array[i-3]:
                return True
    return False


# Test cases:
array_1 = []

array_2 = [random.sample(master_array, 1)]

array_3 = [random.sample(master_array, 2)]

array_4 = [random.sample(master_array, 3)]

array_5 = [random.sample(master_array, 4)]

array_6 = sorted([random.sample(master_array, 10)])

array_7 = [3, 2, 1, 4] # True

array_8 = [2, 3, 4, 5, 6, 7, 8, 6, 5] # True

assert is_cross(array_1) == False
assert is_cross(array_2) == False
assert is_cross(array_3) == False
assert is_cross(array_4) == False
assert is_cross(array_5) == False
assert is_cross(array_6) == False
assert is_cross(array_7) == True
assert is_cross(array_8) == True
