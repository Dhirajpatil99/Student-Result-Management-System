import mysql.connector

class dbconnection():
    __host = ""
    __user = ""
    __password = ""
    __database = ""
    _cnx =""
    _mydb=""

    def __init__(self, hostname, user, password, database):
        self.__host = hostname
        self.__user = user
        self.__password = password
        self.__database = database
        
        

    def create_database(self):
        self._mydb = mysql.connector.connect(host=self.__host, user=self.__user, password=self.__password)
        self._cnx = self._mydb.cursor()
        self._cnx.execute(f"create database if not exists {self.__database};")
        self._cnx.execute(f"use {self.__database}; ")

    def connect(self):
        return self._mydb

    def __del__(self):
        self._mydb.close()
        

class create_table(dbconnection):

    def __init__(self,hostname,user,password,database):
        super().__init__(hostname,user,password,database)
        super().create_database()
        mydb=super().connect()
        self._cnx=mydb.cursor()

    def create_course_table(self):
        self._cnx.execute(f"""create table if not exists course
(course_id varchar(255) primary key not null,
course_name text,
number_of_modules int not null,
course_co_ordinator varchar(255),
foreign key (course_co_ordinator) references teacher_details(teacher_id)
);""")

        
        

    def create_teacher_table(self):
        self._cnx.execute("""create table if not exists teacher_details
                    ( 
                    teacher_id varchar(255) primary key not null,
                    teacher_name varchar(255) not null
                    );""")
        
    def create_teacher_cred(self):
        self._cnx.execute("""create table if not exists teacher_cred
                    ( 
                    teacher_id varchar(255) not null,
                    teacher_passwd varchar(255) not null,
                    foreign key (teacher_id) references teacher_details(teacher_id)
                    );""")
        
        
    
    


class triggers(dbconnection):

    def __init__(self,hostname,user,password,database):
        super().__init__(hostname,user,password,database)
        super().create_database()
        mydb=super().connect()
        self._cnx=mydb.cursor()

        

    def create_module_table(self,course_name,module_id):
        self._cnx.execute(f"""create table if not exists {course_name}_{module_id}_student_details
                    (
                    roll_no int primary key not null,
                    mcq int,
                    lab int,
                    foreign key (roll_no) references {course_name}_student_details(roll_no)
                    );""")
        
        
    def create_student_table(self,course_name):
        self._cnx.execute(f"""create table if not exists {course_name}_student_details
                    (
                    roll_no int primary key not null,
                    student_name varchar(255)
                    );""")
        
        
    def create_coursedetails__table(self,course_id):
        self._cnx.execute(f"""create table if not exists {course_id}_details
                    (
                    MODULEid int,
                    module_name varchar(255),
                    teacher_id varchar(255),
                    foreign key (teacher_id) references teacher_details(teacher_id)
                    );""")
        
        

    
    

