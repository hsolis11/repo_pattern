import database
from database import User


def main_menu():
    print("Main menu:")
    print("\t1.) Add user")
    print("\t2.) Find user")
    print("\t3.) List users")
    print("\t4.) Edit user")
    print("\t5.) Delete user")
    print("\t6.) Quit")
    response = input("Input: ")
    return response

def find_user():
    user_id, username = None, None
    print("Find user:")
    print("\t1.) By ID:")
    print("\t2.) By Username:")
    decision = input(": ")
    if decision == '1':
        user_id = input("Type User ID: ")
    elif decision == '2':
        username = input("Type Username: ")
    return {'user_id': user_id,
            'username': username}


def add_user(user_object):
    print("Adding user:")
    f_name = input("First name: ")
    l_name = input("Last name: ")
    username = input("Username: ")
    password = input("Password ")
    return user_object(None, f_name, l_name, username, password)


def edit_user(user: User):
    print("Edit user:")
    print("Leave empty to not change value")
    f_name = input(f"Current '{user.f_name}', new: ")
    l_name = input(f"Current '{user.l_name}', new: ")
    password = input(f"New: ")
    if f_name:
        user.f_name = f_name
    if l_name:
        user.l_name = l_name
    if password:
        user.password = password
    return user


def main():
    run = True

    while run:
        user_input = main_menu()
        if user_input >= '6':
            run = False
        else:
            if user_input == '1':
                with database.Users() as db:
                    db.add_user(add_user(User))
                    db.complete()
            elif user_input == '2':  # Find user
                decision = find_user()
                with database.Users() as db:
                    user = None
                    if decision['user_id']:
                        user = db.get_user(user_id=decision['user_id'])
                    elif decision['username']:
                        user = db.get_user(username=decision['username'])
                    if user:
                        print("User found")
                        print(user)
                    else:
                        print("User not found\n")

            elif user_input == '3':
                with database.Users() as db:
                    users = db.get_list()
                    for user in users:
                        print(user)
            elif user_input == '4':
                print("Edit user")

            elif user_input == '5':
                print("Delete User")
                # Delete user by id, first and last name, username


if __name__ == "__main__":
    main()
