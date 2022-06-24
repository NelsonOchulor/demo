import mysql.connector
# established connection between your database
mysqldb = mysql.connector.connect(
    host="localhost", user="root", password="UGconnect2002", database="project1")
mycursor = mysqldb.cursor()  # cursor() method create a cursor object
try:
    mycursor.execute(
        "UPDATE personal_record SET first_name = 'Tony', state = 'Maryland' WHERE client_ID = 53")
    mysqldb.commit()  # Commit is used for your changes in the database
    print('Record updated successfully...')
except:
    # rollback used for if any error
    mysqldb.rollback()
mysqldb.close()  # Connection Close
