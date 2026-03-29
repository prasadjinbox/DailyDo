from os import remove

import streamlit as st
import functions as fc


# ---------- Session state ----------
if "show_dialog" not in st.session_state:
    st.session_state["show_dialog"] = False
if "selected_todo" not in st.session_state:
    st.session_state["selected_todo"] = None
if "message" not in st.session_state:
    st.session_state["message"] = ""


# ---------- Load data ----------
todos = fc.generate_list_todos_from_file()
#print(todos)

# ---------- Functions ----------
# Add a new item to the list.
def add_item_todos() :
    new_item = st.session_state["new_todos_item"]
    if new_item:
        todos.append(new_item + "\n")
        fc.write_list_todos_to_file(todos)
        st.session_state["new_todos_item"] = ""

def open_confirm_dialog(todo_item):
    st.session_state.selected_todo = todo_item
    st.session_state.show_dialog = True


@st.dialog("Confirm Completion")
def show_popup():

    selected = st.session_state.selected_todo
    st.write(f"Are you ready to continue completion - {st.session_state['selected_todo'].strip()}?\n ?")

    if st.button("Yes", key="confirm_btn", type="primary"):
        if selected in todos:
            todos.remove(selected)
            fc.write_list_todos_to_file(todos)
            st.session_state.message = f"{selected} - Removed from the List"
        st.session_state.show_dialog = False
        st.session_state.selected_todo = None
        st.rerun()

    if st.button("No", key="cancel_btn"):
        st.session_state.show_dialog = False
        st.session_state.selected_todo = None
        st.rerun()

# ---------- UI ----------


st.title("Your Check List")
st.subheader("Smart way to follow up your check list")
st.write("Here is your check list")

if st.session_state.message :
    st.success(st.session_state.message)
    st.session_state.message = ""


for i,item in enumerate(todos):
    col1, col2 = st.columns([5,1])
    with col1:
        st.write(item)
    with col2:
        st.button("complete", key=f"complete_{i}", on_click=open_confirm_dialog, args=(item,))


if st.session_state.show_dialog :
    show_popup()



st.text_input(label="Enter an item to the list : ", placeholder="Enter an item to the list", key="new_todos_item", on_change=add_item_todos)
print("Hello")

st.write("------- Debug --------")
st.session_state.message = ""
st.session_state