# Task 1: Calculate Area with Conditions

def calculate_area(length, width):
    area_rectangle = length * width
    if length == width:
        return 'This is a square!'
    else:
        return area_rectangle

length = int(input('Enter the length: '))
width = int(input('Enter the width: '))
area = calculate_area(length, width)
if isinstance(area, str):
    print(area)
else:
    print(f"The area of the rectangle is: {area}")

# Task 2: Generate Fibonacci Series

n=int(input('enter the nomber :'))
i=0
a=0
b=1
c=0
while c<=n:
    print(c,end=' ')
    a=b
    b=c
    c=a+b
print(c)

# Task 3:

import mysql.connector as c
con=c.connect(host="localhost",user="root",password="root",database="assignment")
if con.is_connected(): 
    print("Connected")
while True:
    first_name=input('Enter Student First Name :')
    last_name=input('Enter Student Last Name :')
    age=int(input('Enter Student Age :'))
    grade=float(input('Enter Student Grade :'))
    cursor=con.cursor()
    query="insert into student (first_name,last_name,age,grade) values('{}','{}',{},{})".format(first_name,last_name,age,grade)
    cursor.execute(query)
    con.commit()
    print('data submitted')
    x=int(input('1->Enter More\n2->Exit\n'))
    if x==2:
        break

first_name=input('Enter First Name :')
grade=float(input('Enter Grade :'))
q1="update student set grade={} where first_name='{}'".format(grade,first_name)
cursor=con.cursor()
cursor.execute(q1)
con.commit()
print('data updated')

last_name=input('Enter Student Last Name :')
q2="delete from student where last_name='{}'".format(last_name)
cursor=con.cursor()
cursor.execute(q2)
con.commit()
print('data deleted')

print('All Student Records')
cursor=con.cursor()
q3="select * from student"
cursor.execute(q3)
display=cursor.fetchall()
print(display)