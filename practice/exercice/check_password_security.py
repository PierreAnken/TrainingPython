if __name__ == '__main__':

    # create an empty list of insecure reasons
    insecure_reasons = []

    # ask the user for a password
    user_password = input("Please choose a password? ")

    # We will check the security of the password in many steps

    # 1) check if the length of it is at least 10
    if len(user_password) < 10:
        insecure_reasons.append(f'Length of {len(user_password)} under 10')

    # 2) check if it contains at least a number Hint: isdigit() // any([True, False]) =>
    if not any(letter.isdigit() for letter in user_password):
        insecure_reasons.append('the password must contain at least one number')

    # 3) check if it contains at least a letter Hint: isalpha()
    if not any(letter.isalpha() for letter in user_password):
        insecure_reasons.append('the password must contain at least one letter')

    # 4) check if contains a special character like "$@#.-"
    if not any(letter in '$@#.-' for letter in user_password):
        insecure_reasons.append('the password must contain at least one special character: $@#.-')

    # if every condition is correct, print "Your password <password> is secured
    if not insecure_reasons:
        print(f"Your password {user_password} is secured")
    # else print "You password <password> is insecure, <reasons>
    else:
        print(f"You password {user_password} is insecure:\n {' - '.join(insecure_reasons)}")
