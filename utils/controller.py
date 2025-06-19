def get_user_info(user_data: list) -> None:
    for user in user_data:
        print(f"Twój znajomy {user['name']} z mieiscowosci {user['location']} opublikował {user['posts']} postów")


def add_user(user_data: list) -> None:
    new_name = input('podaj imie nowego uzytkownika: ')
    new_location = input('podaj Lokalizacje nowego użytkownika: ')
    new_posts = int(input('podai Liczbe postow nowego użytkownika: '))
    user_data.append({"name": new_name, "location": new_location, "posts": new_posts})


def remove_user(users_data: list) -> None:
    uzytkownik_do_usuniecia = input('podaj uzytkownika do usuniecia: ')

    for user in users_data:
        if user["name"] == uzytkownik_do_usuniecia:
            users_data.remove(user)

def update_user( users_data: list) -> None:

    użykownik_do_edycji = input('podaj uzytkownika do edycji: ')
    for user in users_data:
        if user['name'] == użykownik_do_edycji:
            user ['name']=input('podaj nowe imie użytkownika: ')
            user ['location']=input('podaj nowa lokalizacie: ')
            user ['posts'] = int(input('podaj nowa liczbe postów uzytkownika: '))