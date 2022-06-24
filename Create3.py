import mysql.connector
# established connection between your database
mysqldb = mysql.connector.connect(
    host="localhost", user="root", password="UGconnect2002", database="project1")
mycursor = mysqldb.cursor()  # cursor() method create a cursor object

first_name = input('Enter First Name = ')
last_name = input('Enter Last Name = ')
birth_date = input('Enter Birth Date = ')
address = input('Enter Address = ')
city = input('Enter City = ')
state = input('Enter State = ')
post_code = str(input('Enter Post Code = '))
contact = input('Enter Contact Number = ')
email = input('Enter email = ')

try:
    mycursor.execute(
        f"INSERT INTO personal_record VALUES (default, '{first_name}', '{last_name}', '{birth_date}', '{address}', '{city}', '{state}', '{post_code}', '{contact}', '{email}')")

    mysqldb.commit()  # Commit is used for your changes in the database
    print('Personal Record Data Saved Successfully')

except:
    print('Something wrong with Personal Record, please check')

mysqldb.close()  # Connection Close
