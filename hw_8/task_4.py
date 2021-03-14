import os


def myWalk(path):
    arr = []

    def foo(path_):
        for i in os.listdir(path_):
            if os.path.isdir(path_ + '/' + i):
                arr.append((path_ + '/' + i, 'dir'))
                foo(path_ + '/' + i)
            else:
                arr.append((path_ + '/' + i, 'file'))

    foo(path)

    return arr
