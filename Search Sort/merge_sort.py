def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0  # for left half
        j = 0  # for right half
        k = 0  # track for final array

        while i < len(left_half) and j < len(right_half):

            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i = i+1
            else:
                arr[k] = right_half[j]
                j = j+1
            k = k+1
        while i < len(left_half):
            arr[k] = left_half[i]
            k = k+1
            i = i+1

        while j < len(right_half):
            arr[k] = right_half[j]
            k = k+1
            j = j+1
    print("Merging array ", arr)


arr = [11, 2, 5, 4, 7, 56, 2, 12, 23]
merge_sort(arr)
print(arr)
