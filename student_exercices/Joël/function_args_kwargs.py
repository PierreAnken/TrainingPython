def echo(*args, **kwargs):

    args = list(args)
    print(type(args), args)
    print(type(kwargs), kwargs)


echo(3, 4, a=1, b=2)
