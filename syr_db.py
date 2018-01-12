import sqlite3

#Create a db connection
con = sqlite3.Connection('university')

#Create a cursor to access the db
c = con.cursor()

#Create tables
def create_table():
    c.execute("CREATE TABLE students(Name VARCHAR, Rollno VARCHAR, Course TEXT)")

def enter_data_into_db():
    name = input("Enter your name: ")
    rollno = input("Enter your roll num: ")
    course = input("Enter your course: ")

    c.execute("INSERT INTO students (Name, Rollno, Course) VALUES (? ,? , ?)",(name, rollno, course))
    con.commit()

def read_data():
    name = input("Enter your name you want to read: ")
    rollno = input("Enter your roll num you want to get: ")
    sql = "SELECT * from students where name=? AND rollno = ?"
    for row in c.execute(sql,[(name),(rollno)]):
        print(row)

enter_data_into_db()
read_data()

con.close()