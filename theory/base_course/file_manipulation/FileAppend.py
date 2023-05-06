from string import ascii_lowercase as alphabet

for letter in alphabet:
    with open('alphabet.txt', 'a') as file_pointer:
        file_pointer.write(letter)
