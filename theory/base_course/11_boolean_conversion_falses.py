false_values = [0, ' ', False, None, [], {}, tuple(), set(), 0.0]

for false_value in false_values:
    print(f'>{false_value}<', 'of type', type(false_value).__name__, ' =>', bool(false_value))

my_list = []  # False
if my_list: # if my_list != False and my_list != None and len(my_list) > 0
    print('\nThe list is not empty')
else:
    print('\nThe list is empty')
