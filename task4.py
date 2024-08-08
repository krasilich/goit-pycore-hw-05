from typing import Optional


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(handler):
    def wrapper(*args, **kwargs):
        try:
            return handler(*args, **kwargs)
        except ValueError as e:
            return str(e)
        except Exception as e:
            return "Unexpected error occurred."

    return wrapper


@input_error
def add_contact(args, contacts):
    """
    Adds a contact to the contacts dictionary.
    :param args:
    :param contacts:
    :return:
    """

    if len(args) != 2:
        raise ValueError("Provide name and phone number.")

    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def get_contact(args, contacts):
    """
    Returns the phone number for the given contact.
    :param args:
    :param contacts:
    :return:
    """
    if len(args) != 1:
        raise ValueError("Provide name of the contact.")

    name = args[0]

    if name not in contacts:
        raise ValueError("Contact not found.")

    return contacts[name]


@input_error
def remove_contact(args, contacts):
    """
    Removes the contact from the contacts dictionary.
    :param args:
    :param contacts:
    :return:
    """

    if len(args) != 1:
        raise ValueError("Provide name of the contact.")

    name = args[0]

    if name not in contacts:
        raise ValueError("Contact not found.")

    del contacts[name]

    return "Contact removed."


@input_error
def update_contact(args, contacts):
    """
    Updates the phone number for the given contact.
    :param args:
    :param contacts:
    :return:
    """

    if len(args) != 2:
        raise ValueError("Provide name and phone number.")

    name, phone = args

    if name not in contacts:
        raise ValueError("Contact not found.")

    contacts[name] = phone

    return "Contact updated."


@input_error
def list_contacts(contacts) -> str:
    """
    Returns the list of contacts.
    :param contacts:
    :return: str
    """
    if len(contacts) == 0:
        return "No contacts found."

    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


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
        elif command == "phone":
            print(get_contact(args, contacts))
        elif command == "remove":
            print(remove_contact(args, contacts))
        elif command == "all":
            print(list_contacts(contacts))
        elif command == "update":
            print(update_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
