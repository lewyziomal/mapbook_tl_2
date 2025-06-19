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


def update_user(users_data: list) -> None:
    użykownik_do_edycji = input('podaj uzytkownika do edycji: ')
    for user in users_data:
        if user['name'] == użykownik_do_edycji:
            user['name'] = input('podaj nowe imie użytkownika: ')
            user['location'] = input('podaj nowa lokalizacie: ')
            user['posts'] = int(input('podaj nowa liczbe postów uzytkownika: '))


def get_coordinates(city: str) -> list:
    import requests
    from bs4 import BeautifulSoup
    url = f'https://pl.wikipedia.org/wiki/{city}'
    response = requests.get(url).text
    response_html = BeautifulSoup(response, "html.parser")
    longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
    latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
    return [latitude, longitude]


def get_map(users_data: list) -> None:
    import folium
    map = folium.Map(location=(52.23, 21.00), zoom_start=6)
    for user in users_data:
        coordinates = get_coordinates(user['location'])

        folium.Marker(
            location=(coordinates[0], coordinates[1]),
            popup=f"Twój znajomy: {user['name']}, <br/> z miejscowości: {user['location']} opublikował: {user['posts']} postów").add_to(
            map)
    map.save('mapa.html')
