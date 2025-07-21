## We will be creating a databse student.db using sqlite3 using this code, running this in the terminal will create the database here 

#we will create the code to use the sqlite 3 database here
import sqlite3

##connect to sqlite
connection = sqlite3.connect("student.db")

#create a cursor object to insert rec0rd, create table
cursor = connection.cursor()

##create the table
table_info = """
create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),
SECTION VARCHAR(25), MARKS INT) 
"""#varchar means it has alphanumeric values and each value has 25 characters, int means integer values

cursor.execute(table_info) #this will create the table 

##Inserting some records
cursor.execute('''Insert Into STUDENT values('Rohan', 'Probability and Statistics' , 'A', '95')''')
cursor.execute('''Insert Into STUDENT values('Ayushi', 'Probability and Statistics' , 'A', '92')''')
cursor.execute('''Insert Into STUDENT values('John', 'Devops' , 'B', '71')''')
cursor.execute('''Insert Into STUDENT values('Pradeep', 'Probability and Statistics' , 'B', '49')''')
cursor.execute('''Insert Into STUDENT values('Pratyush', 'Probability and Statistics' , 'A', '93')''')
cursor.execute('''Insert Into STUDENT values('Sakshi', 'Devops' , 'A', '91')''')
cursor.execute('''Insert Into STUDENT values('Ali', 'Devops' , 'B', '82')''')
cursor.execute('''Insert Into STUDENT values('Komal', 'Probability and Statistics' , 'A', '75')''')
cursor.execute('''Insert Into STUDENT values('Mihir', 'Devops' , 'B', '58')''')

## Display all the records
print("The inserted records are ")
data = cursor.execute('''SELECT * FROM STUDENT''') #* means select all
for row in data:
    print(row)
    
## Commit your changes to database
connection.commit()
connection.close() #it is important to do this step