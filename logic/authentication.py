def check_login(username, password):
    list_username = ['1']
    list_password = ['1']

    if username in list_username and password == list_password[list_username.index(username)]:
        return True
    else:
        return False
