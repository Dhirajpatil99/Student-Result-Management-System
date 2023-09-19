import streamlit as st 
import mysql.connector 
import pandas as pd
from streamlit_option_menu import option_menu
from table_functions import triggers
from helper_functions import functions 



class login(functions,triggers):
    
    def __init__(self,host,user,password,database):
        super().__init__(host,user,password,database)
        super().create_database()
        self.mydb=super().connect()
        self.cnx=self.mydb.cursor()

    def admin_login(self):
        pswd=st.text_input("Enter Password",type="password")
        if pswd=="xxxxxx":
            st.title("Admin Page")
            with st.sidebar:
                option=option_menu(None,["Course","Teacher","Student"],icons=["person","book"],menu_icon="cast",orientation="horizontal")
            if option=="Course": 
                tmenu=option_menu(None,["View Course","Add Course","Delete Course"],icons=["",""],menu_icon="cast",orientation="horizontal")
                if tmenu=="View Course":
                   self._view_course()

                if tmenu=="Add Course":
                    course_id = st.text_input("Enter Course ID")
                    course_name = st.text_input("Enter Course Name ")
                    module = st.text_input("Enter number of modules ")
                    course_coordinator = st.text_input("Enter Course Co-ordinator code ")
                    if course_id!="" and course_name!="" and module!="" and course_coordinator != "":
                        if self._add_course(course_id,course_name,module,course_coordinator):
                            self.create_coursedetails__table(course_id)
                            self.create_student_table(course_id)
                            for i in range(1,int(module)+1):
                                self.create_module_table(course_id,str(i))
                            st.success("Course Added")
                        else:
                            st.error("Error Occured")

                if tmenu=="Delete Course":
                    course_id = st.text_input("Enter Course ID")
                    if course_id!="":
                        if self._delete_course(course_id):
                            st.success("Course Deleted")
                        else:
                            st.error("Error Occured")

            if option=="Teacher": 
                tmenu=option_menu(None,["View Teacher","Add Teacher","Delete Teacher","Teacher info","view login"],icons=["",""],menu_icon="cast",orientation="horizontal")
                if tmenu=="View Teacher":
                   self._view_teacher()
                if tmenu=="Add Teacher":
                    teacher_id = st.text_input("Enter Teacher ID")
                    teacher_name = st.text_input("Enter Teacher Name ")
                    if teacher_id!="" and teacher_name!="" :
                        if self._add_teacher(teacher_id,teacher_name):
                            st.success("Teacher Added")
                        else:
                            st.error("Error Occured")
                if tmenu=="Delete Teacher":    #first teacher is not deleted
                    teacher_id = st.text_input("Enter Course ID")
                    if teacher_id!="":
                        if self._delete_teacher(teacher_id):
                            st.success("Teacher Deleted")
                        else:
                            st.error("Error Occured")
                
                if tmenu=="Teacher info":
                    teacher_id = st.text_input("Enter Teacher ID")
                    teacher_passwd = st.text_input("Enter Teacher password")
                    if teacher_id!="" and teacher_passwd!="" :
                        if self._add_teacher_info(teacher_id,teacher_passwd):
                            st.success("Teacher login Added")
                        else:
                            st.error("Error Occured")
                    
                if tmenu=="view login":
                   self._view_teacher()


            
            if option=="Student": 
                tmenu=option_menu(None,["View Student","Add Student","Delete Student","Add Result","View Result"],icons=["",""],menu_icon="cast",orientation="horizontal")
                if tmenu=="View Student":
                   course_id=self._get_course_id()
                   self._view_Student(course_id)  ###########################
                if tmenu=="Add Student":
                    course_id=self._get_course_id()
                    Student_rollno = st.text_input("Enter Student ID")
                    Student_name = st.text_input("Enter Student Name ")
                    if Student_rollno!="" and Student_name!="" :
                        if self._add_Student(Student_rollno,Student_name,course_id):
                            st.success("Student Added")
                        else:
                            st.error("Error Occured")
                if tmenu=="Delete Student":    
                    student_rollno = st.text_input("Enter Student Roll Number")
                    if student_rollno!="":
                        if self._delete_student(student_rollno):
                            st.success("Student Deleted")
                        else:
                            st.error("Error Occured")
                if tmenu=="Add Result":
                    Id = st.text_input("Enter Roll no")
                    course_id= st.text_input("Enter course ID: ")
                    Lab = st.text_input(f"Enter  Lab Marks ")
                    McQ = st.text_input(f"Enter  McQ Marks ")
                    module_id = st.text_input("Enter Module")
                    # Instructor = st.text_input(f"Enter module  Instructor ")
                    if Id!="" and Lab!="" and McQ!="" and course_id!="" and module_id!="" :
                        if self._add_result(Id,Lab,McQ,course_id,module_id):
                            st.success("Student Added ")
                        else:
                            st.error("Error Occured ")
                if tmenu=="View Result":
                    course_id=self._get_course_id()
                    module_id=st.selectbox("option",("1","2"))
                    self._view_result(course_id,module_id)



    def teacher_login(self):
        teacher_id=st.text_input("Enter User name")
        pswd=st.text_input("Enter Password",type="password")
        if teacher_id!="" and pswd!="":
            self.cnx.execute(f"select * from teacher_cred where teacher_id = '{teacher_id}' and teacher_passwd= '{pswd}' ")
            if self.cnx.fetchone():
                st.title("Teacher Page")
                st.subheader(f"Welcome")
                option=option_menu(None,["Add Result","View Result","View Student","Add Student","Delete Student"],icons=["person","book"],menu_icon="cast",orientation="horizontal")
                if option=="Add Result":
                    Id = st.text_input("Enter Roll no")
                    course_id= st.text_input("Enter course ID: ")
                    Lab = st.text_input(f"Enter  Lab Marks ")
                    McQ = st.text_input(f"Enter  McQ Marks ")
                    module_id = st.text_input("Enter Module")
                    # Instructor = st.text_input(f"Enter module  Instructor ")
                    if Id!="" and Lab!="" and McQ!="" and course_id!="" and module_id!="" :
                        if self._add_result(Id,Lab,McQ,course_id,module_id):
                            st.success("Student Added ")
                        else:
                            st.error("Error Occured ")
                elif option=="View Result":
                    course_id=self._get_course_id()
                    module_id=st.selectbox("option",("1","2"))
                    self._view_result(course_id,module_id)

                if option=="View Student":
                   course_id=self._get_course_id()
                   self._view_Student(course_id)  ###########################
                if option=="Add Student":
                    course_id=self._get_course_id()
                    Student_rollno = st.text_input("Enter Student ID")
                    Student_name = st.text_input("Enter Student Name ")
                    if Student_rollno!="" and Student_name!="" :
                        if self._add_Student(Student_rollno,Student_name,course_id):
                            st.success("Student Added")
                        else:
                            st.error("Error Occured")
                if option=="Delete Student":    
                    student_rollno = st.text_input("Enter Student Roll Number")
                    if student_rollno!="":
                        if self._delete_student(student_rollno):
                            st.success("Student Deleted")
                        else:
                            st.error("Error Occured")
                st.session_state.role=None
            else:
                st.error("Wrong Password")
                

        

    def student_login(self):
        roll_no=st.text_input("Enter Your roll number")
        course_id=st.text_input("Enter Your course_id")
        module_id=st.text_input("Enter your module")
        if course_id!="" and module_id!="" and roll_no!="" :
            if self._view_student_result(course_id,module_id,roll_no):
                st.success("Student")                
            else:
                st.error("Not Found")

        st.session_state.role=None

