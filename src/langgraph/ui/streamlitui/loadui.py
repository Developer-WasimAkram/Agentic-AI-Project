import streamlit as st  
import os 
import sys
from datetime import datetime

from langchain_core.messages import HumanMessage,AIMessage
from src.langgraph.ui.uiconfigfile import Config
class LoadStreamlitUI:
    
    def __init__(self):
        self.config=Config()
        self.user_controls={}
        
    def initialize_session(self):
        return {
        "current_step": "requirements",
        "requirements": "",
        "user_stories": "",
        "po_feedback": "",
        "generated_code": "",
        "review_feedback": "",
        "decision": None
    } 
        
        
        
    def load_streamlit_ui(self):
        st.set_page_config(
            page_title="🤖 " + self.config.get_page_title(),layout="wide")
         
        st.header(self.config.get_page_title())
        st.session_state.timeframe =''
        st.session_state.IsFetchButtonClicked = False
        st.session_state.IsSDLC = False
        
        
        with st.sidebar:
            
            #Get options from config
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()
            groq_model_options = self.config.get_groq_model_options()
            
            #Select LLM
            self.user_controls["select_llm"] =st.selectbox("Select LLM",llm_options)
            
            if self.user_controls["select_llm"] == "Groq":
                #Model  Selection
                self.user_controls["select_gorq_model"] = st.selectbox("Select GroQ Model", groq_model_options)
                #API key input
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"]=st.text_input("API Key",type="password")
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your GROQ API key to proceed. Don't have? refer : https://console.groq.com/keys ")
                   
            
            #Select Usecase
            self.user_controls["select_usecase"] = st.selectbox("Select Usecase", usecase_options)
            
            if "state" not in st.session_state:
                st.session_state.state = self.initialize_session()
                
                
        return self.user_controls
                
a=LoadStreamlitUI()