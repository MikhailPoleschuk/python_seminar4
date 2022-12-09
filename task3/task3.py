# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Ввод: [1, 1, 2, 3, 4, 4, 4]
# Вывод: [2, 3]

list_ = [1, 1, 2, 3, 4, 4, 4]
print(list_)
new_list = []

for i in range(len(list_)):
    
    one_element = 1
    for j in range(len(list_)):
       
        if list_[i] == list_[j] and j != i:
            one_element = 0
    if one_element == 1:
        new_list.append(list_[i])

print(new_list)
