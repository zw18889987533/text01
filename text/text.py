#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/11 20:28
# @Author  : harry
# @desc :
import os

import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
import datetime
import time
import random

# from langchain import OpenAI
# from streamlit_option_menu import option_menu

# st.set_page_config(layout="wide", page_title='数翼 Streamlit Chat 示例')
#
# default_title = '新的对话'
#
# conversations = [{
#     'title': '我是一个哲学爱好者',
#     'messages': [
#         ('user', '我是一个哲学爱好者，想和你聊聊哲学。'),
#         ('assistant', '你好！我很乐意和你聊聊哲学。你想聊什么话题？'),
#         ('user', '我一直在思考自由意志的问题。你认为自由意志是否存在？'),
#     ]
# }, {
#     'title': '我最近在关注强人工智能',
#     'messages': [
#         ('user', '我最近在关注强人工智能（AGI）技术，想和你聊聊'),
#         ('assistant', '你好！我很乐意和你聊聊 AGI 技术。你想聊什么方面？'),
#         ('user', '我一直在思考 AGI 技术的潜在风险。你认为 AGI 技术会对人类造成威胁吗？'),
#     ],
# }]
#
# def chat(user, message):
#     with st.chat_message(user):
#         print(user, ':', message)
#         st.markdown(message)
#
#
# if 'conversations' not in st.session_state:
#     st.session_state.conversations = conversations
# conversations = st.session_state.conversations
#
# #  当前选择的对话
# if 'index' not in st.session_state:
#     st.session_state.index = 0
#
# AVAILABLE_MODELS = [
#     "gpt-4",
#     "gpt-4-0314",
#     "gpt-4-32k",
#     "gpt-4-32k-0314",
#     "gpt-3.5-turbo",
#     "gpt-3.5-turbo-0301",
#     "text-davinci-003",
#     "code-davinci-002",
# ]
#
# with st.sidebar:
#     #st.image('assets/hero.png')
#     st.subheader('', divider='rainbow')
#     st.write('')
#     llm = st.selectbox('选择您的模型', AVAILABLE_MODELS, index=4)
#
#     if st.button('新的对话'):
#         conversations.append({'title': default_title, 'messages': []})
#         st.session_state.index = len(conversations) - 1
#
#     titles = []
#     for idx, conversation in enumerate(conversations):
#         titles.append(conversation['title'])
#
#     option = option_menu(
#         'Conversations',
#         titles,
#         default_index=st.session_state.index
#     )
#
# # get api key from env
# openai_api_key = os.getenv("OPENAI_API_KEY")
# openai = OpenAI(model_name=llm)
#
# st.session_state.messages = conversations[st.session_state.index]['messages']
#
# prompt = st.chat_input("请输入你的问题")
# if prompt:
#     if conversations[st.session_state.index]['title'] == default_title:
#         conversations[st.session_state.index]['title'] = prompt[:12]
#     for user, message in st.session_state.messages:
#         chat(user, message)
#     chat('user', prompt)
#     answer = openai.predict(prompt)
#     st.session_state.messages.append(('user', prompt))
#     st.session_state.messages.append(('assistant', answer))
#     chat('assistant', answer)
# else:
#     for user, message in st.session_state.messages:
#         chat(user, message)

# x = st.slider('x')
# st.write(x, 'is', x * x)  # 滑动框
# # 输入框
# st.text_input("输入框", key="name")
# st.session_state.name
#
# # 选项框
# if st.checkbox('abc'):
#     st.markdown('111')
#
# # 数据选择框
# df = pd.DataFrame({
#     'first': [1, 2, 3, 4],
#     'second': [10, 20, 30, 40]
# })
# option = st.selectbox(
#     'whe?',
#     df['second']
# )
# 'YOU selectcd:', option
#
#
# @st.cache_data
# def get_data_from_csv():
#     df = pd.read_csv('D:\py_caseauto\py_caseauto\caseauto\StreamlitProjects\data\data.csv', encoding='gbk')
#     print('get data')
#     return df
#
#
# df = get_data_from_csv()
#
# option_1 = st.selectbox(
#     '选择',
#     df['卡池'].unique(),  # 去重
# )
# 'YOU selectcd:', option_1
#
# option_2 = st.multiselect(
#     'what',
#     df.columns,
#     ['账号', 'SSR数量', 'SR数量']
# )
# option_2
#
# cs = st.slider('次数', 0, df['总次数'].max(), (0, 10))
#
# R = st.slider('R数量', 0, df['R数量'].max(), (0, 1))
#
# a1 = df[(df['卡池'] == option_1) & (df['总次数'] > cs[0]) & (df['总次数'] < cs[1]) & (df['R数量'] > R[0]) & (df['R数量'] < R[1])][option_2]
# a1
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from airtest.core.android.android import Android

device = Android()
# 获取设备号
currentDevice = device.get_default_device()
print("现在连接的测试设备:", currentDevice)

