# example.py

def greet(name: str) -> str:
    """
    Function to greet a person.
    
    :param name: Name of the person being greeted
    :return: Greeting string
    """
    return f"Hello, {name}!"


if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet(name))