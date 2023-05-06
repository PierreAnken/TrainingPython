my_global = 'globale'


def my_function():
    print(my_global)

    my_locale = 'locale'

    global my_globale_2
    my_globale_2 = 'globale 2'

my_function()

# bug => print(my_locale)
print(my_globale_2)



