#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/7 20:26
# @Author  : harry
# @desc :
import pandas as pd
import streamlit as st
from streamlit_echarts import st_echarts
import os, sys
sys.path.append(os.getcwd())
from Base.BaseSettings import DataDIR

st.set_page_config(
    page_title="抽卡分析",
    page_icon="👋",
)

st.write("# 抽卡总结 👋")

st.sidebar.header("介绍栏 :taurus:")

st.sidebar.success("总结页签 :aries:")


@st.cache_data
def get_data_from_csv(file_path):
    df = pd.read_csv(file_path, encoding='gbk')
    print('get data')
    return df

file_path = st.selectbox('选择需要分析的抽卡信息', [DataDIR + '抽卡记录.csv'],index=0)

df = get_data_from_csv(file_path)

kc_name = df['卡池'].unique()
kc_zh = df['账号'].unique()
kc_times = df['抽取时间']
zcs = df['总次数'].max()
ssr_num = df['SSR数量'].sum()
up_ssr_num = df['up数量'].sum()
sr_num = df['SR数量'].sum()
r_num = df['R数量'].sum()
ssr_ck_num = round((df['SSR出货抽数'].sum()) / df['SSR出货抽数'].astype(bool).sum(axis=0), 2)
ssr_Probability = round(ssr_num / zcs, 2)
sr_Probability = round(sr_num / zcs, 2)
r_Probability = round(r_num / zcs, 2)
ssr_up_Probability = round(up_ssr_num / zcs, 2)
#  输出文本
st.subheader('', divider='rainbow')
st.markdown(
    f"""
    抽卡小助手**👈\\
    抽取的卡池为：（{kc_name}）\\
    抽取账号为：{kc_zh}\\
    抽卡脚本运行时间：{kc_times[0]}\\
    平均SSR抽数：{ssr_ck_num}\\
    总计消耗：{zcs*880}蚀之晶
    ### 抽卡基础信息
    - 总共抽取次数（总次数/账号次数）：{zcs} 次十连\\
    - :rainbow[SSR数量]：{ssr_num}\\
    - :green[SR数量]：{sr_num}\\
    - :blue[R数量]：{r_num}\\
    - :rainbow[UP_SSR数量]：{up_ssr_num}\\
    ### 抽卡概率计算（保留两位）
    - :rainbow[SSR概率]：{ssr_Probability * 100}%\\
    - :green[SR概率]：{sr_Probability * 100}%\\
    - :blue[R概率]：{r_Probability * 100}%\\
    - :rainbow[UP_SSR概率]：{ssr_up_Probability * 100}%\\
"""
)
st.subheader('卡池概率饼图', divider='rainbow')
option = {
    'title': {
        'text': '角色祈愿',
        'subtext': '所有卡池',
        'left': 'center'
    },
    'tooltip': {
        'trigger': 'item'
    },
    'legend': {
        'orient': 'vertical',
        'left': 'left'
    },
    'series': [
        {
            'name': '抽取概率',
            'type': 'pie',
            'radius': '60%',
            'data': [
                {'value': (ssr_Probability, '%'), 'name': 'SSR概率'},
                {'value': sr_Probability, 'name': 'SR概率'},
                {'value': r_Probability, 'name': 'R概率'},
            ],
            'emphasis': {
                'itemStyle': {
                    'shadowBlur': 10,
                    'shadowOffsetX': 0,
                    'shadowColor': 'rgba(0, 0, 0, 0.5)'
                }
            }
        }
    ]
}

st_echarts(options=option, height="600px", width="100%")

st.subheader('原始数据过滤', divider='rainbow')
option_1 = st.selectbox(
    '选择查看的卡池',
    df['卡池'].unique(),  # 去重
)
'你的选择是:', option_1

option_2 = st.multiselect(
    '选择查看项目',
    df.columns,
    ['卡池', 'SSR数量', '十连名单']
)
option_2

cs = st.slider('次数', 0, df['总次数'].max(), (0, 500))
R = st.slider('SSR数量', 0, df['SSR数量'].max(), (0, 1))
a1 = df[(df['卡池'] == option_1) & (df['总次数'] > cs[0]) & (df['总次数'] <= cs[1]) & (df['SSR数量'] > R[0]) & (
            df['SSR数量'] <= R[1])][option_2]
a1
