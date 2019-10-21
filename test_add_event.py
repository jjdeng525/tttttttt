import unittest,requests
import utils.util as ut
file = ut.DATAPATH+'/add_event.csv'
data = ut.get_test_data(file)  # 读取测试数据
base_url = ut.get_config()['url']  # 获取配置文件中接口地址公共部分
url = base_url+'add_event/'   # 发布会查询接口地址
mark = 0   # 用于标记测试数据
cur,con = ut.con_db(ut.get_config()['db_ip'])  # 连接数据库
logger = ut.log(__name__)
class Test_Add_Event(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_add_event_1(self):
        logger.info('123456')