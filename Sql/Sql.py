import re
import pymysql


class MySql:
    @staticmethod
    def login():
        connect = pymysql.connect(host="localhost",
                                  user="root",
                                  password="root",
                                  database="password")
        cursor = connect.cursor()
        sql = "select username,password from users"
        cursor.execute(sql)
        users = cursor.fetchall()
        return users

    @staticmethod
    def createTable():
        connect = pymysql.connect(host="localhost",
                                  user="root",
                                  password="root",
                                  db="password")
        c = connect.cursor()
        sql = "show tables"
        c.execute(sql)
        tables = [c.fetchall()]
        table_list = re.findall('(\'.*?\')', str(tables))
        table_list = [re.sub("'", '', each) for each in table_list]
        if "password" in table_list:
            pass
        else:
            sql = "CREATE TABLE `password`  (`id` int(0) NOT NULL AUTO_INCREMENT," \
                  "`condition` varchar(255) NULL," \
                  "`username` varchar(255) NULL," \
                  "`password` varchar(255) NULL," \
                  "PRIMARY KEY (`id`))"
            c.execute(sql)
            connect.commit()
        connect.close()

    @staticmethod
    def getData():
        connect = pymysql.connect(host="localhost",
                                  user="root",
                                  password="root",
                                  db="password")
        c = connect.cursor()
        sql = 'select * from password'
        c.execute(sql)
        data = c.fetchall()
        data_list = []
        for row in data:
            num = row[0]
            condition = row[1]
            username = row[2]
            password = row[3]
            temp = [num, condition, username, password]
            data_list.append(temp)
        return list(data_list)
        connect.close()

    @staticmethod
    def addDef(condition, username, password):
        connect = pymysql.connect(host="localhost",
                                  user="root",
                                  password="root",
                                  db="password")
        c = connect.cursor()
        sql = "insert into password (`condition`, `username`, `password`) values ('%s','%s','%s')" % (
            condition, username, password)
        c.execute(sql)
        connect.commit()
        connect.close()

    @staticmethod
    def delDef(num):
        connect = pymysql.connect(host="localhost",
                                  user="root",
                                  password="root",
                                  db="password")
        c = connect.cursor()
        sql = "delete from password where id = %s" % num
        c.execute(sql)
        connect.commit()
        connect.close()
