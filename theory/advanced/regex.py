import re

if __name__ == '__main__':
    # base
    print('\n### base ###')
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    match_object = phoneNumRegex.search('My number is 415-555-4242.')
    print('Phone number found: ' + match_object.group())

    # Groups
    # They can be used to separate results
    print('\n### Groups ###')
    phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
    match_object = phoneNumRegex.search('My number is 415-555-4242.')
    print(f'match_object.groups(): {match_object.groups()}')
    print(f'match_object.group(): {match_object.group()}')

    # regular expression special chars: . ^ $ * + ? { } [ ] \ | ( )
    # escape them with \

    # Pipe |
    # or operator, first result is returned
    print('\n### pipe | (or) ###')
    heroRegex = re.compile(r'Batman|Tina Fey')

    mo1 = heroRegex.search('Batman and Tina Fey')
    print(f'match_object.groups(): {mo1.group()}')

    # ?, +, . and * wildcard
    # Make a group optional / + one or more / * any amount / . replace anything except a new line
    print('\n### ?,+ and * wildcard ###')
    batRegex = re.compile(r'Bat(wo)?man')

    mo1 = batRegex.search('The Adventures of Batman')
    print(mo1.group())

    mo2 = batRegex.search('The Adventures of Batwoman')
    print(mo2.group())

    batRegex2 = re.compile(r'Bat(wo)*man')
    mo3 = batRegex2.search('The Adventures of Batwowowowoman')
    print(mo3.group())

    batRegex3 = re.compile(r'Bat(wo)+man')
    mo3 = batRegex3.search('The Adventures of Batman')
    print(mo3)

    # regex are greedy, the match by default the longest result
    # add an '?' after a range {} to get the shortest result
    print('\n### greedy ###')

    greedyHaRegex = re.compile(r'(Ha){3,5}')
    mo1 = greedyHaRegex.search('HaHaHaHaHa')
    print(mo1.group())

    nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
    mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
    print(mo2.group())

    # findall()
    # if no group return a list of strings
    print('\n### findall() ###')

    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')  # has no groups
    match_list = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
    print(match_list)

    phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')  # has groups
    match_list = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
    print(match_list)

    # Shorthand character class
    print('\n### Shorthand character class ###')
    # \d Any numeric digit from 0 to 9.
    # \D Any character that is not a numeric digit from 0 to 9.
    # \w Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)
    # \W Any character that is not a letter, numeric digit, or the underscore character.
    # \s Any space, tab, or newline character. (Think of this as matching “space” characters.)
    # \S Any character that is not a space, tab, or newline

    xmasRegex = re.compile(r'(\d+)(\s\w+)')
    match_list = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
    print(match_list)

    # Own Character classes
    print('\n### Own Character classes ###')
    vowelRegex = re.compile(r'[aeiouAEIOU]')
    match_list = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
    print(match_list)

    # ^ mark a class as negative and will match anything not inside it
    consonantRegex = re.compile(r'[^aeiouAEIOU]')
    match_list = consonantRegex.findall('RoboCop eats baby food. BABY FOOD.')
    print(match_list)

    # ^ and $ (start and end)
    print('\n### ^ and $ (start and end) ###')
    beginsWithHello = re.compile(r'^Hello')
    match_object = beginsWithHello.search('Hello, world!')
    print(match_object.group())

    match_object = beginsWithHello.search('He said hello.')
    print(match_object)

    # re.DOTALL
    # dot matches now newlines
    print('\n### re.DOTALL ###')

    noNewlineRegex = re.compile('.*')
    match_object = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
    print(match_object)

    newlineRegex = re.compile('.*', re.DOTALL)
    match_object = newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
    print(match_object)

    # Summary of notation
    # The ? matches zero or one of the preceding group.
    # The * matches zero or more of the preceding group.
    # The + matches one or more of the preceding group.
    # The {n} matches exactly n of the preceding group.
    # The {n,} matches n or more of the preceding group.
    # The {,m} matches 0 to m of the preceding group.
    # The {n,m} matches at least n and at most m of the preceding group.
    # {n,m}? or *? or +? performs a non-greedy match of the preceding group.
    # ^spam means the string must begin with spam.
    # spam$ means the string must end with spam.
    # The . matches any character, except newline characters.
    # \d, \w, and \s match a digit, word, or space character, respectively.
    # \D, \W, and \S match anything except a digit, word, or space character, respectively.
    # [abc] matches any character between the brackets (such as a, b, or c).
    # [^abc] matches any character that isn’threads between the brackets.

    # Case-Insensitive Matchings
    print('\n### Case-Insensitive Matching ###')
    robocop = re.compile(r'robocop', re.I)
    match_object = robocop.search('RoboCop is part man, part machine, all cop.').group()
    print(match_object)

    # verbose mode
    phoneRegex = re.compile(r'''
     (\d{3}|\(\d{3}\))?             # area code
     (\s|-|\.)?                     # separator
     \d{3}                          # first 3 digits
     (\s|-|\.)                      # separator
     \d{4}                          # last 4 digits
     (\s*(ext|x|ext.)\s*\d{2,5})?   # extension
     ''', re.VERBOSE)

