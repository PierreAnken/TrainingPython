import random
from string import ascii_lowercase as alphabet

# lambda functions are inline short functions
# applied to a set of element

word_list = ['table', ' zen   ', 'castle', 'edge']


def len_without_space(value: str):
    return len(value.strip())


print('Sort by length without space', sorted(word_list, key=len_without_space))

print('Sort by length without space, with lambda', sorted(word_list, key=lambda word: len(word.strip())))

print('Sort by last letter without space, with lambda', sorted(word_list, key=lambda word: word.strip()[-1]))

print(
    'Sort by index sum, without space, with lambda',
    sorted(
        word_list, key=lambda word: sum([alphabet.index(letter) for letter in word.strip()])
    )
)

print('Sort randomly', sorted(word_list, key=lambda _: random.randint(0, len(word_list))))
