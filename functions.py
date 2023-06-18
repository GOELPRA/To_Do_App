FILEPATHV = "todos.txt"


def get_todo(filepath = FILEPATHV):
    """ Get the list of To Dos from the External File"""
    with(open(filepath, "r") as file):
        todos_arg=file.readlines()
    return todos_arg


def write_todo(todo_arg, filepath = FILEPATHV):
    """Write the Todos to External File"""
    with(open(filepath, "w") as file):
        file.writelines(todo_arg)


def print1():
    print("hello")