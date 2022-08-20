import time
import random

def quick_sort(a_list, start, end):
    # list size is 1 or less (which doesn't make sense)
    if start >= end:
        return

    # Call the partition helper function to split the list into two section 
    # divided between a pivot point
    pivot = partitionStart(a_list, start, end)
    quick_sort(a_list, start, pivot-1)
    quick_sort(a_list, pivot+1, end)
        

def partitionStart(a_list, start, end):
    return partition(a_list, start, end)

def partition(a_list, start, end):
    # Select the first element as our pivot point
    pivot = a_list[start]
    
    # Start at the first element past the pivot point
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and a_list[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and a_list[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            # Swap the values
            a_list[low], a_list[high] = a_list[high], a_list[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    # Swap the values
    a_list[start], a_list[high] = a_list[high], a_list[start]

    return high


print("Quick Sort:")
# myList = [54,26,93,17,77,31]
myList = [x for x in range(1000)]
random.shuffle(myList)

# print(myList)
start_time = time.time()
quick_sort(myList,0,len(myList)-1)
end_time = time.time()
# print()
# print("Sorted Listed: ")
# print(myList)   

print(f"The execution time is: {end_time-start_time}")

# -- LAST ELEMENT AS PIVOT --
import sys
x=1500
sys.setrecursionlimit(x)

def last_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return last_sort(items_lower) + [pivot] + last_sort(items_greater)

print('Quick Sort (Last Elem Pivot):')

start_time = time.time()
last_sort(myList)
end_time = time.time()

print(f"The execution time is: {end_time-start_time}")

# -- RANDOM ELEMENT AS PIVOT --
def random_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop(random.randint(0, len(sequence)-1))

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return last_sort(items_lower) + [pivot] + last_sort(items_greater)

print('Quick Sort (Random Elem Pivot):')

start_time = time.time()
random_sort(myList)
end_time = time.time()

print(f"The execution time is: {end_time-start_time}")

# -- MEAN AS PIVOT --
def mean_sort(sequence):
    start = sequence[0]
    middle = sequence[int(len(sequence) / 2)]
    end = sequence[int(len(sequence) - 1)]

    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop(sequence.index(int((start + middle + end) / 3)))

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return last_sort(items_lower) + [pivot] + last_sort(items_greater)

print('Quick Sort (Mean Pivot):')

start_time = time.time()
mean_sort(myList)
end_time = time.time()

print(f"The execution time is: {end_time-start_time}")

# From what I can tell, testing with the different pivot methods that I found
# online, it looks like the first element pivot is the most efficient. The
# second most efficient that I found appears to be using the mean as the pivot
# as it usually completes between 0.012 and 0.018. Using a random element as the
# pivot can be efficient but is much more volatile than using the mean. The
# worst efficiency I found was using the last element as the pivot as it
# hovers between 0.025 and 0.041.