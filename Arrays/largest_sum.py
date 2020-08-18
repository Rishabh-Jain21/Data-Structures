'''
Find largest continuous sum in an array os positive and negative integers'''


def large_cont_sum(arr):
    if len(arr) == 0:
        return 0
    current_sum = max_sum = 0

    for num in arr:
        current_sum = current_sum+num
        if current_sum >= max_sum:
            max_sum = current_sum

    return max_sum


print(large_cont_sum([1, 2, -1, 3, 4, -1]))  # 9
print(large_cont_sum([1, 2, -1, 3, 4, 10, 10, -10, -1]))  # 29
print(large_cont_sum([1, -1, ]))  # 1
