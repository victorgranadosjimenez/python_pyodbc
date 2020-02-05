import pyodbc

class customers ():
    #creating the constructor method, only once innit
    def __init__(self, customerID, compa_name, cont_name, contact_title, address, city, region, postal_code, country, phone, fax):
        self.customerID = customerID
        self.company_name = compa_name
        self.contact_name = cont_name
        self.contact_title = contact_title
        self.address = address
        self.city = city
        self.region = region
        self.phone = phone
        self.postal_code = postal_code
        self.country = country
        self.fax = fax
        server = "localhost,1433"
        database_name = "Northwind"
        user_name = "sa"
        password = "Passw0rd2018"
        self.docker_Northwind = pyodbc.connect('DRIVER={ODBC DRIVER 17 for SQL SERVER};'
                                                'SERVER=' + server + ';'
                                                'DATABASE=' + database_name + ';'
                                                'UID=' + user_name + ';'
                                                'PWD=' + password)
        self.cursor = self.docker_Northwind.cursor()


    def save_to_database(self):
        sql_insert = "INSERT INTO Customers( CustomerID, CompanyName, ContactName, ContactTitle, Address, City, Region, PostalCode, Country, Phone, Fax) \
        VALUES ({},{},{},{},{},{},{},{},{},{},{})".format(self.customerID, self.company_name, self.contact_name, self.contact_title, self.address, self.city, self.region, self.postal_code, \
        self.country, self.phone, self.fax)

        self.cursor.execute(sql_insert)
        self.cursor.commit()

        print(sql_insert)


    def delete_from_database(self, where_clause):
        self.where_clause = where_clause
        sql_delete = "DELETE * FROM Customers WHERE {}".format(self.where_clause)

        self.cursor.execute(sql_delete)
        self.cursor.commit()

    def update_customers(self, column, where_condition):
        self.column = column
        self.where_condition = where_condition
        sql_update = "UPDATE Customers SET {} WHERE {}".format(self.column, self.where_condition)

        self.cursor.execute(sql_update)
        self.cursor.commit()

    def create_table(self, new_table, new_row, datatype):
        self.new_table = new_table
        self.new_row = new_row
        self.datatype = datatype
        sql_create = "CREATE {} ({} {});".format(self.new_table, self.new_row, self.datatype)

        self.cursor.execute(sql_create)
        self.cursor.commit()





# customer1 = customers("'008'", "'Sparta'", "'james'", "'Sir'", "'Homeless'", "'London'", "'SE'", "'WD2'", "'UK'", "'077'", "'What?'")
# customer1.save_to_database()