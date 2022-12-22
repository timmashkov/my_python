# модуль импорта данных 
# исправил ошибку при вызове функции
def import_data(data, sep=None):
    with open('phone.csv', 'a+') as file:
        if sep == None:
            for i in data:
                file.write(f"{i}\n")
            file.write(f"\n")
        else:
            file.write(sep.join(data))
            file.write(f"\n")
