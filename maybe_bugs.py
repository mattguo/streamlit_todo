import streamlit as st

# The issue is, no matter if I clicked which of the 3 buttons, I always got "clicked 2" output 
for i in range(3):
    st.button(f"Button {i}", key=f"btn_{i}", on_click=lambda: st.warning(f"clicked {i}"))
