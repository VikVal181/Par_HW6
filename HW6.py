def bin_search(nums, low, high, n):

    if low > high:
        return -1

    mid = (low + high)//2

    if n == nums[mid]:
        return mid
    elif n < nums[mid]:
        return bin_search(nums, low, mid-1, n)
    else:
        return bin_search(nums, mid+1, high, n)

list = [2, 5, 6, 11, 14, 15, 19, 23, 51]
target = 6

index = bin_search(list, 0, len(list)-1, target)

if index == -1:
    print("Заданного числа нет в списке")
else:
    print("Искомое число находиться в списке на " + str(index) + " месте")