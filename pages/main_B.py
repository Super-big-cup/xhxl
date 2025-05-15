import streamlit as st
from utils_02 import get_memory
from langchain.memory import ConversationBufferMemory

custom_ai_avatar = "./01.jpg"
custom_ai_avatar_02 = "./02.jpg"

st.header("二次元角色聊天模拟器 💡")

with st.expander("性别和性格"):
    sex = st.radio("请选择角色性别:",["男","女"],index=None)
    xg = st.text_input("请输入性格(例如:活泼可爱、开朗乐观等)")

with st.sidebar:
    api_key = st.text_input("请输入您的API密钥:",type="password")
    st.markdown("⚠️ 你的api密钥不会保存在网页上")
    creativity = st.slider("请选择聊天的创造力(数字小说明更严谨，数字大说明更多样)"
              ,min_value=0.0,max_value=1.0,value=0.2,step=0.1)
    st.markdown("[获取API密钥](https://www.bigmodel.cn/usercenter/proj-mgmt/apikeys)")
    st.divider()
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(return_messages=True)
if "messages" not in st.session_state:
    st.session_state.messages = [{"role":"ai","content":"你好~"}]

for message in st.session_state.messages:
    # st.chat_message("ai").write(message["content"])
    if message["role"] == "ai" and sex =="女":
        st.chat_message("ai", avatar=custom_ai_avatar).write(message["content"])
    elif message["role"] == "ai" and sex =="男":
        st.chat_message("ai", avatar=custom_ai_avatar_02).write(message["content"])
    else:
        st.chat_message("human").write(message["content"])

input_01 = st.chat_input("让我们开始聊天吧~")

if input_01:
    if not api_key:
        st.error("您需要先输入密钥后才能开始使用")
        st.stop()
    if not sex:
        st.info("选择一个角色性别吧~")
        st.stop()
    if not xg:
        st.info("输入一个角色性格吧~")
        st.stop()
    st.session_state.messages.append({"role":"human","content":input_01})
    st.chat_message("human").write(input_01)

    with st.spinner("Ai思考中......"):
        response = get_memory(input_01,st.session_state.memory,api_key,creativity,sex,xg)

        # msg = {"role": "ai", "content": response}
        # st.session_state.messages.append(msg)
        # st.chat_message("ai").write(response)

        msg = {"role": "ai", "content": response}
        st.session_state.messages.append(msg)
        if sex == "女":
            st.chat_message("ai", avatar=custom_ai_avatar).write(response)
        elif sex == "男":
            st.chat_message("ai", avatar=custom_ai_avatar_02).write(response)