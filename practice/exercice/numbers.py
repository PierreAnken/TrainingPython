def get_number_from_position(list_of_number, asked_position):
    # check if the asked position is inside the list
    if len(list_of_number) >= asked_position:
        value_at_position = list_of_number[asked_position - 1]
        print(f"The number {value_at_position} is at the position {asked_position}")
    else:
        print("invalid position")


if __name__ == '__main__':

    number_list = [23, 45, 234, 67, 98, 45, 234, 79, 23]

    # ask the user for a position
    try:
        user_input = int(input("whats the position of the object? "))

        # pass the position to a new function (to create) called get_number_from_position
        get_number_from_position(number_list, user_input)
    except:
        print(f'Invalid number')
