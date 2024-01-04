#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/30 22:47
# @Author  : harry
# @desc :此页面为，测试工具主界面
import os

import streamlit as st
import datetime
import json
st.set_page_config(
    page_title='测试工具',
    page_icon="👋",
)

st.write("# 自用-测试进度管理 ❥")

st.sidebar.header("介绍栏 :taurus:")

st.sidebar.success("总结页签 :aries:")

# 读取用户选择的结束时间，如果文件不存在则设置默认值
try:
    with open("data_json/endtime_user_settings.json", "r") as file:
        end_user_settings = json.load(file)
    with open("data_json/start_time_user_settings.json", "r") as file:
        start_user_settings = json.load(file)
except FileNotFoundError:
    end_user_settings = {"end_time": "2024-01-17"}
    start_user_settings = {"start_time": "2023-12-30"}


# 输入开始时间
start_time = st.date_input("版本开始时间", datetime.datetime.strptime(start_user_settings["start_time"], "%Y-%m-%d").date())

if st.button("确认版本开始时间"):
    start_user_settings["start_time"] = start_time.strftime("%Y-%m-%d")
    with open("data_json/start_time_user_settings.json", "w") as file:
        json.dump(start_user_settings, file)

# 输入结束时间
end_time = st.date_input("版本结束时间", datetime.datetime.strptime(end_user_settings["end_time"], "%Y-%m-%d").date())

# 保存用户选择的结束时间
if st.button("确认版本结束时间"):
    end_user_settings["end_time"] = end_time.strftime("%Y-%m-%d")
    with open("data_json/endtime_user_settings.json", "w") as file:
        json.dump(end_user_settings, file)



# 计算剩余时间和进度
current_time = datetime.datetime.now().date()
remaining_time = end_time - current_time
progress_percentage = int(((current_time - start_time).days / (end_time - start_time).days) * 100)

# 显示结果
st.write(f"当前时间：{current_time}")
st.write(f"剩余时间：{remaining_time.days} 天")

st.subheader('', divider='rainbow')
# 创建一个输入框
user_input = st.text_input("请输入内容：")

# 创建一个按钮
if st.button("确认输入内容"):
    # 读取已有的 JSON 数据
    try:
        with open("data_json/output.json", "r") as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = {}

    # 将新的输入内容追加到 JSON 数据中
    data["user_input"] = data.get("user_input", []) + [user_input]

    # 保存输入的内容到 JSON 文件
    with open("data_json/output.json", "w") as json_file:
        json.dump(data, json_file)

# 创建一个按钮 - 删除 JSON 内容
if st.button("删除 JSON 内容"):
    # 删除 JSON 文件
    try:
        os.remove("data_json/output.json")
        st.success("成功删除数据")
    except FileNotFoundError:
        st.warning("JSON 文件不存在")


# 显示 JSON 文件中的所有内容
with st.container():
    try:
        with open("data_json/output.json", "r") as json_file:
            saved_data = json.load(json_file)
            st.write("从 JSON 文件中读取的内容:")
            for item in saved_data.get("user_input", []):
                st.write(item)
    except FileNotFoundError:
        st.warning("JSON 文件不存在")

# 显示结果（在这里显示，也可以在容器外显示）
# 这里只是为了演示效果，实际应用中可以根据需要在容器内外显示
st.write("这是容器外的内容")