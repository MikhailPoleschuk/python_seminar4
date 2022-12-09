# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
# - k=4 => 8*(x**4) + 9*(x**3) + 1*(x**2) + 5*x + 4 = 0 или 8*(x**4) + 5*x + 4 = 0 и т.д.
import random
k_ = int(input('->'))
kf_ = random.randrange(0, 100)
count = k_-1
if kf_ == 0:
    resoult_ = ''
else:
    resoult_ = str(f'{kf_}*x**{k_}')

while count >= 0:
    kf_ = random.randrange(0, 100)
    if kf_ != 0:
        if resoult_ != '':
            str_ = str(f'{kf_}*x**{count}')
            resoult_ = resoult_ + ' + ' + str_
        else:
            str_ = str(f'{kf_}*x**{count}')
            resoult_ = resoult_ + str_
        # '+'.join([resoult_,str_])

    count -= 1
resoult_ = resoult_+" = 0"
print(resoult_)
