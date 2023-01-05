import view

phone_book = []

def get_phone_book() -> list:
    global phone_book
    return phone_book

def set_phone_book (new_phone_book: list):
    global phone_book
    phone_book = new_phone_book

def add_contact():
    global phone_book
    contact = view.input_new_contact() 
    phone_book.append(contact)

def remove_contact():
    global phone_book
    view.print_phone_book(phone_book)
    
    id = view.input_remove_contact()
    if id > len(phone_book) or id < 0:
        view.print_error_not_in_book(id)
        return

    confirm = input(f'Вы точно хотите удалить контакт {phone_book[id-1][0]}? (y/n)')
    if confirm.lower() == 'y':
        del_contact = phone_book.pop(id-1)

def find_contact():
    global phone_book
    search = view.input_search()
    matches = list(filter(lambda x: search in x[0] or search in x[1] or search in x[2], phone_book))
    if len(matches) == 0:
        view.print_not_found()
        return
    
    view.print_contacts(matches)

def edit_contact():
    global phone_book
    view.print_phone_book(phone_book)

    id = view.input_edit_contact_id()
    if id > len(phone_book) or id < 0:
        view.print_error_not_in_book(id)
        return

    contact = view.input_edit_contact_data(phone_book[id-1])
    for idx, x in enumerate(contact):
        if x and len(x) > 0:
            phone_book[id-1][idx] = x