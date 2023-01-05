import phone_book as pb

path = 'phone_book.txt'

def load_contacts() -> list:
    global path
    with open(path, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    pb.set_phone_book(str_to_list(data))

def save_contacts():
    global path
    ready_book = list_to_str(pb.get_phone_book())
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(ready_book)

def list_to_str(phone_book: list) -> str:
    str_phone_book = ""
    for contact in phone_book:
        new_contact = ';'.join(contact)
        str_phone_book += new_contact + '\n'
    return str_phone_book[:-1]

def str_to_list(phone_book: list) -> list:
    new_list = []
    for contact in phone_book:
        new_contact = contact.strip().split(';')
        new_list.append(new_contact)
    return new_list