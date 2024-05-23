# name: str = input ('Enter your name: ')
# print(f'Witaj! {name}')


data_of_users: list = [
    {'name': 'Julia', 'surname': 'Szklazewska', 'posts': 5, 'location': 'Hajnówka'},
    {'name': 'Sebastian', 'surname': 'Dudek', 'posts': 15, 'location': 'Siedlce'},
    {'name': 'Marek', 'surname': 'Pietrzak', 'posts': 7, 'location': 'Rzeszów'},
    {'name': 'Marcin', 'surname': 'Szczepaniuk', 'posts': 35, 'location': 'Mińsk Mazowiecki'},
]

print(f'Witaj {data_of_users[0]['name']}')


def read(users: list) -> None:
    """
    this is a function to show users from an list
    :param users: a list of users
    :return: None
    """
    for user in users[1:]:
        print(f'Twój znajomy {user['name']},opublikował :{user['posts']}')


# read(data_of_users)

def add_users(users: list) -> None:
    """
    add user to a list
    :param users: user list
    :return: None
    """
    name: str = input('Enter your name: ')
    surname: str = input('Enter your surname:')
    posts: int = int(input('Enter your posts:'))
    location: str = input('Enter your location:')
    new_user: dict = {'name': name, 'surname': surname, 'posts': posts, 'location': location}
    users.append(new_user)


# add_users(data_of_users)
# read(data_of_users)
def delete_user(users: list) -> None:
    name: str = input('Enter a name of user to remove: ')
    for user in users:
        if user['name'] == name:
            users.remove(user)


# delete_user(data_of_users)
# read(data_of_users)
