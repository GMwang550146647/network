from __future__ import print_function
import os
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
import re
from configs import DB_NAME, TABLES


class DataBase():
    def __init__(self, user_name="root"):
        self.user_name = user_name
        self.cursor = None
        self.cnx = None
        self.data_dir = '../data'
        self.file_list = [
            "load_employees.dump", "load_titles.dump", "load_departments.dump",
            "load_salaries.dump", "load_dept_emp.dump", "load_dept_manager.dump"
        ]
        self.tables=[re.findall(r'load_(.+?)\.dump',filei)[0] for filei in self.file_list]

    def __enter__(self):
        self.cnx = mysql.connector.connect(user=self.user_name)
        self.cursor = self.cnx.cursor()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.cnx.close()

    def select_database(self, db_name):
        try:
            self.cursor.execute("USE {}".format(db_name))
        except mysql.connector.Error as err:
            print("Database {} does not exists.".format(DB_NAME))
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                self.create_database()
                print("Database {} created successfully.".format(DB_NAME))
                self.cnx.database = DB_NAME
            else:
                print(err)
                exit(1)

    def create_database(self):
        try:
            self.cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)

    def create_tabels(self, tables):
        for table_name in tables:
            table_description = TABLES[table_name]
            try:
                print("Creating table {}: ".format(table_name), end='')
                self.cursor.execute(table_description)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")

    def load_data(self):
        """
        加载数据可能会出错，一次上传的太大了，通过设置以下内容可以更改
            mysql -u root
            set global max_allowed_packet=268435456; 248
        :return:
        """
        for filei in self.file_list:
            with open(os.path.join(self.data_dir, filei)) as f:
                content = f.read()
                self.cursor.execute(content)
        self.cnx.commit()

    def insert_data(self):
        # 1.增加员工信息
        tomorrow = datetime.now().date() + timedelta(days=1)
        data_employee = ('Geert', 'Vanderkelen', tomorrow, 'M', date(1977, 6, 14))
        add_employee = ("INSERT INTO employees "
                        "(first_name, last_name, hire_date, gender, birth_date) "
                        "VALUES (%s, %s, %s, %s, %s)")
        self.cursor.execute(add_employee, data_employee)

        # 2.修改员工
        emp_no = self.cursor.lastrowid
        print("emp_no = cursor.lastrowid  ->".format(emp_no))
        add_salary = ("INSERT INTO salaries "
                      "(emp_no, salary, from_date, to_date) "
                      "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")
        data_salary = {
            'emp_no': emp_no,
            'salary': 50000,
            'from_date': tomorrow,
            'to_date': date(9999, 1, 1),
        }
        self.cursor.execute(add_salary, data_salary)

        # 3.确保数据已提交
        self.cnx.commit()

    def query_data(self):
        query = ("SELECT first_name, last_name, hire_date FROM employees "
                 "WHERE hire_date BETWEEN %s AND %s")
        hire_start = date(1999, 1, 1)
        hire_end = date(1999, 12, 31)
        self.cursor.execute(query, (hire_start, hire_end))

        for (first_name, last_name, hire_date) in self.cursor:
            print("{}, {} was hired on {:%d %b %Y}".format(last_name, first_name, hire_date))

    def drop_database(self,db_name):
        query="drop database {};".format(db_name)
        self.cursor.execute(query)
        self.cnx.commit()

    def main(self):
        # 1.选择某一个数据库（如果不存在则创建）
        self.select_database(DB_NAME)
        # 2.创建各表格的结构
        self.create_tabels(TABLES)
        # 3.把数据放进去
        self.load_data()
        # 4.插入数据
        self.insert_data()
        # 5.查询数据
        self.query_data()
        # 6.删除全部表格
        # self.drop_database(DB_NAME)


if __name__ == '__main__':
    with DataBase() as db:
        db.main()
