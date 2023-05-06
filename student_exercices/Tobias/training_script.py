# function
# Input: 2 structure (tuple, list, set)
# Output: dictionary: every different values as key, and as value a counter (how many time in all structures)

# initialize the function
def count_unique_values(structure1, structure2):
    data = list(structure1) + list(structure2)

    # create empty dictionnary
    dict_count = {}
    # iterate over all elements from all structure
    for value in data:
        print(dict_count)
        # if element in dictionary, increase the counter of its value from one
        if value in dict_count.keys():
            dict_count[value] += 1

        # else add the key to the dict with a counter from 1
        else:
            dict_count[value] = 1

    return dict_count


if __name__ == '__main__':

    l1, t1 = ['a', 1, 2, 3], (3, 2, 0, 'b')
    result_dict = count_unique_values(l1, t1)

    print(result_dict[2] == 2)
    print(result_dict.get('c') is None)
