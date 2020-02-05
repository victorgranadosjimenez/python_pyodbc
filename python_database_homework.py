

import pyodbc



class Region:
    def __init__(self, regionID, region_description):
        self.regionID = regionID
        self.region_description = region_description

class Suppliers:
    def __init__(self, supplierID, company_name, contact_name, contact_title, address, city, region, postal_code, country, phone, fax, home_page):
        self.supplierID = supplierID
        self.company_name = company_name
        self.contact_name = contact_name
        self.contact_title = contact_title
        self.address = address
        self.city = city
        self.region = region
        self.postal_code = postal_code
        self.country = country
        self.phone = phone
        self.fax = fax
        self.home_page = home_page


class Connection:
    def __init__(self):
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


# class ReadOperation:
#     def __init__(self, sql):
#         self.ops = sql
#
# class Program_Main:
#     def __init__(self):
#         self.result = ""
#
#     def run(self):
#         #run program
#         return ""
#
    def crud_operation(self,table_choosen, column_choosen, where_condition, datatype):
        # crud=create read update delete
        self.table_choosen = table_choosen
        self.column_choosen = column_choosen
        self.where_condition = where_condition
        self.datatype = datatype

        sql_create = "CREATE {} ({} {});".format(self.table_choosen, self.column_choosen, self.datatype)
        sql_read= "SELECT FROM {}".format(table_choosen)
        sql_update = "UPDATE {} SET {} WHERE {}".format(self.table_choosen, self.column_choosen, self.where_condition)
        sql_delete = "DELETE FROM {} WHERE {}".format(self.table_choosen, self.where_condition)

        self.cursor.execute(sql_create)
        self.cursor.execute(sql_read)
        self.cursor.execute(sql_update)
        self.cursor.execute(sql_delete)
        self.cursor.commit()
        result = ""
#
#
#
# main_prog = Program_Main()
# main_prog.run()