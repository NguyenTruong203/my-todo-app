import streamlit as st
import functions

todos = functions.get_todos()


def add_todo(): # a call-back function
    todo = st.session_state["new_todo"] + "\n" #dictionary
    todos.append(todo)
    functions.write_todos(todos)


todos = functions.get_todos()
st.title("My Todo App")
st.subheader("Mỗi ngày tôi chọn 1 niềm vui")
st.write("Chọn những bông hoa chọn những nụ cười")
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        st.experimental_rerun()

st.text_input(label="Enter a todo:", placeholder="Add new todo",
              on_change=add_todo, key='new_todo')

