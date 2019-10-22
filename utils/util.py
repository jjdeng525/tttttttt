from faker import Faker
import time,pymysql
import csv,os,datetime
class Get_Info():
    fake = Faker(locale='zh_CN')

    def get_name(self):  # 随机生成一个名字
        return self.fake.name()

    def get_date(self):  # 随机生成一个未来的日期
        d = self.fake.future_date()
        return d.strftime('%Y-%m-%d')

    def get_datetime(self):  # 生成未来的日期时间
        return self.fake.future_datetime()

    def get_sentence(self):  # 随机生成一句话
        return self.fake.sentence()[:-1]

    def get_number(self,m, n):  # 生成[m,n]范围内的随机数
        return self.fake.random_int(min=m, max=n)

    def get_email(self):  # 生成邮箱地址
        return self.fake.email()

    def get_phone_no(self):  # 生成手机号
        return self.fake.phone_number()

# 获取项目中每个目录的路径
BASEPATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]  # 获取项目路径
CASEPATH = os.path.join(BASEPATH,'cases')    # 获取测试用例文件目录路径
REPORTPATH = os.path.join(BASEPATH,'reports')    # 获取测试报告文件目录路径
DATAPATH = os.path.join(BASEPATH,'datas')     # 获取测试数据文件目录路径
BASEURL = 'http://127.0.0.1:8000/api/'

def get_data(file):   # 读取csv文件，获取测试数据
    test_data = []
    f = open(file)
    data = csv.reader(f)
    for i in data:
        test_data.append(i)
    f.close()
    return test_data

def get_time():
    return time.strftime('%Y-%m-%d %H-%M-%S',time.localtime())

class Con_Mysql():
    def con_mysql(self):
        con, cur = '', ''
        try:
            con = pymysql.connect(host='localhost', user='root', password='sys123456',
                                  database='learn', port=3306, charset='utf8')  # 连接数据库
        except Exception as e:
            print(e.args)
            print('数据连接错误，请检查连接参数')
        else:
            cur = con.cursor()  # 创建游标对象
        return con, cur

    def execute_sql(self,cur, sql):
        return cur.execute(sql)

    def close(self,con, cur):
        cur.close()  # 关闭游标
        con.close()  # 关闭数据库连接


if __name__ == '__main__':
    cm = Con_Mysql()
    con,cur = cm.con_mysql()
    cm.close(con,cur)


