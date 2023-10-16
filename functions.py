# this is our functions file  :)
# todos = []


def get_todos(filepath="todos.txt"):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos, filepath="todos.txt"):
    with open(filepath, 'w') as file:
        file.writelines(todos)


if __name__ == "__main__":
    while True:
        user_input = input("enter add , show , edit , complete , exit : ")
        user_input = user_input.strip()

        if user_input.startswith("add"):
            todo = user_input[4:]
            todos = get_todos()
            todos.append(todo + '\n')
            write_todos(todos)

        elif user_input.startswith("show"):
            todos = get_todos()
            for index, todoo in enumerate(todos):
                todoo = todoo.strip('\n')

                row = f"{index + 1}-{todoo}"
                print(row)

        elif user_input.startswith("edit"):
            try:

                number = int(user_input[5:])
                number = number - 1
                todos = get_todos()
                print('here before changing values', todos)
                new_todo = input("enter new todo : ")
                todos[number] = new_todo + '\n'
                print('here after changing values', todos)
                write_todos(todos)
            except ValueError:
                print("invalid command!")
                continue

        elif user_input.startswith("complete"):
            try:

                todos = get_todos()

                number = int(user_input[8:])
                removed_todo = todos[number - 1].strip('\n')
                todos.pop(number - 1)
                write_todos(todos)

                message = f"Todo {removed_todo} is removed from list"
                print(message)
            except IndexError:
                print("invalid Index!")
                continue
        # if whatever in user_input:

        #   print("hey , you just entered wrong ")
        elif user_input.startswith("exit"):
            break
        else:
            print("Invalid command")
    print("bye!")
