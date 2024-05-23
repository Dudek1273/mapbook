# name: str = input ('Enter your name: ')
# print(f'Witaj! {name}')

data_of_users: list = [
    {'name': 'Julia', 'surname': 'Szklazewska', 'posts': 5, 'location': 'Hajnówka'},
    {'name': 'Sebastian', 'surname': 'Dudek', 'posts': 15, 'location': 'Siedlce'},
    {'name': 'Marek', 'surname': 'Pietrzak', 'posts': 7, 'location': 'Rzeszów'},
    {'name': 'Marcin', 'surname': 'Szczepaniuk', 'posts': 35, 'location': 'Legnica'},
]

print(f'Witaj {data_of_users[0]['name']}')
def read(users:list)->None:
    """
    this is a function to show users from an list
    :param users: a list of users
    :return: None
    """
    for user in users[1:]:
        print(f'Twój znajomy {user['name']},opublikował :{user['posts']}')

read(data_of_users)