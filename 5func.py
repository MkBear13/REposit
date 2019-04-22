def sorting(list_of_data):
    for i in range(len(list_of_data) - 1):
        for j in range(len(list_of_data) - i - 1):
            if list_of_data[j] > list_of_data[j + 1]:
                buff = list_of_data[j]
                list_of_data[j] = list_of_data[j + 1]
                list_of_data[j + 1] = buff
    return list_of_data


list1 = [1, 2, 3, 5, 9, 4, 17, 6, 13]
print(sorting(list1))