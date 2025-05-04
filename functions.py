def get_todos(filename="./todos.txt"):
    """
    Reads a text file and returns the list of to-do items
    """
    with open(filename, 'r') as file:
        todos = file.readlines()
    for index, todo in enumerate(todos):
        todos[index] = todo[:-1]
    return todos

def save_todos(todos_local, filename="./todos.txt"):
    """
    Stores the to-do items list into a text file
    :param todos_local: to-do items list to write
    :param filename: name of the file where to store the list
    :return: None
    """
    copy = []
    for index, todo in enumerate(todos_local):
        copy.append(todo + '\n')
    with open(filename, 'w') as file:
        file.writelines(copy)