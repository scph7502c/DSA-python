def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            print(mid)
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    print("Not found")
    return None


my_list = [5, 1, 2, 3, 56, 22, 99, 34, 66, 21, 14]
my_list = sorted(my_list)
binary_search(my_list, 166)
