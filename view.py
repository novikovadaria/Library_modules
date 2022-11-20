def get_value():
    print("Hello! Welcome to library.")
    start_act = input(
        "To add new data input 1\n")

    if start_act == '1':
        while True:
            title = input('What is the title of the book? ')
            number_of_pages = int(input('How many pages does it have? '))
            first_name = input('What is the first name of the author? ')
            last_name = input('What is the last name of the author? ')
            print("Thank you!")
    else:
        print("See you soon!")

    return title, number_of_pages, first_name, last_name


def output():
    print('All done.')
