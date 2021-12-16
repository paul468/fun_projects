import math

def binarysearch(array, target:int):
    index = -1
    current_pos = math.ceil(len(array) / 2)
    curr_zero = 0
    curr_max = len(array) - 1
    while curr_zero <= curr_max:
        current_pos = math.ceil((curr_zero + curr_max) / 2)
        #print(array[curr_zero : curr_max], current_pos)
        if array[current_pos] <= target:
            curr_zero = current_pos + 1
            index = current_pos
        else:
            curr_max = current_pos - 1

    return index