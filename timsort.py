import random
import time

def insertion(unsorted):
    for i in range(1, len(unsorted)):
        value = unsorted[i]
        j = i-1
        while j >= 0 and value < unsorted[j]:
                unsorted[j+1] = unsorted[j]
                unsorted[j] = value
                j -= 1
    return unsorted

# https://github.com/graphoarty/scripts/blob/master/Sorting%20Algorithms/tim_sort.py
def Merge(L_arr, R_arr):

    L_pointer = 0
    R_pointer = 0
    temp_arr = []

    while L_pointer < len(L_arr) and R_pointer < len(R_arr):
        if L_arr[L_pointer] < R_arr[R_pointer]:
            temp_arr.append(L_arr[L_pointer])
            L_pointer = L_pointer + 1
        else:
            temp_arr.append(R_arr[R_pointer])
            R_pointer = R_pointer + 1
        # else:
        #     temp_arr.append(L_arr[L_pointer])
        #     temp_arr.append(R_arr[R_pointer])
        #     L_pointer = L_pointer + 1
        #     R_pointer = R_pointer + 1

    temp_arr.extend(L_arr[L_pointer:])
    temp_arr.extend(R_arr[R_pointer:])

    return temp_arr

def timsort():
    RUN = 32
    for x in range(0, len(arr), RUN):
        arr[x : x + RUN] = insertion(arr[x : x + RUN])

    nextRUN = RUN
    while nextRUN < len(arr):
        for x in range(0, len(arr), 2 * nextRUN):
            arr[x : x + 2 * nextRUN] = Merge(arr[x : x + nextRUN], arr[x + nextRUN: x + 2 * nextRUN])
        nextRUN = nextRUN * 2


arr = []
for x in range(0, 1000):
    arr.append(random.randint(0, 100))
print(arr)
start_time = time.time()
timsort()
print("--- %s seconds ---" % (time.time() - start_time))
print(arr)
