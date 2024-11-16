def groups_of_3(numbers:list[int]) -> list[list[int]]:
    count = 0
    new_list = []
    small_list = []
    for num in numbers:
        small_list.append(num)
        count += 1
        if count == 3:
            new_list.append(small_list)
            small_list = []
            count = 0
    if small_list != []:
        new_list.append(small_list)
    return new_list



