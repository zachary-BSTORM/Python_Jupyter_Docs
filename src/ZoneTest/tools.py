def get_number():
    """
    loop until a number is entered
    :return: number
    """
    while True:
        try:
            number = int(input("Enter a number: "))
            return number
        except ValueError:
            print("Invalid input. Please enter a number.")
            
def get_string():
    """
    loop until a string is entered
    :return: string
    """
    while True:
        string = input("Enter a string: ")
        if string:
            return string
        else:
            print("Invalid input. Please enter a non-empty string.")
            