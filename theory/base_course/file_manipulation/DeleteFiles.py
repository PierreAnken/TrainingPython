import os


file_list = os.listdir()
print(file_list)

for file_name in file_list:
    if not file_name.endswith('.py'):
        os.remove(file_name)
        print(f'{file_name} removed')
