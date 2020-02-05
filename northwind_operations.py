from northwind import *


operation = input("please enter your character fro CRUD operations")

my_table = CRUD("")

if operation == 'C':
    table_choosen = input("introduce table name")
    my_table.create_operation(table_choosen)
elif operation == "R":
    my_result_set = my_table.read_operation(input("introduce table name"))
    my_table.print_result_set(my_result_set)
elif operation == "U":
    my_table.update_operation(input("introduce table name"))
elif operation == "D":
    my_table.delete_operation(input("introduce table name"))



