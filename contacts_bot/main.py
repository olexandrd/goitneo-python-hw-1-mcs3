def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        res = "Contact added."
    except (KeyError, ValueError, IndexError):
        res = "Please add new contact in format: add name phone"
    return res


def change_contact(args, contacts):
    try:
        name, phone = args
    except ValueError:
        res = "Please change contact using format: change name phone"
    if name in contacts.keys():
        contacts[name] = phone
        res = "Contact changed."
    else:
        res = "Contact not found. Please add contact first."
    return res


def show_phone(args, contacts):
    name = args[0]
    try:
        res = contacts[name]
    except (KeyError, IndexError):
        res = "Contact not found. Please add contact first."
    return res


def show_all(contacts):
    res = str()
    for k, v in contacts.items():
        res = res + f"{k}: {v},\n"
    res = res.rstrip(",\n")
    return res


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
