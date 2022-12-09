# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл,
# содержащий сумму многочленов (складываются числа, у которых "х" в одинаковых степенях).

# Ограничения текущей версии которые надо допиливать:
# 1. Запись многочлена всегда с 3-мя коэфициентами
# 2. не доработано с хоэфициентом +1
# 3. в результат отработать пробелы между -+ и цифрой от коэффициента


file_path = 'file1.txt'
with open(file_path, 'w') as f_data1:
    f_data1.writelines('4x*2 - 3*x - 25 = 0')

file_path = 'file2.txt'
with open(file_path, 'w') as f_data2:
    f_data2.writelines('2x*2 + 2*x + 10 = 0')


file_path = 'file1.txt'
with open(file_path, 'r') as f_data1_:
    str1_ = f_data1_.readline()

file_path = 'file2.txt'
with open(file_path, 'r') as f_data2_:
    str2_ = f_data2_.readline()


def find_c(str_):  # ищем в строке коэффициент С
    str_ = str_.split('=')
    str_ = str_[0][:-1]
    str_ = str_.replace(' ', '')

    for i in range(len(str_)-1, 0, -1):

        if str_[i] == "x" and i != len(str_)-1:

            for j in range(len(str_)-1, i, -1):
                if str_[j] == "+" or str_[j] == "-":
                    c_ = str_[j:len(str_)]
                    c_num = int(c_)
                    return c_num
                    break

    return 0


def find_b(str_):  # ищем в строке коэффициент B
    str_ = str_.split('=')
    str_ = str_[0][:-1]
    str_ = str_.replace(' ', '')

    for i in range(len(str_)-1, 0, -1):

        if str_[i] == "x" and i != len(str_)-1:

            for j in range(i, 0, -1):
                if str_[j] == "-":
                    b_ = str_[j:i-1]
                    return b_
                    break
                elif str_[j] == "+":

                    b_ = str_[j+1:i-1]
                    return b_
                    break

    return 0


def find_a(str_):  # ищем в строке коэффициент A
    str_ = str_.split('=')
    str_ = str_[0][:-1]
    str_ = str_.replace(' ', '')

    count = 0
    for i in range(len(str_)-1, 0, -1):

        if str_[i] == "x" and i != len(str_)-1:

            count += 1
            if count == 2:

                a_ = str_[0:i]
                if a_ == '-':
                    return -1
                    break

                else:
                    return a_
                    break

    return 0


def find_abc(str1_):
    c_str = find_c(str1_)
    if c_str != 0:
        c_num = int(c_str)

    b_str = find_b(str1_)
    if b_str != 0:
        b_num = int(b_str)

    a_str = find_a(str1_)
    if a_str != 0:
        a_num = int(a_str)

    return a_num, b_num, c_num


a1, b1, c1 = find_abc(str1_)
# print(f'a1= {a1},b1={b1},c1={c1}')
a2, b2, c2 = find_abc(str2_)
# print(f'a2= {a2},b2={b2},c2={c2}')

result_ = ''

if a1+a2 > 0 or a1+a2 < 0:
    result_ = str(a1+a2) + 'x**2 '
else:
    result_ = ''

if b1+b2 > 0:
    result_ = result_ + ' + ' + str(b1+b2) + 'x '
elif b1+b2 < 0:
    result_ = result_  + str(b1+b2)+ 'x '

if c1+c2 > 0:
    result_ = result_ + ' + ' + str(c1+c2)
elif c1+c2 < 0:
    result_ = result_  + str(c1+c2)

result_=result_ + ' = 0'

print(result_)

file_path = 'file_result.txt'
with open(file_path, 'w') as f_:
    f_.writelines(result_)



# print(f'{a1+a2}x*2 {b2+b1}x {c2+c1} = 0')
