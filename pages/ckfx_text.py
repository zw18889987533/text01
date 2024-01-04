# -*- coding: utf-8 -*-
# @Time    : 2023/12/7 20:28
# @Author  : harry
# @desc :
import pandas as pd
import streamlit as st
from streamlit_echarts import st_echarts

import os, sys
sys.path.append(os.getcwd())
from info_Stream_text.Base.BaseSettings import DataDIR

st.set_page_config(page_title='抽卡分析图表',
                   layout='wide',
                   initial_sidebar_state='collapsed')


@st.cache_data
def get_data_from_csv(file_path):
    df = pd.read_csv(file_path, encoding='gbk')
    print('get data')
    return df


file_path = st.selectbox('选择需要分析的抽卡信息', [DataDIR + '抽卡记录.csv'], index=0)

df = get_data_from_csv(file_path)
# print(df)

st.sidebar.header('数据过滤')
# platform = st.sidebar.multiselect(
#     '请选择账号',
#     options=df['账号'].unique(),
#     default=df['账号'].unique(),
# )
# genre = st.sidebar.multiselect(
#     '请选择卡池',
#     options=df['卡池'].unique(),
#     default=df['卡池'].unique(),
# )
# df_selection = df.query(
#     '账号 == @platform & 卡池 == @genre'
# )
# 初始化session_state
if 'platform' not in st.session_state:
    st.session_state.platform = df['账号'].unique()

if 'genre' not in st.session_state:
    st.session_state.genre = df['卡池'].unique()

# 处理账号选择
platform = st.sidebar.multiselect(
    '请选择账号',
    options=df['账号'].unique(),
    default=st.session_state.platform,
)
st.session_state.platform = platform

# 重置卡池选择
if 'reset_genre' in st.session_state:
    st.session_state.genre = df['卡池'].unique()
    st.session_state.pop('reset_genre')

# 处理卡池选择
genre = st.sidebar.multiselect(
    '请选择卡池',
    options=df['卡池'].unique(),
    default=st.session_state.genre,
)
st.session_state.genre = genre

# 根据选择的账号和卡池进行筛选
df_selection = df.query('账号 == @platform & 卡池 == @genre')

st.sidebar.header("介绍栏 :taurus:")

st.sidebar.success("总结页签 :aries:")

kaci = df['卡池'].unique()

st.title(f'天地劫卡池抽卡分析表({kaci})')

zcs = df_selection['总次数'].max()
ssr_num = df_selection['SSR数量'].sum()
up_ssr_num = df_selection['up数量'].sum()
sr_num = df_selection['SR数量'].sum()
r_num = df_selection['R数量'].sum()

ssr_Probability = round(ssr_num / zcs, 2)

sr_Probability = round(sr_num / zcs, 2)

r_Probability = round(r_num / zcs, 2)

ssr_up_Probability = round(up_ssr_num / zcs, 2)

first_column, second_column, third_column, fourth_column, fifth_column = st.columns(5)
with first_column:
    st.subheader('总抽数')
    st.subheader(f'{zcs}抽')
with second_column:
    st.subheader('SSR数量')
    st.subheader(f'SSR-{ssr_num}个')
with third_column:
    st.subheader('up数量')
    st.subheader(f'SSR-{up_ssr_num}个')
with fourth_column:
    st.subheader('SSR-率')
    st.subheader(f'{ssr_Probability}%')
with fifth_column:
    st.subheader('upSSR-率')
    st.subheader(f'{ssr_up_Probability}%')

st.markdown('---')

st.subheader('卡池-角色统计', divider='rainbow')

# option_1 = {
#     'tooltip': {
#         'trigger': 'item'
#     },
#     'legend': {
#         'top': '5%',
#         'left': 'center'
#     },
#     'series': [
#         {
#             'name': '抽卡概率',
#             'type': 'pie',
#             'radius': ['40%', '70%'],
#             'avoidLabelOverlap': 'false',
#             'itemStyle': {
#                 'borderRadius': 10,
#                 'borderColor': '#fff',
#                 'borderWidth': 2
#             },
#             'label': {
#                 'show': 'false',
#                 'position': 'center'
#             },
#             'emphasis': {
#                 'label': {
#                     'show': 'true',
#                     'fontSize': 20,
#                     'fontWeight': 'bold'
#                 }
#             },
#             'labelLine': {
#                 'show': 'false'
#             },
#             'data': [
#                 {'value': str(ssr_num), 'name': 'SSR数量'},
#                 {'value': str(sr_num), 'name': 'SR数量'},
#                 {'value': str(r_num), 'name': 'R数量'},
#                 {'value': str(up_ssr_num), 'name': 'UP_数量'},
#             ]
#         }
#     ]
# }
# st_echarts(options=option_1, height="600px", width="100%")


# name_max = df_selection['抽取结果']
# print(name_max)
# 将所有数据整合为一个列表
SSR_items_data = df_selection['抽到的SSR名称']
SSR_items = []
for i in SSR_items_data:
    SSR_items.append(i)
#  处理空列表和转换“”
SSR_items_list = [item for item in eval('[' + ','.join(filter(None, SSR_items)) + ']') if item]

SSR_items_count = {}
for sublist in SSR_items_list:
    for item in sublist:
        if item in SSR_items_count:
            SSR_items_count[item] += 1
        else:
            SSR_items_count[item] = 1

sorted_data = dict(sorted(SSR_items_count.items(), key=lambda item: item[1]))

option = {
    'title': {
        'text': '抽卡角色数量分析'
    },
    'tooltip': {
        'trigger': 'axis',
        'axisPointer': {
            'type': 'shadow'
        }
    },
    'legend': {},
    'grid': {
        'left': '3%',
        'right': '4%',
        'bottom': '3%',
        'containLabel': True
    },
    'xAxis': {
        'type': 'value',
        'boundaryGap': [0, 10]
    },
    'yAxis': {
        'type': 'category',
        'data': list(sorted_data.keys())
    },
    'series': [
        {
            'name': 'SSR英灵数量',
            'type': 'bar',
            'data': list(sorted_data.values())
        }
    ]
}

st_echarts(options=option, height="600px", width="100%")




