import requests
import os
import datetime
import time
import traceback
import re
import uuid


GROUPS = ['613019056d70a378bf512cbc2cf0bb01128033da092b79fb576a5eb2bc4e7a11']

STORAGE_URL = 'http://taojy123.cn:30416/query/temp<rand>.png'

REPORT_URL = 'http://taojy123.cn:30416/query/ddc_daily_report/'
# REPORT_URL = 'http://prod.tflag.cn:32370/query/ddc_daily_report/'


def make_report():
    print('=============== make board =====================')

    # cmd = './phantomjs screenshot.js' # linux
    cmd = f'phantomjs.exe screenshot.js {REPORT_URL} 800 1100 300'  # win
    print(cmd)
    os.system(cmd)
    time.sleep(1)



def push_report():

    storage_url = STORAGE_URL.replace('<rand>', uuid.uuid4().hex)
    print(storage_url)

    files = {
        'file': open('report.png', 'rb')
    }
    r = requests.post(storage_url, files=files)
    assert r.text == 'ok', r.text

    for group in GROUPS:
        url = 'https://oapi.dingtalk.com/robot/send?access_token=' + group
        print(url)
        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": "DDC运营日报通知",
                "text": f'![screenshot]({storage_url})'
            },
        }
        print(data)
        r = requests.post(url, json=data)
        print(r.text)


# while True:
    
#     print('========================')
#     print(datetime.datetime.now())
    
#     try:
#         make_report()
#         push_report()
#     except Exception as e:
#         print('------------------------')
#         traceback.print_exc()
#         print('------------------------')

#     time.sleep(3600)

make_report()
