from typing import Optional
from dataclasses import dataclass
import streamlit as st

@dataclass
class TodoItem:
    label: str
    checked: bool

st.title('Todo List')

st.session_state.setdefault('todos', [])
st.session_state.setdefault('editing_mode', False)
st.session_state.setdefault('updating_item', None)

def change_edit_mode(editing_mode: bool, updating_item: Optional[TodoItem])->None:
    st.session_state['editing_mode'] = editing_mode
    st.session_state['updating_item'] = updating_item


updating_item = st.session_state.get('updating_item')
if st.session_state.get('editing_mode'):
    colLabel, colChecked, colUpdate = st.columns(3)
    label = colLabel.text_input("Label", value=updating_item.label if updating_item else "")
    finished = colChecked.checkbox("Finished", value=updating_item.checked if updating_item else False)
    if colUpdate.button("Save"):
        if updating_item:
            updating_item.label = label
            updating_item.checked = finished
        else:
            todos = st.session_state.get('todos')
            todos.append(TodoItem(label=label, checked=finished))
        change_edit_mode(False, None)
        st.rerun()
else:
    st.button("New Item", on_click=lambda: change_edit_mode(True, None))

todos = st.session_state.get('todos')
st.divider()
for index, t in enumerate(todos):
    colLabel, colUpdate = st.columns(2)
    if t.checked:
        colLabel.write(f"~~{t.label}~~")
    else:
        colLabel.write(t.label)
    if not st.session_state.get('editing_mode'):
        if colUpdate.button(f"Update", key=f"btnUpdate_{index}"):
            change_edit_mode(True, t)
            st.rerun()
