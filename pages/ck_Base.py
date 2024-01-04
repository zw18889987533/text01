#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/7 20:26
# @Author  : harry
# @desc :
import streamlit as st
from info_Stream_text.Base.BaseSettings import DataDIR
from info_Stream_text.my_utils import file_open_util
from airtest.core.android.android import Android
import subprocess
st.set_page_config(
    page_title="抽卡配置输入",
    page_icon="👋",
)

def get_device_model():
    try:
        result = subprocess.run(['adb', 'shell', 'getprop', 'ro.product.model'], capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout.strip()
        else:
            return "未知设备型号"
    except Exception as e:
        return f"获取设备型号失败：{e}"


def get_battery_status(device_serial):
    try:
        result = subprocess.run(['adb', '-s', device_serial, 'shell', 'dumpsys', 'battery'], capture_output=True, text=True)
        if result.returncode == 0:
            output_lines = result.stdout.strip().split('\n')
            battery_level = None

            for line in output_lines:
                if "level:" in line:
                    battery_level = line.split(':')[1].strip()

            return battery_level if battery_level is not None else "未知电量"
        else:
            return "未知电量"
    except Exception as e:
        return f"获取电池信息失败：{e}"

# 断开连接
def disconnect_device(device):
    try:
        device.disconnect()
        st.success("成功断开设备连接")
    except Exception as e:
        st.error(f"断开设备连接失败：{e}")

kc_book = file_open_util.open_excle_data(DataDIR + '抽卡.xlsx', 0, 3, 12, 1)
yl_book = file_open_util.open_excle_data(DataDIR + '英雄基础信息表.xlsx', 0, 3, 12, 1)

ck_name = []
hero_Preview = []
for kc_book_key in kc_book:
    name = kc_book[kc_book_key]['Name']
    ck_name.append(name)
    # hero = kc_book[kc_book_key['HeroPreview']]
    # hero_Preview.append(hero)

yl_data = {}
for yl_key, yl_value in yl_book.items():
    yl_data[yl_key] = {
        'Descript': yl_value['Descript'],
        'FragmentItem_ID': yl_value['FragmentItem_ID'],
    }

yl_dict = {v['Descript']: str(int(v['FragmentItem_ID'])) for k, v in yl_data.items()}
# print(yl_dict)


ck_name_set = set(ck_name)

st.write("# 配置输入 👋")

st.sidebar.header("介绍栏 :taurus:")

st.sidebar.success("总结页签 :aries:")

col1, col2, col3 = st.columns(3)

col1.write("点击--连接设备--确认PC连接至手机----》》》")
# 创建一个按钮来连接设备
if col2.button("获取设备信息", type="primary"):
    try:
        # 尝试连接设备
        device = Android()
        current_device = device.get_default_device()
        android_device = "android://127.0.0.1:5037/" + current_device + "?cap_method=MINICAP&touch_method=MAXTOUCH&"
        st.success(f"成功连接设备：{android_device}")

        # 获取分辨率
        resolution = device.get_current_resolution()
        st.info(f"设备分辨率：{resolution}")

        #获取设备型号
        device_model = get_device_model()
        st.info(f"设备型号：：{device_model}")

        # 获取电池信息
        battery_level = get_battery_status(current_device)
        st.info(f"设备电量：{battery_level}")

    except Exception as e:
        st.error(f"连接设备失败：{e}，请检查你的设备是否打开开发者模式")



fstest_originate = int(st.text_input('起始抽卡账号数', '1'))
st.write('起始账号:(ww_', fstest_originate, ')')

fstest_end = int(st.text_input('结束抽卡账号数（不包括此数）', '5'))
st.write('结束账号:(ww_', fstest_end - 1, ')')

gacha = st.multiselect(
    '请选择你要抽取的卡池：',
    ck_name,
    ['新手召唤', '狼袭'])
st.write('你选择的卡池:', gacha)

serverName = st.text_input('请输入服务器名称：', '内网OBDaily')
st.write('你选择的服务器为：', serverName)

summon_ck_num = st.text_input('每个卡池抽取次数：', '100')
st.write('次数为：', summon_ck_num)

# 使用multiselect方法
up_id1 = st.multiselect(
    f'请选择卡池--{gacha[0]}--的up英灵：',
    list(yl_dict.keys()),  # 显示字典的键
    ['尉迟良']  # 默认选择项
)
# 输出所选键对应的值
up_id1_values = [yl_dict[key] for key in up_id1]
st.write('你选择的up英灵碎片id:', up_id1_values)

# 使用multiselect方法
up_id2 = st.multiselect(
    f'请选择卡池--{gacha[1]}--的up英灵：',
    list(yl_dict.keys()),  # 显示字典的键
    ['尉迟良']  # 默认选择项
)
# 输出所选键对应的值
up_id2_values = [yl_dict[key] for key in up_id2]
st.write('你选择的up英灵碎片id:', up_id2_values)
