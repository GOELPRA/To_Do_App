import streamlit as st
import functions
todos = functions.get_todo()


def add_t():
    todo_1 = st.session_state["N_todo"]
    todos.append(todo_1 + "\n")
    functions.write_todo(todos)
    st.session_state["N_todo"] = ""


st.title("My Todo App")
st.subheader("This is a sub-header")
st.write("Hello world")

i = 0

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)

    if checkbox:
        todos.pop(index)
        functions.write_todo(todos)
        del st.session_state[todo]
        st.experimental_rerun()

    i = i + 1

st.text_input(label="Add to do", placeholder="Add new todo:", on_change=add_t, key="N_todo")

st.session_state