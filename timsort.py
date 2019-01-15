import random
import time

def insertion(unsorted):
    for i in range(1, len(unsorted)):
        value = unsorted[i] #start from the second index so we can compare it to the left
        j = i-1 #j will be "the left" comared to value
        while j >= 0 and value < unsorted[j]:
                unsorted[j+1] = unsorted[j]
                unsorted[j] = value
                j -= 1
        #while j isn't/is the mostleft and the right index is smaller than the left index
        #swap the right index and the left index
        #we want to check further to the left so decrement j by 1
    return unsorted

# https://github.com/graphoarty/scripts/blob/master/Sorting%20Algorithms/tim_sort.py
def Merge(L_arr, R_arr):

    L_pointer = 0 #both pointers start from 0
    R_pointer = 0
    temp_arr = []

    while L_pointer < len(L_arr) and R_pointer < len(R_arr):
        if L_arr[L_pointer] < R_arr[R_pointer]:
            temp_arr.append(L_arr[L_pointer])
            L_pointer = L_pointer + 1
        #if L_pointers is smaller, append it to temp_array
        #move the L_pointers by 1
        else:
            temp_arr.append(R_arr[R_pointer])
            R_pointer = R_pointer + 1
        #if L_pointers is smaller, append it to temp_array
        #move the L_pointers by 1

    temp_arr.extend(L_arr[L_pointer:])
    temp_arr.extend(R_arr[R_pointer:])
    #if one of the array is empty but the other one isn't
    #append all items left

    return temp_arr

def timsort():
    RUN = 5 #how big size to split the array
    arr = []
    for x in range(0, 10):
        arr.append(random.randint(0, 100))
    print(arr)
    for x in range(0, len(arr), RUN):
        arr[x : x + RUN] = insertion(arr[x : x + RUN]) #splitted arrays sorted using insertion sort

    nextRUN = RUN
    while nextRUN < len(arr):
        for x in range(0, len(arr), 2 * nextRUN):
            arr[x : x + 2 * nextRUN] = Merge(arr[x : x + nextRUN], arr[x + nextRUN: x + 2 * nextRUN]) #splitted arrays merge using merge sort
        nextRUN = nextRUN * 2

    return arr

def main():
    print(timsort())

if __name__ == '__main__':
    main()
