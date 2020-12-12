# Given an array rotate it by given number

def rotate_1(lst, d):
    # Time complexity O(n)
    # Space complexity O(n)

    new_lst = []
    l = len(lst)
    for i in range(len(lst)):
        new_lst.append(lst[(i+d) % l])

    return new_lst


def rotate_2(lst, d):
    l = len(lst)
    # By list partioning
    return lst[d % l:]+lst[:d % l]


array = [1, 2, 3, 4, 5, 6, 7]
d = -2
print(rotate_1(array, d))
print(rotate_2(array, d))


# Find element at index i after d rotation

def element_index(lst, d, i):
    l = len(lst)
    return lst[((d % l)+i) % l]


array = [1, 2, 3, 4, 5, 6, 7]
d = -2
i = 3
print(element_index(array, d, i))
