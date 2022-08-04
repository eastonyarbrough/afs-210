# Binary search function
def binary_search(list, item):
    total_size = len(list)
    mid_index = (total_size / 2)
    if (list[0] > item or list[int(total_size - 1)] < item):
        return False
    else:
        if list[int(mid_index)] == item:
            return True
        elif list[int(mid_index)] > item:
            cut_list = list[:int(mid_index)]
            return binary_search(cut_list, item)
        elif list[int(mid_index)] < item:
            cut_list = list[int(mid_index):]
            return binary_search(cut_list, item)

# Allow user to input list and target
usr_lst = input('Provide an ordered list of numbers to search: ')
stringified_lst = usr_lst.strip('][').split(', ')
parsed_lst = []

# Parse list from user for search function
def parse(list):
    if len(list) > 0:
        parsed_lst.append(int(list[0]))
        list.pop(0)
        return parse(list)
    return
parse(stringified_lst)

target = int(input('Enter the search criteria: '))

# Print search result
print(binary_search(parsed_lst, target))