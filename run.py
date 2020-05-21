
import datetime
import time
import traceback

import report


report.GROUPS = [
    # '613019056d70a378bf512cbc2cf0bb01128033da092b79fb576a5eb2bc4e7a11',  # 运营日报测试群
    '7e95f199da13a7483da519274be704c8d0e8557bc55323f67441e9e116fe66c6',  # TiDev
    # 'a8d8a969caebddef437c9582f93da87713b9bd4b0fea6da490ed1f0b7e50ae35',  # DDC 大群
]

report.STORAGE_URL = 'http://tiadmin.jinns.top/query/temp<rand>.png'

report.REPORT_URL = 'http://tiadmin.jinns.top/query/ddc_daily_report/'



target = '12:00'
while True:
    now = datetime.datetime.now()
    code = now.strftime('%H:%M')
    print(now, code, target)

    if code == target:
        print('-------------------------------')
    
        try:
            report.make_report()
            report.push_report()
        except Exception as e:
            print('========================')
            traceback.print_exc()
            print('========================')

        time.sleep(60)

    time.sleep(20)


