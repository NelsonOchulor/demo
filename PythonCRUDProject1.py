import mysql.connector
from mysqlx import DeleteStatement
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 2000)

# established connection between your database
mysqldb = mysql.connector.connect(
    host="localhost", user="root", password="", database="project1")
mycursor = mysqldb.cursor()  # cursor() method create a cursor object

try:
    # Execute SQL Query to select all record
    mycursor.execute("select * from personal_record")
    result = mycursor.fetchall()  # fetches all the rows in a result set

    def createNewClient():
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
            sql = "INSERT INTO personal_record (first_name, last_name, birth_date, address, city, state, post_code, contact, email) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (first_name, last_name, birth_date, address,
                      city, state, post_code, contact, email)
            mycursor.execute(sql, values)
            mysqldb.commit()
            print('Personal Record Data Saved Successfully')

        except:
            print('Something wrong with Personal Record, please check')

    def displayAllclients():
        mycursor.execute("SELECT * FROM personal_record")
        myresult = mycursor.fetchall()
        for x in myresult:
            x = pd.DataFrame(myresult, columns=['ID', 'First', 'Last', 'Birth Date',
                                                'Address', 'City', 'State', 'Postal Code', 'contact', 'email'])
        print(x)

    print('Record Read successfully...')
except:
    print('Error:Unable to fetch data.')

# mysqldb.close()  # Connection Close


def deleteClient():
    global client_ID
    client_ID = input("Please Enter Client ID you want to Delete")

    # Execute SQL Query to detete a record
    sql = "DELETE FROM driving_record WHERE client_ID= %s"
    values = (client_ID,)
    mycursor.execute(sql, values)
    mysqldb.commit()  # Commit is used for your changes in the database

    sql = "DELETE FROM health_record WHERE client_ID= %s"
    values = (client_ID,)
    mycursor.execute(sql, values)
    mysqldb.commit()  # Commit is used for your changes in the database

    sql = "DELETE FROM personal_record WHERE client_ID= %s"
    values = (client_ID,)
    mycursor.execute(sql, values)
    mysqldb.commit()  # Commit is used for your changes in the database
    print('Record deleted successfully...')

    # rollback used for if any error
    mysqldb.rollback()


def updateClient():
    while True:
        print(
            "Press 1 to change First Name, 2 to change Last Name, 3 to change Phone Number, 4 to exit")

        # take the user input for the selection
        sel2 = int(input("\nSelection: "))

        if sel2 == 1:
            client_ID = input("Enter Client ID")
            first_name = input(
                "Please Enter  Client's Updated First Name ")
            sql = "update personal_record SET first_name = %s WHERE client_ID = %s"
            values = (first_name, client_ID)
            mycursor.execute(sql, values)
            mysqldb.commit()
        elif sel2 == 2:
            client_ID = input("Enter Client ID")
            last_name = input("Please Enter  Client's Updated last Name ")
            sql = "update personal_record SET last_name = %s WHERE client_ID = %s"
            values = (last_name, client_ID)
            mycursor.execute(sql, values)
            mysqldb.commit()
        elif sel2 == 3:
            client_ID = input("Enter Client ID")
            contact = input("Please Enter  Client's Updated Phone Number ")
            sql = "update personal_record SET contact = %s WHERE client_ID = %s"
            values = (contact, client_ID)
            mycursor.execute(sql, values)
            mysqldb.commit()
        elif sel2 == 4:
            break


def startup():                                  # the startup function is called below so that it can run
    while True:                                 # this will loop infinitely because the condition is always True
        # create a menu to give the user options
        print("Welcome To Amazing Insurance Company!")
        print("\t1. Create Client.")
        print("\t2. Display All Clients")
        print("\t3. Update Client.")
        print("\t4. Delete Client")
        print("\t5. Quit")
        # We want to check for an error if the user inputs a non-integer value
        while True:
            try:
                # take the user input for the selection
                sel = int(input("\nSelection: "))
            except ValueError:
                print(ValueError)
                print("Please Enter an Integer 1-5!")
            else:
                break
        if sel == 1:                            # if-else statement checks for each possible selection
            # runs the insert_emp() function defined above
            createNewClient()
        elif sel == 2:
            displayAllclients()
        elif sel == 3:
            updateClient()
        elif sel == 4:
            deleteClient()

        elif sel == 5:
            print("Thank you! Have a good day!")
            break                               # immediately break the loop
        else:
            print("Please make a valid input.")


startup()  # This will run when the program starts
