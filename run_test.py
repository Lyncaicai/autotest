# coding=utf-8

import os
import requests
import yaml
import base64
import sys
from lib.sendRequest import send_req
from init_db.init_db import init_db

reload(sys)
sys.setdefaultencoding('utf8')

# 从环境变量获取域名/账户/密码
uri = os.environ.get('HOST')
user = os.environ.get('USER')
password = os.environ.get('PASS')

# 指定测试数据
test_data_file = ['system_config', 'fund_manage']

# 进行登录操作
try:
    r = requests.post('%s/bms-pub/user/login' % uri,
                      params={'login_id': user, 'password': base64.b64encode(password)})
    r_json = r.json()
    # print(r_json)
except Exception as e:
    print('\n登录失败: %s' % e)
    os.exit()
else:
    print('\n登录成功.')
    app_token = r_json['data']['app_token']

# 初始化数据库数据
try:
    init_db()
except Exception as e:
    print('初始化失败: %s' % e)
    os.exit()
else:
    print('初始化成功.')

# 循环读取不同模块的测试数据
count_all = 0
count_all_fail = 0
for tdf in test_data_file:
    try:
        f = open('./test_data/%s.yaml' % tdf)
        interfaces = yaml.load(f)
        # print(interfaces)
    except Exception as e:
        print('\n---读取%s失败: %s' % (tdf, e))
        continue
    else:
        if interfaces is not None:
            print('\n---读取%s成功' % tdf)
        else:
            print('\n---读取%s成功: 但文件为空' % tdf)
            continue

    # 循环读取接口及测试数据
    count = 0
    count_fail = 0
    for interface in interfaces:
        count = count + 1
        count_all = count_all + 1
        print('%s:%s %s %s' % (count, interface['method'], interface['url'], interface['params']))
        try:
            # 发送请求
            r_json = send_req(interface['method'], interface['before'], '%s%s' % (uri, interface['url']),
                              interface['params'], cookies={'app_token': app_token})
            # 判断请求结果
            result = ''
            for k, v in interface['expect'].items():
                if r_json[k] == v:
                    result = 'pass'
                else:
                    result = 'fail'
                    count_fail = count_fail + 1
                    count_all_fail = count_all_fail + 1
                    break
            print('expect: %s' % interface['expect'])
            print('response: %s' % r_json)
            print(result)
        except Exception as e:
            print(e)
        else:
            # 增加测试数据留存处理代码
            pass
    print('\n%s模块测试结果如下:\n共运行%s次测试,成功%s次,失败%s次\n' % (tdf, count, count - count_fail, count_fail))

print('-----------------------------------------------')
print('\n本轮测试结果如下:\n共运行%s次测试,成功%s次,失败%s次\n' % (count_all, count_all - count_all_fail, count_all_fail))
