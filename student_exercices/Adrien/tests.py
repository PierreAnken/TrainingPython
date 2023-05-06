from string import ascii_lowercase as alphabet

if __name__ == '__main__':

    print(alphabet[-1:-len(alphabet)-1:-1])
    print(alphabet[0:len(alphabet):1])
    alphabet_inv = alphabet[::-1]
    print(alphabet_inv)
