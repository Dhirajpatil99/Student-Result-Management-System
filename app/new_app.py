import streamlit as st
from login import login as l

from streamlit_option_menu import option_menu
st.set_page_config(page_title="Result Management System")
l=l("localhost","root","root","management_system")
st.title("Result Management System")
with st.sidebar:
    choice=option_menu("ROLES",("ADMIN","TEACHER","STUDENT"))
if choice=="ADMIN":
    l.admin_login()
if choice=="TEACHER":
    st.session_state.role="teacher"
    l.teacher_login()
if choice=="STUDENT":
    st.session_state.role="student"
    l.student_login()