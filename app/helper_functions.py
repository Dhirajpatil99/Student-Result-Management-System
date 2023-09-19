from table_functions import dbconnection
import pandas as pd
import streamlit as st

class functions(dbconnection):
    
    def __init__(self,host,user,password,database):
        super().__init__(host,user,password,database)
        super().create_database()
        self.mydb=super().connect()
        self.cnx=self.mydb.cursor()
    
    def _view_course(self):
        self.cnx.execute("Select * from course")
        st.table(pd.DataFrame(self.cnx.fetchall(),columns=["Course_ID","Course_name","Total Modules","Co-ordinator"]))

    def _get_course_id(self):
         self.cnx.execute("select course_id from course;")
         option=self.cnx.fetchall()
         course_id=st.selectbox("option",("D01",))
         return course_id

    def _add_course(self,course_ID,course_name,modules,coordinator):
            try:
                self.cnx.execute(f"insert into course values('{course_ID}','{course_name}',{int(modules)},'{coordinator}') ")
                self.mydb.commit()
                return 1
            except:
                 return 0
            
    def _delete_course(self,course_ID):
            try:
                self.cnx.execute(f"delete from  course where course_id like '{course_ID}' ")
                self.mydb.commit()
                return 1
            except:
                 return 0
            
    def _add_teacher(self,teacher_id,teacher_name):
            try:
                self.cnx.execute(f"insert into teacher_details values('{teacher_id}','{teacher_name}') ")
                self.mydb.commit()
                return 1
            except:
                 return 0
            
    def _add_teacher_info(self,teacher_id,teacher_passwd):
             try:
                self.cnx.execute(f"insert into teacher_cred values('{teacher_id}','{teacher_passwd}')")
                self.mydb.commit()
                return 1
             except:
                return 0
             
    def _view_teacher_info(self):
         self.cnx.execute("select teacher_id,teacher_passwd from teacher_cred")
         st.table(pd.DataFrame(self.cnx.fetchall(),columns=["teacher_id","teacher_passwd"]))
        
            
    def _add_Student(self,roll_no,Student_name,course_id):
            try:
              self.cnx.execute(f"insert into {course_id}_student_details values('{roll_no}','{Student_name}') ")
              self.mydb.commit()
              return 1
            except:
                 return 0
            
    def _add_result(self,roll_no,Lab,McQ,course_id,module_id):
          try:
              self.cnx.execute(f"insert into {course_id}_{module_id}_student_details values('{roll_no}','{Lab}','{McQ}') ")
              self.mydb.commit()
              return 1
          except:
                 return 0
    
    def _view_result(self,course_id,module_id):
         self.cnx.execute(f"select * from {course_id}_{module_id}_student_details")
         st.table(pd.DataFrame(self.cnx.fetchall(),columns=["roll_no","Lab","McQ"]))
              
    
    def _view_teacher(self):
        self.cnx.execute("Select * from teacher_cred")
        st.table(pd.DataFrame(self.cnx.fetchall(),columns=["Teacher ID","Teacher Name"]))


    def _delete_teacher(self,teacher_ID):
            try:
                self.cnx.execute(f"delete from  teacher_details where teacher_id like '{teacher_ID}' ")
                self.mydb.commit()
                return 1
            except:
                 return 0
            
    def _delete_student(self,student_ID):
            try:
                self.cnx.execute(f"delete from  d01_student_details where roll_no like '{student_ID}' ")
                self.mydb.commit()
                return 1
            except:
                 return 0
            

    def _view_Student(self,course_id):
        self.cnx.execute(f"Select * from {course_id}_student_details")  ###################manucal written number
        st.table(pd.DataFrame(self.cnx.fetchall(),columns=["roll_no","student_name"]))


    def _view_student_result(self,course_id,module_id,roll_no):
        try:
            self.cnx.execute(f"Select * from {course_id}_{module_id}_student_details where roll_no={roll_no}")  ###################manucal written number
            st.table(pd.DataFrame(self.cnx.fetchall(),columns=["roll_no","McQ","Lab"]))
            return 1
        except:
            return 0
