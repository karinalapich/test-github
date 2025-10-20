import string


def check_password(password):
    errors = []

    if len(password) != 8:
        errors.append("Длина пароля не равна 8")

    if password == password.lower():
        errors.append("В пароле отсутствуют заглавные буквы")

    if password == password.upper():
        errors.append("В пароле отсутствуют строчные буквы")

    if not any(symbol.isdigit() for symbol in password):
        errors.append("В пароле отсутствуют цифры")

    special_chars = '*-#'
    if not any(symbol in special_chars for symbol in password):
        errors.append("В пароле отсутствуют специальные символы")

    allowed_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + '*-#'
    if not all(symbol in allowed_chars for symbol in password):
        errors.append("В пароле используются непредусмотренные символы")

    if not errors:
        print("Надежный пароль")
    else:
        for error in errors:
            print(error)


password = input().strip()
check_password(password)