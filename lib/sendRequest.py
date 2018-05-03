# coding=utf-8
import requests
import os

# 从环境变量获取域名
uri = os.environ.get('HOST')


def send_req(method, before, url, params, cookies):
    if method == 'get':
        # 加工请求参数
        if before is not None:
            try:
                url_before = before['url']
                method_before = before['method']
                params_before = before['params']
                after_before = before['after']
                # print(before)
            except Exception as e:
                print(e)

            if method_before == 'get':
                try:
                    r = requests.get('%s%s' % (uri, url_before), params=params_before, cookies=cookies)
                    r_json = r.json()
                    for a in after_before:
                        params[a] = r_json['data'][a]
                    print(params)
                except Exception as e:
                    print(e)
            elif method_before == 'post':
                try:
                    r = requests.post('%s%s' % (uri, url_before), params=params_before, cookies=cookies)
                    r_json = r.json()
                    for a in after_before:
                        params[a] = r_json['data'][a]
                    print(params)
                except Exception as e:
                    print(e)
            else:
                pass

        # 发送请求
        try:
            r = requests.get(url, params=params, cookies=cookies)
            r_json = r.json()
        except Exception as e:
            print(e)
        else:
            return r_json

    elif method == 'post':
        # 加工请求参数
        if before is not None:
            try:
                url_before = before['url']
                method_before = before['method']
                params_before = before['params']
                after_before = before['after']
                # print(before)
            except Exception as e:
                print(e)

            if method_before == 'get':
                try:
                    r = requests.get('%s%s' % (uri, url_before), params=params_before, cookies=cookies)
                    r_json = r.json()
                    for a in after_before:
                        params[a] = r_json['data'][a]
                    print(params)
                except Exception as e:
                    print(e)
            elif method_before == 'post':
                try:
                    r = requests.post('%s%s' % (uri, url_before), params=params_before, cookies=cookies)
                    r_json = r.json()
                    for a in after_before:
                        params[a] = r_json['data'][a]
                    print(params)
                except Exception as e:
                    print(e)
            else:
                pass

        # 发送请求
        try:
            r = requests.post(url, params=params, cookies=cookies)
            r_json = r.json()
        except Exception as e:
            print(e)
        else:
            return r_json
    else:
        pass


if __name__ == '__main__':
    pass