def binary_search(li, target, low=None, high=None):
    # li = [range(100)]
    # target = 46 should be found on index 45 + 1
    target = int(target)
    if low is None:
        low = 0
    if high is None:
        high = len(li) - 1  # 101 - 1
    if high < low:
        # high will be kept getting divided. So high < low means the target is not in the list.
        print("Your target is not in the list.")
        return False
    mid_point = (low+high) // 2  # (100 // 2)  == 50
    if li[mid_point] == target:  # 50 != 46
        return mid_point
    elif target > li[mid_point]:  # 46 not > 50
        return binary_search(li, target, mid_point + 1, high)
    elif target < li[mid_point]:  # 46 < 50
        return binary_search(li, target, low, mid_point-1)#low=0,high = 50-1


if __name__ == '__main__':
    li = list(range(100))
    print(binary_search(li, 46))
