import json

if __name__ == '__main__':

    with open(file='numbers_1_100.json', mode='r') as file_pointer:
        file_content = file_pointer.read()
        print(type(file_content))

        number_list = json.loads(file_content)
        print(type(number_list))
        print(number_list)
