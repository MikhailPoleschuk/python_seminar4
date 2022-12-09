# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
n = int(input('->'))
list_ = []
for i in range(1, n+1):
    list_.append(i)
new_list = []
new_list.append(1)
for i in range(2,len(list_)):
    ne_prostoe_= 0
    for j in range(1,i):
        if list_[i] % list_[j] == 0:
            ne_prostoe_= 1
    if ne_prostoe_==0:
        new_list.append(list_[i])        

print(new_list)
