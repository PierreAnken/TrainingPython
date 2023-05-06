user_input = input('Enter a number ')

# Is the string only composed of integers?
if user_input.isdigit():
    x = int(user_input)

    if x > 150:
        print("x > 150")
    elif x < 150:
        print("x < 150")
    else:
        print("x == 150")
else:
    print('Invalid number', user_input)
