# Ubuntu 18.04
# cd /root/workspace
# git clone https://github.com/taojy123/dingding
# cd dingding/
# chmod a+x phantomjs
# ln -s /root/workspace/dingding/phantomjs /usr/local/bin/phantomjs
# cd /usr/share/fonts/truetype
# mkdir myfonts
# cd myfonts/
# cp /root/workspace/dingding/msyh.ttc ./
# chmod 777 *
# apt install xfonts-utils
# mkfontscale
# mkfontdir
# apt install fontconfig
# fc-cache
# cd workspace/dingding/
# pip install requests
# python3 report.py


import os
import datetime
import time
import traceback
import re
import uuid

import requests


GROUPS = [
    # '613019056d70a378bf512cbc2cf0bb01128033da092b79fb576a5eb2bc4e7a11',
    '7e95f199da13a7483da519274be704c8d0e8557bc55323f67441e9e116fe66c6',
]

# STORAGE_URL = 'http://taojy123.cn:30416/query/temp<rand>.png'
STORAGE_URL = 'http://tiadmin.jinns.top/query/temp<rand>.png'

# REPORT_URL = 'http://taojy123.cn:30416/query/ddc_daily_report/'
REPORT_URL = 'http://tiadmin.jinns.top/query/ddc_daily_report/'


def make_report():
    print('=============== make board =====================')

    # cmd = './phantomjs screenshot.js'
    cmd = f'phantomjs screenshot.js {REPORT_URL} 850 1100 3'
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
                "title": "DDC运营日报推送",
                "text": f'![screenshot]({storage_url})'
            },
        }
        print(data)
        r = requests.post(url, json=data)
        print(r.text)


if __name__ == '__main__':
    make_report()
    push_report()
