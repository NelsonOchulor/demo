
import mysql.connector
# established connection between your database
mysqldb = mysql.connector.connect(
    host="localhost", user="root", password="", database="project1")
mycursor = mysqldb.cursor()  # cursor() method create a cursor object

try:
    # Execute SQL Query to select all record
    mycursor.execute("select * from personal_record")
    result = mycursor.fetchall()  # fetches all the rows in a result set
    for i in result:
        client_ID = i[0]
        first_name = i[1]
        last_name = i[2]
        birth_date = i[3]
        address = i[4]
        city = i[5]
        state = i[6]
        post_code = i[7]
        contact = i[8]
        email = i[9]
        print(first_name, last_name, birth_date, address,
              city, state, post_code, contact, email)
        print('Record Read successfully...')
except:
    print('Error:Unable to fetch data.')
mysqldb.close()  # Connection Close
