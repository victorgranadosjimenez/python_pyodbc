
import pyodbc

class NorthWind:
    def __init__(self):
        self.server = "localhost,1433"
        self.database_name = "NorthWind"
        self.user_name = "SA"
        self.password = "Passw0rd2018"
#we having an handle creating the variable connection to use the result of the connect method
        self.connection = pyodbc.connect('DRIVER={ODBC DRIVER 17 for SQL SERVER};'
                                                'SERVER=' + self.server + ';'
                                                'DATABASE=' + self.database_name + ';'
                                                'UID=' + self.user_name + ';'
                                                'PWD=' + self.password)
        self.my_northwind_cursor = connection.cursor()
operation = input("which CRUD operation do you want to run")
table = input("Please provide the table name")


def read_operation(table_name):
    result_set = my_northwind_cursor.execute("SELECT * FROM {}".format(table_name))
    print_result_set(result_set)
def create_operation(table_name, column_name, data_type):
    result_set = my_northwind_cursor.execute("ALTER TABLE {} ADD {} {}".format(table_name, column_name, data_type))
    print_result_set(result_set)
def update_operation(table_name, column_name, condition):
    result_set = my_northwind_cursor.execute("UPDATE {} SET {} WHERE {}".format(table_name, column_name, condition))
    print_result_set(result_set)
def delete_operation(table_name, condition):
    result_set = my_northwind_cursor.execute("DELETE FROM {} WHERE {}".format(table_name, condition))
    print_result_set(result_set)


def print_result_set(result_set):
    for item in result_set:
        print(item)


if(operation == "C"):
    column_name = input("please introduce column name")
    data_type = input ("please introduce the type of data")
    create_operation(table,column_name,data_type)
elif(operation == "R"):
    read_operation(table)
elif(operation == "U"):
    column_name = input("please introduce column name")
    condition = input("please introduce the where condition")
    update_operation(table,column_name,condition)
elif(operation == "D"):
    condition = input("please introduce the where condition")
    table_name = table
    delete_operation(table_name,condition)

