def get_user_info(user_data:list)->None:
    for user in user_data:
        print(f"Twój znajomy {user['name']}! z mieiscowosci {user['location']} opublikował {user[ 'posts']} postów")
