import table_functions as tf



db=tf.create_table("localhost","root","root","management_system")
#creating teacher table if not created
db.create_teacher_table()
#creating course table if not created
db.create_course_table()

db.create_teacher_cred()




