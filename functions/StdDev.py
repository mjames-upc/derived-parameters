from numpy import std, dstack

def execute(*args):
    if len(args) == 1 and isinstance(args[0], list):
        return execute(*args[0])
    return dstack(args).std(axis=2)
