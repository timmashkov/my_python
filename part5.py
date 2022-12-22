
def print_data(data):
    if len(data) > 0:
        print("Фамилия".center(20), "Имя".center(20), "Отчество".center(20), "Дата рождения".center(20), "Группа".center(15), "Поток".center(30))
        print("-"*130)
        for item in data:
            print(item[0].center(20), item[1].center(20), item[2].center(20), item[3].center(20), item[4].center(15), item[5].center(30))
    else:
        print("Справочник пуст!")
        

# модуль поиска группы

from export_data import export_data
from print_data import print_data

def search_data(word, data):
    if len(data) > 0:
        for item in data:
            if word in item:
                return item
    else:
        return None
