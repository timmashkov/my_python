#Преобразовать набора списков users = ['user1','user2','user3','user4','user5'] ids = [4, 5, 9, 14, 7] salary = [111,222,333] в другой набор

from numpy import array
from pandas.core.common import flatten

l = [[1, 2, 3], [4, 5, 6]]

print(list(array(l).flat))
print(list(flatten(l)))
