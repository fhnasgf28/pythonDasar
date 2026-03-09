def greet_user(name):
    print(f"Hello, {name}!")


def welcome_user(name):
    greet_user(name)
    print(f"Welcome to our community, {name}!")


def get_user_name():
    name = input("Please enter your name:")
    return name


def validate_name(name):
    while not name.strip():
        print("Name cannot be empty. Please enter a valid name")
        name = input("Please enter yout name:")
    return name


def say_goodby(name):
    print(f"Goodbye, {name}! Have a great day")


def main():
    # meminta input pengguna
    name = get_user_name()
    name = validate_name(name)
    welcome_user(name)
    say_goodby(name)


if __name__ == "__main__":
    main()
