import requests

def create_user(name, password, email, phone):
    headers = {
        'name': name,
        'password': password,
        'email': email,
        'phone': phone
    }
    response = requests.post('http://127.0.0.1:8000/users/', headers)
    print(f"New user { name } with email { email } has been created,\n\n")

def get_all_users():
    response = requests.get('http://127.0.0.1:8000/users/')
    return response.json()

create_user('Akash_3', '123', '3@gmail.com', '12345')

users = get_all_users()
for user in users:
    print(f" User {user['id']}:")
    print(f" Name: {user['name']}")
    print(f" Email: {user['email']}")
    print(f" Phone: {user['phone']}")
    print(f" Password: {user['password']}")
