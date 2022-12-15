
#Дан список, вывести отдельно буквы и цифры.

import methods as m

length = m.enter_num('Введите размер массива: ')
print('Сгенерированный массив: ')
lst = m.create_list(length)
print(lst)

print('Отсортированный массив: ')
print(m.separate_by_elements(lst))
