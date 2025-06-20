class User:
    def __init__(self, name: str, surname: str, location: str, posts: str):
        self.name=name
        self.surname=surname
        self.location=location
        self.posts=posts
        self.get_coordinates=self.get_coordinates()


    def get_coordinates(self) -> list:
        import requests
        from bs4 import BeautifulSoup

        url = f'https://pl.wikipedia.org/wiki/{self.location}'
        response = requests.get(url).text
        response_html = BeautifulSoup(response, "html.parser")
        longitude = float(response_html.select('.longitude')[1].text.replace(',', '.'))
        latitude = float(response_html.select('.latitude')[1].text.replace(',', '.'))
        return [latitude, longitude]

    def get_map(users_data:list) -> None:
        map = folium.Map(location=(52.23, 21.00), zoom_start=6)
        for user in users_data:
            coordinates = get_coordinates(user['location'])

            folium.Marker(
                location=(coordinates[0], coordinates[1]),
                popup=f"Twój znajomy: {user['name']}, <br/> z miejscowości: {user['location']} opublikował: {user['posts']} postów").add_to(
                map)
        map.save('mapa.html')
    get_map(users)