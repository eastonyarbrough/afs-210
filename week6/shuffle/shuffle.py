import random

# Allow user to input ordered list
usr_lst = input('Please provide a sorted list of numbers: ')
stringified_lst = usr_lst.strip('][').split(', ')
parsed_lst = []
shuffled_lst = []

# Parse list from user into usable format
def parse(lst):
    if len(lst) > 0:
        parsed_lst.append(int(lst[0]))
        lst.pop(0)
        return parse(lst)
    return
parse(stringified_lst)

# -- SHUFFLE ALGORITHM --
# The time complexity is O(n) because the algorithm must examine each
# item in the list and the time increases linearly with the size of
# the data that is input into the algorithm.
def shuffle(lst):
    temp = lst.copy()
    if len(temp) > 0:
        elem = temp.pop(random.randint(0, len(temp)-1))
        shuffled_lst.append(elem)
        return shuffle(temp)
    else:
        print(shuffled_lst)
        shuffled_lst.clear()

# Output of application showing list prior to shuffle and after.
print('Before Shuffle: ')
print(f'{parsed_lst}')

print('Shuffled: ')
shuffle(parsed_lst)
shuffle(parsed_lst)
shuffle(parsed_lst)
shuffle(parsed_lst)
shuffle(parsed_lst)