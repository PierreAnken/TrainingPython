# https://www.python-forum.de/viewtopic.php?t=36346
# A

def outerdec(func):
    def innerdec():
        return func + 1

    return innerdec()


def normalfunc():
    return 3


newfunc = outerdec(normalfunc())
print(newfunc)

# B

def outerdec(func):
    def innerdec():
        return func() + 1

    return innerdec()


def normalfunc():
    return 3


newfunc = outerdec(normalfunc)
print(newfunc)
