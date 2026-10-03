def check_password_strength(password):
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_symbol = any(not char.isalnum() for char in password)

    if len(password) <= 4:
        print("Password strength: Very Weak")
    elif len(password) >= 8 and not has_upper:
        print("Password strength: Weak")
    elif len(password) >= 8 and has_upper and not has_lower:
        print("Password strength: Medium")
    elif len(password) >= 8 and has_upper and has_lower and not has_symbol:
        print("Password strength: Strong")
    elif len(password) >= 8 and has_upper and has_lower and has_symbol:
        print("Password strength: Very Strong")
    else:
        print("Password strength: Weak")


def main():
    password = input("Enter a password: ")
    check_password_strength(password)


if __name__ == '__main__':
    main()
