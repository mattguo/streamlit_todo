import streamlit as st


for i in range(3):
    st.button(f"Button {i}", key=f"btn_{i}", on_click=lambda: st.warning(f"clicked {i}"))
