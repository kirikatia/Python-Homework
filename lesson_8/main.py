import data_base
import view
import phone_book as pb

def choice_menu(choice):
    match choice:
        case 1:
            view.print_phone_book(pb.get_phone_book())
        case 2:
            data_base.load_contacts()
            view.print_book_loaded()
        case 3:
            data_base.save_contacts()
            view.print_book_saved()
        case 4:
            pb.add_contact()
        case 5:
            pb.edit_contact()
        case 6:
            pb.remove_contact()
        case 7:
            pb.find_contact()
            pass
        case 0:
            return True


while True:
    choice = view.main_menu()
    if choice_menu(choice):
        break