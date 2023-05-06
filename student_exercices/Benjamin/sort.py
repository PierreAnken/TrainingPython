word_list = ['222', '63', '1000', '132']

print(
    'Sort by length without space, with lambda',
    sorted(
        word_list, key=lambda word: sum([int(b) for b in word])
    )
)
