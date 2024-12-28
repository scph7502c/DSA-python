def bubble_sort(list):
    for i in range(len(list)):
        for j in range(0, len(list) - i - 1):
            if list[j] > list[j + 1]:
                tmp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = tmp
    print(list)
    return list


my_list = [3, 1, 2, 67, 34, 12, 11, 10, 7, 9]
bubble_sort(my_list)
