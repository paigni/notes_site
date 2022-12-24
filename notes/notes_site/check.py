def check_reg_password(data:dict):
    password1 = data.get('password1')
    password2 = data.get('password2')
    if password1 == password2:
        return True
    return False

def check_register_data(data: dict):
    if not isinstance(data, dict):
        return False

    values = data.keys()
    true_list = [
        "username",
        "email",
        "password1",
        "password2",
    ]
    for value in true_list:
        if value not in values:
            return False
        return True