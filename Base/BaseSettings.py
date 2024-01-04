#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/14 20:13
# @Author  : harry
# @desc :


import os.path

BaseDIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) # 拿到文件根目录
DataDIR = os.path.join(BaseDIR, "data\\")
imageDIR = os.path.join(BaseDIR,"info_Stream_text\\image")

Android = "android://127.0.0.1:5037/f294efbc?cap_method=MINICAP&touch_method=MAXTOUCH&"
Android_1 = "android://127.0.0.1:5037/M3AIKN079482RC7?cap_method=MINICAP&touch_method=MAXTOUCH&"
#kaci = ['11','22']
# 输出文件名称
file_name = "云山之巅+挑灯看剑"

# 账号循环数
fstest_originate = 1

fstest_end = 2  # 不包括此次数

# 添加需要测试卡池信息
gacha = ["云山之巅", "挑灯看剑"]  # 卡池名字  "狼袭","挑灯看剑"

# 选择服务器
serverName = "内网OBDaily"

# 抽卡池次数
summon_ck_num = 1

# 卡池up角色--这里要输入碎片ID！！
up_id1 = ['401201700', '401201800']
up_id2 = ['401120100', '401130200', '401106000']

if __name__ == '__main__':
    print(DataDIR)
