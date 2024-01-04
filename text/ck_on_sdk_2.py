# -*- encoding=utf8 -*-
__author__ = "zhangwang"
from info_Stream_text.Base.BaseSettings import Android, DataDIR, gacha, serverName, up_id1, up_id2, \
    fstest_end, file_name, summon_ck_num
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from collections import Counter
import csv

from info_Stream_text.pages.ck_Base import fstest_originate
from info_Stream_text.my_utils import file_open_util

if not cli_setup():
    auto_setup(__file__, logdir=True,devices=[Android, ])

# script content
print("start...")

# poco("Detail").wait_for_appearance()


yl_book = file_open_util.open_excle_data(DataDIR + '英雄基础信息表.xlsx', 0, 3, 12, 1)
name_list = []
sp_list = []

for key in yl_book:
    name = yl_book[key]['Descript']
    name_list.append(name)
    sp = yl_book[key]['FragmentItem_ID']
    sp_list.append(str(sp).replace('.0', ''))

sp_list1 = [str(key) for key in sp_list]
id_name = {k: v for k, v in zip(sp_list1, name_list)}

# 处理公告
try:
    Total_munber = 0  # 总次数
    deta = []  # 存放最终数据
    #new_ID = "fstest179@123.com"
    for i in range(fstest_originate, fstest_end):
        try:
            testApp = "com.zlongame.tdj"

            start_app(testApp)
            sleep(10)

            from poco.drivers.unity3d import UnityPoco
            poco = UnityPoco()

            from poco.drivers.android.uiautomation import AndroidUiautomationPoco
            Android_poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

            ID_munber = 0  # 账号抽卡次数
            for j in range(10):
                if poco(text="游戏公告").exists():
                    poco("CloseButton").click()
                    sleep(2)
                else:
                    break
            sdk_ID = 'ww_' + str(i)
            sdk_password = "111111"
            sdk_text = poco("UserNameInputField").child("Text")
            sleep(5)
            if not sdk_text.get_text() == sdk_ID:
                poco("UserNameInputField").click()
                sleep(1)
                poco("UserNameInputField").set_text(sdk_ID)
                poco(texture="LOGO_OB1").click()
                #poco(texture="Font_GameEntry").click()
            else:
                pass
                #poco(texture="Font_GameEntry")


            for j in range(10):
                if poco(text="游戏公告").exists():
                    poco("CloseButton").click()
                    sleep(2)
                else:
                    break

            # 选择服务器
            ServerNameUI = poco("ServerNameText")
            poco("ClickText").wait()
            if not ServerNameUI.get_text() == serverName:
                poco("ServerNameText").click([0.5, 0.5])
                ServerList = poco("ServerListScrollView")
                ServerList.wait_for_appearance()
                ServerName = ServerList.offspring("ServerNameText")
                while ServerNameUI != True:
                    try:
                        for Name_Ser in ServerName:
                            if Name_Ser.get_text() == serverName:
                                ServerList.focus([0.5, 0.5]).drag_to(ServerList.focus([0.5, 0.2]))
                                Name_Ser.click()
                    except Exception:
                        break
            poco(texture="Font_GameEntry").click([0.5, 0.5])
            sleep(10)

            # 处理签到
            for j in range(10):
                if poco(texture="Pattern_Effect").exists():
                    poco(texture="Pattern_Effect").click()
                    sleep(2)
                    for CloseButton in range(10):
                        if poco("CloseButton").exists():
                            poco("CloseButton").click()
                    sleep(1)
                else:
                    break

            # 处理分享
            for j in range(10):
                if poco("RightButton").exists():
                    poco("RightButton").click()
                    sleep(1)
                else:
                    break

            sleep(1)

            for j in range(10):
                if poco(texture="Pattern_Effect").exists():
                    poco(texture="Pattern_Effect").click()
                    sleep(1)
                else:
                    break

            sleep(1)

            # 处理回归
            for j in range(10):
                if poco(text="免费").exists():
                    poco("CloseButton").click()
                    sleep(1)
                else:
                    break
            sleep(1)

            poco(text="召唤").wait_for_appearance()
            poco(texture="Icon_Summon").click()

            poco("FreeText").wait_for_appearance()
            # gachaList = poco("EnhanceScrollview")

            for kc_name in gacha:
                gacha_num = 0
                poco(texture="Button_Back").click()
                poco(text="召唤").click()
                while True:
                    if poco("LightNameText").get_text() == kc_name:
                        poco("LightNameText").click()
                        break
                    else:
                        poco("LightNameText").focus([0.5, 0.5]).drag_to(poco("LightNameText").focus([0.5, 5.0]))
                        sleep(1)
                sleep(1)

                # Card_num = 0 #卡池抽取次数
                summon_one = poco(text="召唤一次")
                summon_ten = poco(text="召唤十次")
                summon_ten.wait_for_appearance()


                #  计算SSR出货数
                kc_SSR_num = 0
                kc_count = 0

                summon_num = summon_ck_num

                while summon_num > 0:
                    ck_id_list = []
                    ck_num_list = []
                    summon_ten.click()
                    now = int(round(time.time() * 1000))
                    CK_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now / 1000))
                    #CK_time = time.strftime("%Y_%m_%d_%H_%M_%S")  # 抽卡时间
                    sleep(2)
                    poco(texture="Xingzhen").scroll(direction='vertical', percent=1.0, duration=1.0)
                    poco("ArrowImage").click()
                    sleep(5)
                    poco(text="确认").wait_for_appearance()
                    for j in range(2, 12):
                        if j == 0 or j == 1:
                            continue
                        k = 13 - j
                        zhuangbeiqianzhui = "item_"
                        zhuangbeiweizhi = zhuangbeiqianzhui + str(k)
                        id = poco("Detail").child("Group").child(name=zhuangbeiweizhi).child("PieceIcon").attr(
                            'texture')  # 获得DI
                        ck_id_list.append(id.replace('I', ''))
                        num = poco("Detail").child("Group").child(name=zhuangbeiweizhi).child("PieceIcon").child(
                            "CountText").get_text()  # 获得碎片数量
                        ck_num_list.append(num)

                        Total_munber += 1
                        ID_munber += 1
                        gacha_num += 1
                        while True:
                            if poco(texture="Pattern_Effect").exists():
                                poco(texture="Pattern_Effect").click()
                            else:
                                break
                        # print(ck_id_list)
                        # print(ck_num_list)
                        # 转换为人名

                    poco(text="确认").click()

                    txt = poco("ChanceAddTxt").get_text()
                    probability = "2.0%" + txt
                    rarity = {'5': 'R', '20': 'SR', '60': 'SSR'}
                    ck_rarity_list = [rarity[item] for item in ck_num_list]
                    counts = Counter(ck_rarity_list)
                    R_num = []
                    SR_num = []
                    SSR_num = []
                    R_num = counts['R']
                    SR_num = counts['SR']
                    SSR_num = counts['SSR']
                    # 抽取结果
                    # ck_jg = [ck_id_list,ck_num_list,ck_rarity_list]
                    # print(ck_id_list)
                    ck_name_list = [id_name[i] for i in ck_id_list if i in id_name.keys()]

                    #ck_ssr_num = 0
                    ck_name_jg = [ck_name_list, ck_num_list, ck_rarity_list]
                    # print(ck_name_jg)
                    # 抽到的SSR分类
                    id_result = {'R': [], 'SR': [], 'SSR': []}

                    [id_result['R'].append(ck_id_list[i]) if ck_rarity_list[i] == 'R' else id_result['SR'].append(
                        ck_id_list[i]) if ck_rarity_list[i] == 'SR' else id_result['SSR'].append(ck_id_list[i]) for i in
                     range(len(ck_id_list))]

                    if not id_result['R']:
                        id_result['R'] = ['0']

                    if not id_result['SR']:
                        id_result['SR'] = ['0']

                    if not id_result['SSR']:
                        id_result['SSR'] = ['0']

                    result_name_list = {k: [id_name[i] for i in v if i in id_name] for k, v in id_result.items()}
                    # print(result_name_list)
                    # 输出ID+稀有度
                    SSR_name_list = result_name_list['SSR']
                    #这里要输入碎片ID！！

                    # up_id3 = ['401121800', '401111000']
                    # up英灵
                    up_count = 0
                    if kc_name == gacha[0]:
                        for j in up_id1:
                            for item in id_result['SSR']:
                                if item == j:
                                    up_count += 1

                    elif kc_name == gacha[1]:
                        for j in up_id2:
                            for item in id_result['SSR']:
                                if item == j:
                                    up_count += 1


                    # else:
                    #     for j in up_id3:
                    #         for item in id_result['SSR']:
                    #             if item == j:
                    #                 up_count += 1
                    #  判断抽到SSR时是多少抽
                    if up_count != 0:
                        kc_SSR_num += 10
                        kc_count = kc_SSR_num
                        kc_SSR_num = 0
                    else:
                        kc_SSR_num += 10
                        kc_count = 0

                    #判断是否歪了
                    up_w_l = ''
                    if SSR_num == 0:
                        up_w = SSR_num - up_count
                        if up_w == 0:
                            up_w_l = '未歪'

                        else:
                            up_w_l = '歪'

                    else:
                        pass


                    data_list = []
                    data_list = [
                        Total_munber, #  '总次数'
                        sdk_ID,  #  '账号'
                        kc_name, #'卡池'
                        ID_munber,
                        gacha_num,
                        CK_time,
                        probability,
                        result_name_list,
                        SSR_name_list,
                        kc_count,
                        SSR_num,
                        SR_num,
                        R_num,
                        up_count,
                        up_w_l,
                        ck_name_list,
                        ck_name_jg,
                    ]
                    # data_list.append(Total_munber)

                    deta.append(data_list)

                    # print(data_list)

                    summon_num -= 1

            stop_app(testApp)
            sleep(5)
            print("输出完成")
        except Exception as r:
            print('网络连接错误！' % r)

        finally:
            stop_app(testApp)
            sleep(30)
            continue
except Exception as r:
    print('未知错误 %s' % r)

finally:
    with open(file_name +'_卡池记录.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['总次数',
                         '账号',
                         '卡池',
                         '当前账号抽取次数',
                         '当前卡池抽取次数',
                         '抽取时间',
                         '绝品概率',
                         '抽到的SSR分类',
                         '抽到的SSR名称',
                         'SSR出货抽数',
                         'SSR数量',
                         'SR数量',
                         'R数量',
                         'up数量',
                         '是否歪'
                         '十连名单',
                         '抽取结果',
                         ])
        for row in deta:
            writer.writerow(row)
        print("over!")
# riqi = time.strftime("%Y-%m-%d %H:%M:%S")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
