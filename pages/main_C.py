import streamlit as st
from util_03 import get_img

st.header("图片生成 🎈")

with st.sidebar:
    api_key = st.text_input("请输入您的API密钥:",type="password")
    st.markdown("⚠️ 你的api密钥不会保存在网页上")
    st.markdown("[获取API密钥](https://www.bigmodel.cn/usercenter/proj-mgmt/apikeys)")
    st.divider()

prompt = st.text_input("请输入关键词生成图片")

button = st.button("生成图片")

if button and not api_key:
    st.error("请输入API密钥")
    st.stop()
if button and not prompt:
    st.info("请输入关键词~")
    st.stop()

if button:
    with st.spinner("图片生成中，请稍后......"):
        response = get_img(prompt, api_key)

        st.image(response,caption="AI生成图片",width=400)