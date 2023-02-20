# todos = []
def get_todos(filepath):
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_local):
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_local)


while True:
    user_action = input("Type add, show, edit, complete: ")
    user_action = user_action.strip().lower()
    match user_action:
        case "add":
            todo = input("Enter a todo:") + "\n"
            file = open("todo.txt", "r")
            todos = file.readlines()
            todos.append(todo)
            file.close()
            write_todos("todo.txt", todos)
        case "show":
            file = open("todo.txt", "r")
            todos = file.readlines()
            file.close()
            for index, item in enumerate(todos):
                print(f"{index + 1}-{item}")
        case "edit":
            number = int(input("Enter an index of the todo list to edit: "))
            number = number - 1
            todos = get_todos("todo.txt")
            new_todo = input("Edit your todo:") + "\n"
            todos[number] = new_todo
            with open("todo.txt", "w") as file:
                file.writelines(todos)

        case "complete":
            number = int(input("Enter an index of the todo list to complete: "))
            with open("todo.txt", "r") as file:
                todos = file.readlines()
            index = number - 1
            todo_to_remove = todos.pop(index)
            write_todos("todo.txt", todos)
            print(f"Todo {todo_to_remove} has been removed from the list")

        case "exit":
            break
print("See you again!")
