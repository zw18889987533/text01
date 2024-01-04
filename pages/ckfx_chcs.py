#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/21 20:11
# @Author  : harry
# @desc :
import pandas as pd
import streamlit as st
from streamlit_echarts import st_echarts
import os, sys

sys.path.append(os.getcwd())
from info_Stream_text.Base.BaseSettings import DataDIR

st.set_page_config(
    page_title="抽卡分析_出现次数",
    page_icon="👋",
)

st.write("# 其他信息-统计 👋")

st.sidebar.header("介绍栏 :taurus:")

st.sidebar.success("总结页签 :aries:")


@st.cache_data
def get_data_from_csv(file_path):
    df = pd.read_csv(file_path, encoding='gbk')
    print('get data')
    return df


file_path = st.selectbox('选择需要分析的抽卡信息', [DataDIR + '抽卡记录.csv'], index=0)

df = get_data_from_csv(file_path)

st.subheader('SSR出现抽数分布图（十连）', divider='rainbow')

cs_num = df['SSR出货抽数'].value_counts().sort_index()[1:]

# st.bar_chart(cs_num, use_container_width=True)

option = {
    'tooltip': {
        'trigger': 'axis',
        'axisPointer': {
            'type': 'shadow'
        }
    },
    'grid': {
        'left': '3%',
        'right': '4%',
        'bottom': '3%',
        'containLabel': True
    },
    'xAxis': [
        {
            'type': 'category',
            'data': cs_num.index.tolist(),
            'axisTick': {
                'alignWithLabel': True
            }
        }
    ],
    'yAxis': [
        {
            'type': 'value'
        }
    ],
    'series': [
        {
            'name': '出现次数',
            'type': 'bar',
            'barWidth': '60%',
            'data': cs_num.values.tolist()
        }
    ]
}
st_echarts(options=option, height="600px", width="100%")

st.subheader('多黄概率分析', divider='rainbow')

SSR_num = df['SSR数量'].value_counts().sort_index()[1:]

SSR_num_keys_list = SSR_num.keys().to_list()
SSR_num_value_list = SSR_num.tolist()

option_1 = {
    'tooltip': {
        'trigger': 'item'
    },
    'legend': {
        'top': '5%',
        'left': 'center',
        'selectedMode': False
    },
    'series': [
        {
            'name': 'Access From',
            'type': 'pie',
            'radius': ['40%', '70%'],
            'center': ['50%', '70%'],
            'startAngle': 180,
            'label': {
                'show': True,
                'formatter': '{b} ({d}%)'
            },
            'data': [
                {'value': SSR_num_value_list[0], 'name': SSR_num_keys_list[0]},
                {'value': SSR_num_value_list[1], 'name': SSR_num_keys_list[1]},
                {
                    'value': SSR_num_value_list[0] + SSR_num_value_list[1],
                    'itemStyle': {
                        'color': 'none',
                        'decal': {
                            'symbol': 'none'
                        }
                    },
                    'label': {
                        'show': False
                    }
                }
            ]
        }
    ]
}
st_echarts(options=option_1, height="600px", width="100%")
