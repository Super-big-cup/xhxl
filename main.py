import streamlit as st
from utils import get_composition

st.header("AI作文生成器 🍃")
with st.sidebar:
    api_key = st.text_input("请输入您的API密钥:",type="password")
    st.markdown("❗你的api密钥不会保存在网页上")
    st.markdown("[获取API密钥](https://www.bigmodel.cn/usercenter/proj-mgmt/apikeys)")
subject = st.text_input("请输入作文主题:")
level = st.text_input("请选择年级(例如：小学、初中、高中):")
number = st.number_input("请输入作文字数:",min_value=1,step=10,value=500)
creativity = st.slider("请选择作文的创造力(数字小说明更严谨，数字大说明更多样)"
                       ,min_value=0.0,max_value=1.0,value=0.2,step=0.1)
button = st.button("生成作文")

if button and not api_key:
    st.error("请输入您的api密钥")
    st.stop()
if button and not subject:
    st.info("请输入作文的主题")
    st.stop()
if button and not level:
    st.info("请填写年级")
    st.stop()
if button and not number >=1:
    st.info("作文字数应该大于等于1")
    st.stop()
if button:
    with st.spinner("AI创作中，请稍等片刻......"):
        title, script = get_composition(api_key,subject,number,level,creativity)
    st.success("作文创作成功")
    st.subheader("标题:")
    st.write(title)
    st.subheader("内容:")
    st.write(script)