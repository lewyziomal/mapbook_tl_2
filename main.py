users: list = [
    {"name": "Bernard","location":"Etk","posts":400},
    {"name": "Krzysztof","location":"Białobrzegi","posts":500},
    {"name": "Maja","location":"Świecie", "posts":300},
    {"name": "Zuzanna","location":"Radzyń_Podlaski","posts":700},
]

def get_user_info(user_data:list)->None:

    for user in user_data:
        print(f"Twój znajomy {user['name']}! z mieiscowosci {user['location']} opublikował {user[ 'posts']} postów")

get_user_info(users)