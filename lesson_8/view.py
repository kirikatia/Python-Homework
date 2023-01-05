def main_menu():
    print('Выберите команду меню:')
    print('1. Показать телефонную книгу')
    print('2. Загрузить телефонную книгу')
    print('3. Сохранить телефонную книгу')
    print('4. Добавить контакт')
    print('5. Изменить контакт')
    print('6. Удалить контакт')
    print('7. Найти контакт')
    print('0. Выйти из приложения\n')
    return input_menu()

def input_menu():
    while True:
        try:
            choice = int(input('Введите пункт меню: '))
            if choice in range (1, 8) or choice == 0: 
                return choice
            else:
                print('Такого пункта меню нет. Внимательнее, пожалуйста')
        except:
            print('Ошибка ввода. Введите корректный пункт меню')

def print_phone_book(phone_book):
    print()
    if len(phone_book) < 1:
        print('Телефонная книга пуста или не загружена\n')
        print()
    else:
        print_contacts(phone_book)

def input_new_contact():
    name = input('Введите имя контакта: ')
    phone = input('Введите телефон контакта: ')
    comment = input('Введите комментарий контакта: ')
    print()
    new_contact = [name, phone, comment]
    return new_contact

def input_remove_contact():
    id = int(input('Введите ID контакта, который стоит удалить: '))
    return id

def input_search():
    return input('Введите строку для поиска контакта: ')

def print_not_found():
    print('Не найдено контактов подходящий под заданный запрос')

def print_contacts(contacts):
    for id, contact in enumerate(contacts, 1):
        print(id, *contact)
    print()

def input_edit_contact_id():
    id = int(input('Введите ID контакта для редактирования: '))
    return id

def input_edit_contact_data(current_contact):
    print('Задайте новые данные контакта, пусто - оставить без редактирования')
    name = input(f'Введите новое имя ({current_contact[0]}): ')
    phone = input(f'Введите новый телефон ({current_contact[1]}): ')
    comment = input(f'Введите новый комментарий ({current_contact[2]}): ')
    print()
    new_contact = [name, phone, comment]
    return new_contact

def print_error_not_in_book(id):
    print(f'Введенный идентификатор {id} отсуствует в книге \n')

def print_book_loaded():
    print('Телефонная книга загружена\n')

def print_book_saved():
    print('Телефонная книга сохранена\n')
