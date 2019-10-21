import unittest
import requests
import json
import utils.util as ut
file = ut.DATAPATH+'/get_event.csv'
data = ut.get_test_data(file)  # 读取测试数据
base_url = ut.get_config()['url']  # 获取配置文件中接口地址公共部分
url = base_url+'get_event_list/'   # 发布会查询接口地址
mark = 0   # 用于标记测试数据
cur,con = ut.con_db(ut.get_config()['db_ip'])  # 连接数据库
logger = ut.log(__name__)
class Test_Get_Event(unittest.TestCase):
    '''发布会查询接口'''
    def setUp(self):
        self.cur = cur
        testdata = {'eid':data[mark][1],'name':data[mark][2]}
        self.res = requests.get(url,testdata) # 发起get请求
    def tearDown(self):
        global mark
        mark += 1
    def test_event_1(self):
        '''使用id查询发布会成功'''
        r = json.loads(self.res.text)  # 将接口返回数据转为字典
        try:
            logger.info(data[mark][1:])
            self.assertEqual(r['status'],10000)  # 断言
            self.assertEqual(r['data']['name'],ut.get_event_name(self.cur,data[mark][1]))
        except AssertionError as e:
            logger.exception(e)
            raise Exception

    def test_event_2(self):
        '''使用name查询发布会成功'''
        r = json.loads(self.res.text)  # 将接口返回数据转为字典
        try:
            logger.info(data[mark][1:])
            self.assertEqual(r['status'], 10000)  # 断言
            self.assertEqual(r['data'][0]['eid'], ut.get_event_id(self.cur,data[mark][2]))
        except AssertionError as e:
            logger.exception(e)
            raise Exception
    def test_event_3(self):
        '''不传入参数，查询失败'''
        r = json.loads(self.res.text)  # 将接口返回数据转为字典

        try:
            logger.info(data[mark][1:])
            self.assertEqual(r['status'], 10021)  # 断言
        except AssertionError as e:
            logger.exception(e)
            raise Exception
    def test_event_4(self):
        '''使用不存在的发布会id，查询失败'''
        r = json.loads(self.res.text)  # 将接口返回数据转为字典
        try:
            logger.info(data[mark][1:])
            self.assertEqual(r['status'], 10022)  # 断言
        except AssertionError as e:
            logger.exception(e)
            raise Exception
    def test_event_5(self):
        '''使用不存在的发布会名称，查询失败'''
        r = json.loads(self.res.text)  # 将接口返回数据转为字典
        try:
            logger.info(data[mark][1:])
            self.assertEqual(r['status'], 10022)  # 断言
        except AssertionError as e:
            logger.exception(e)
            raise Exception
if __name__ == '__main__':
    unittest.main()
    ut.close_db_con(cur,con)


