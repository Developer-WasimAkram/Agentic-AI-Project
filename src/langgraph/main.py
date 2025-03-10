import streamlit as st 
import json 
from src.langgraph.ui.streamlitui.loadui import LoadStreamlitUI


class load_langgraph_agenticai_app:
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI.")


        # Text input for user message
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe 
    else :
        user_message = st.chat_input("Enter your message:")