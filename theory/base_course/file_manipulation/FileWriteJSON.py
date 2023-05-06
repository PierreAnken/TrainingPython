import json

if __name__ == '__main__':

    # Write numbers between 1 and 100 in a file
    with open(file='numbers_1_100.json', mode='w') as file_pointer:
        number_list = list(range(1, 101))  # [1, 2, 3, ... , 100]
        number_list_json = json.dumps(number_list)
        file_pointer.write(number_list_json)
        