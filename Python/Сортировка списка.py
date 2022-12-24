list = input("Введите последовательность чисел через пробел: ")
list_s = [int(a) for a in list.split()]

num = int(input("Введите число которое нужно добавить: "))
if num % 1 == 0:
    list_s.append(num)
    print("Список до сортировки: ", list_s)

def sort(list_s):
    for i in range(len(list_s)): 
        idx_min = i  
        for j in range(i, len(list_s)):
            if list_s[j] < list_s[idx_min]:
                idx_min = j
        if i != idx_min:  
            list_s[i], list_s[idx_min] = list_s[idx_min], list_s[i]
    return list_s

print("Список после сортировки:", sort(list_s))