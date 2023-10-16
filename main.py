import streamlit as sp
import functions


todos = functions.get_todos()

def add_todo():
    todo = sp.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)



sp.title("MY TODO APP")
sp.subheader("this is my todo app :-by sai patil")
sp.text("this app to increase your productivity")

for index,todo in enumerate(todos):
    checkbox = sp.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del sp.session_state[todo]
        sp.rerun()


sp.text_input(label="",placeholder="Enter Todo Here...",on_change=add_todo,key='new_todo')
print("hello")
