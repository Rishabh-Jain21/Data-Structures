'''
Given an integer array,Output all unique pairs that sum to a specific value k
'''

def pair_sum_2(arr,k):
    """
    Iterating over all pairs to find target sum
    
    Time complexity O(n^2)
    Space complexity O(n^2)
    """
    if(len(arr) < 2):
        return
    answers =set()
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if (arr[i] + arr[j])==k:
                answers.add((i,j))
                
    return len(answers)

def pair_sum(arr, k):
    """
    Iterating over the array and check if difference of target and current number is already observed in the array.
    
    Time complexity O(n^2)
    Space complexity O(n)
    """
    if(len(arr) < 2):
        return

    seen = set()
    output = set()

    for num in arr:
        target = k-num

        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))

    return len(output)


print(pair_sum([1, 3, 2, 2], 4))
print(pair_sum_2([1, 3, 2, 2], 4))