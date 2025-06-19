def get_user_info(user_data: list) -> None:
    for user in user_data:
        print(f"Twój znajomy {user['name']}! z mieiscowosci {user['location']} opublikował {user['posts']} postów")


def add_user(user_data: list) -> None:
    new_name = input('podaj imie nowego uzytkownika: ')
    new_location = input('podaj Lokalizacje nowego użytkownika: ')
    new_posts = int(input('podai Liczbe postow nowego użytkownika: '))
    user_data.append({"name": new_name, "location": new_location, "posts": new_posts})
