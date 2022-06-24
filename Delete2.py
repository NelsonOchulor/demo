import mysql.connector
# established connection between your database
mysqldb = mysql.connector.connect(
    host="localhost", user="root", password="UGconnect2002", database="project1")
mycursor = mysqldb.cursor()  # cursor() method create a cursor object
try:
    # Execute SQL Query to detete a record
    mycursor.execute("DELETE FROM personal_backup WHERE client_ID=21")
    mysqldb.commit()  # Commit is used for your changes in the database
    print('Record deleted successfully...')
except:
    # rollback used for if any error
    mysqldb.rollback()
mysqldb.close()  # Connection Close
