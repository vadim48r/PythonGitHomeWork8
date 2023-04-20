# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и 
# Вы должны реализовать функционал для изменения и удаления данных.

def read_data():
    """Читает содержимое файла и возвращает его список строк"""
    with open('data.txt', 'r', encoding='utf-8') as file:
        data = file.read().split("\n")
    return data

def show_data():
    """Эта функция выводит данные телефонного справочника"""
    data = read_data()
    for item in data:
        print(item)

def add_data():
    """Эта функция добавляет новый контакт в телефонный справочник"""
    with open('data.txt', 'a', encoding='utf-8') as file:
        surname = input('Введите фамилию: ')
        name = input('Введите имя: ')
        patronymic = input('Введите отчество: ')
        phone_number = input('Введите номер телефона: ')
        new_contact = f'{surname} {name} {patronymic} {phone_number}\n'
        file.write(new_contact)

def search_data():
    """Эта функция ищет контакты в телефонном справочнике по заданным параметрам"""
    search_param = input('Введите параметр для поиска: ')
    data = read_data()
    found_data = []
    for item in data:
        if search_param in item:
            found_data.append(item)
    if found_data:
        print('Найденные контакты:')
        for item in found_data:
            print(item)
    else:
        print('Контакты не найдены')

def delete_data():
    """Эта функция удаляет контакты из телефонного справочника"""
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    data = read_data()
    new_data = []
    for item in data:
        if surname in item and name in item:
            continue
        new_data.append(item)
    with open('data.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(new_data))

def update_data():
    """Эта функция изменяет контакты в телефонном справочнике"""
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    data = read_data()
    new_data = []
    for item in data:
        if surname in item and name in item:
            new_surname = input('Введите новую фамилию: ')
            new_name = input('Введите новое имя: ')
            new_patronymic = input('Введите новое отчество: ')
            new_phone_number = input('Введите новый номер телефона: ')
            new_item = f'{new_surname} {new_name} {new_patronymic} {new_phone_number}\n'
            new_data.append(new_item)
        else:
            new_data.append(item)
    with open('data.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(new_data))

while True:
    mode = input('Выберите режим работы справочника' + '\n'
                 + '0 - поиск, 1 - просмотреть справочник, 2 - добавить контакт, '
                 + '3 - удалить контакт, 4 - изменить контакт, 5 - выход: ')
    if mode == '1':
        search_data()
    elif mode == '2':
        add_data()
    elif mode == '3':
        delete_data()
    elif mode == '4':
        update_data()
    elif mode == '5':
        break
    elif mode == '0':
        search_data()
    else:
        print('Неверный режим')
