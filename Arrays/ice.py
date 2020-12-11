def maximum(arr):

    if len(arr) == 1:
        return
    mi = arr[0]
    for i in range(len(arr)):
        if arr[i] <= mi:
            mi = arr[i]
            index_mi = i

    ma = arr[index_mi]
    if index_mi == len(arr)-1:
        return 0
    else:
        for j in range(index_mi+1, len(arr)):
            if arr[j] > ma:
                ma = arr[j]
    if ma-mi > 0:
        return ma-mi
    else:
        return 0


def stock(arr):
    min_stock_price = arr[0]
    max_profit = 0
    for price in arr:
        min_stock_price = min(min_stock_price, price)
        comparision_profit = price-min_stock_price
        max_profit = max(max_profit, comparision_profit)
    return max_profit


print(maximum([100, 180, 260, 310, 40, 535, 695]))
print(stock([100, 180, 260, 310, 40, 535, 695]))
print(maximum([23, 12, 3, 10]))
print(stock([23, 12, 3, 10]))
