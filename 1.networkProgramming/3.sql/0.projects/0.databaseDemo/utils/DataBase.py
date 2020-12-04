from __future__ import print_function
import os
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
import re
from .configs import DB_NAME, TABLES
import random
import pymysql

PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
"""
增删改 要commit才会有生效
"""


class DataBase():
    def __init__(self, user_name="root", password="gmwang"):
        self._user_name = user_name
        self._password = password
        self._cursor = None
        self._cnx = None
        self.data_dir = os.path.join(PROJECT_PATH, 'data')
        self.file_list = [
            "load_employees.dump", "load_titles.dump", "load_departments.dump",
            "load_salaries.dump", "load_dept_emp.dump", "load_dept_manager.dump"
        ]
        self.tables = [re.findall(r'load_(.+?)\.dump', filei)[0] for filei in self.file_list]

    def __enter__(self):
        self._cnx = mysql.connector.connect(
            host='127.0.0.1',
            database=None,
            user=self._user_name,
            password=self._password
        )
        # 1.普通cursor 获取到的数据是列表
        self._cursor = self._cnx.cursor()
        # 2.dict cursor 获取字典数据
        # self._cursor = self._cnx.cursor(dictionary=True)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._cursor.close()
        self._cnx.close()

    def select_database(self, db_name):
        try:
            self._cursor.execute("USE {}".format(db_name))
        except mysql.connector.Error as err:
            print("Database {} does not exists.".format(DB_NAME))
            if err.errno == errorcode.ER_BAD_DB_ERROR:
                self.create_database()
                print("Database {} created successfully.".format(DB_NAME))
                self._cnx.database = DB_NAME
            else:
                print(err)
                exit(1)

    def create_database(self):
        try:
            self._cursor.execute(
                "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
        except mysql.connector.Error as err:
            print("Failed creating database: {}".format(err))
            exit(1)

    def create_tabels(self, tables):
        for table_name in tables:
            table_description = TABLES[table_name]
            try:
                print("Creating table {}: ".format(table_name), end='')
                self._cursor.execute(table_description)
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
                self._cursor.execute(content)
        self._cnx.commit()

    def insert_data(self):
        for i in range(500000, 1400000):
            try:
                # 1.增加员工信息
                # tomorrow = datetime.now().date() + timedelta(days=1)
                # data_employee = ('Geert{}'.format(i), 'Vanderkelen{}'.format(i), tomorrow, 'M', date(1977, 6, 14))
                # add_employee = ("INSERT INTO employees "
                #                 "(first_name, last_name, hire_date, gender, birth_date) "
                #                 "VALUES (%s, %s, %s, %s, %s)")
                # self._cursor.execute(add_employee, data_employee)

                # 2. 增加dept信息
                data_dept_emp = (i, 'd00{}'.format(random.randint(3, 7)), date(1977, 6, 14), date(1977, 6, 18))
                add_dept_emp = ("INSERT INTO dept_emp "
                                "(emp_no, dept_no, from_date, to_date) "
                                "VALUES (%s, %s, %s, %s)")
                self._cursor.execute(add_dept_emp, data_dept_emp)
                # 2.修改员工
                # emp_no = self._cursor.lastrowid
                # print("emp_no = cursor.lastrowid  ->".format(emp_no))
                # add_salary = ("INSERT INTO salaries "
                #               "(emp_no, salary, from_date, to_date) "
                #               "VALUES (%(emp_no)s, %(salary)s, %(from_date)s, %(to_date)s)")
                # data_salary = {
                #     'emp_no': emp_no,
                #     'salary': 50000,
                #     'from_date': tomorrow,
                #     'to_date': date(9999, 1, 1),
                # }
                # self._cursor.execute(add_salary, data_salary)
                # 3.确保数据已提交
                self._cnx.commit()
            except Exception as err:
                print(err)
                # 回滚
                self._cnx.rollback()

    def update_data(self):
        """
        事务！ commit 是保证事务安全的措施 ，insert,delete,update 都需要commit，这样能保证事务性！
        :return:
        """
        # 1.修改员工工资,但是这个是要先查询再更改，所以要进行事务加锁
        query = "SELECT * from salaries where emp_no=10011 for update"
        self._cursor.execute(query)
        emp_no, salary, _, _ = self._cursor.fetchone()
        add_salary = ("UPDATE salaries SET "
                      "salary =%(salary)s WHERE emp_no=%(emp_no)s")
        data_salary = {
            'emp_no': emp_no,
            'salary': salary + 1,
        }
        self._cursor.execute(add_salary, data_salary)
        self._cnx.commit()

    def query_data(self):
        query = ("SELECT first_name, last_name, hire_date FROM employees "
                 "WHERE hire_date BETWEEN %s AND %s")
        hire_start = date(1800, 1, 1)
        hire_end = date(1999, 12, 31)
        self._cursor.execute(query, (hire_start, hire_end))

        # 1.方法1： fetch 都是iterator，只能fetch一次
        # data=self._cursor.fetchone()
        # data=self._cursor.fetchmany(10)
        # data = self._cursor.fetchall()

        # 2.方法2： 直接用其iterator属性获取：
        for (first_name, last_name, hire_date) in self._cursor:
            print("{}, {} was hired on {:%d %b %Y}".format(last_name, first_name, hire_date))

    def drop_database(self, db_name):
        query = "drop database {};".format(db_name)
        self._cursor.execute(query)
        self._cnx.commit()

    def main(self):
        # 1.选择某一个数据库（如果不存在则创建）
        self.select_database(DB_NAME)
        # 2.创建各表格的结构
        # self.create_tabels(TABLES)
        # 3.把数据放进去
        # self.load_data()
        # 4.插入数据
        # self.insert_data()
        # 5.查询数据
        self.query_data()
        # 6.删除全部表格
        # self.drop_database(DB_NAME)


if __name__ == '__main__':
    with DataBase() as db:
        db.main()
