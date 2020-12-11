# Given a sorted array of integers,return indices of the two numbers such that they add upp to a specific target

def indices(array_list, target_sum):
    i = 0
    j = len(array_list)-1
    while i < j:
        if array_list[i]+array_list[j] == target_sum:
            return i, j
        elif array_list[i]+array_list[j] < target_sum:
            i = i+1
        elif array_list[i]+array_list[j] > target_sum:
            j = j-1
    return None


lst = [1, 3, 5, 6, 8]
target = 10
print(indices(lst, target))
