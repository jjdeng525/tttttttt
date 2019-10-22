import requests
url = 'http://127.0.0.1:9000/api/login/'
data = {'username':'admin','password':'sys123456'}
rep = requests.post(url=url,data=data)
rep = rep.json()
print(rep)
token = rep['token'] # 获取登录后服务器返回的token值
url = 'http://127.0.0.1:9000/api/card/'
data = {'card_id':'612345678990345','card_user':'张三'}
header = {'Authorization':'Token '+token}
rep = requests.post(url=url,headers=header,data=data)  # 在请求时加上头部，头部中带上token值
rep = rep.json()
print(rep)

