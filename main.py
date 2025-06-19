from utils.model import users
from utils.controller import get_user_info, add_user, remove_user, update_user


def main():
    print('===========MENU============')
    print('0 - zakończ program ')
    print('1 - wyswietl co u znajomych ')
    print('2 - dodaj noego uzytkownika')
    print('3 - usun uzytkownika  ')
    print('4 - edytuj uzytkownika ')
    print('===========MENU============')

    while True:
        choice: str = input("Wybierz opcje MENU: ")
        if choice == '0':
            break
        if choice == '1':
            get_user_info(users)
        if choice == '2':
            add_user(users)
        if choice == '3':
            remove_user(users)
        if choice == '4':
            update_user(users)
    get_user_info(users)


if __name__ == "__main__":
    main()
