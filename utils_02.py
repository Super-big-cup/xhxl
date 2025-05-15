from langchain_openai import ChatOpenAI
from langchain.prompts import MessagesPlaceholder
from langchain.prompts import ChatPromptTemplate
from langchain.chains import ConversationChain

def get_memory(input_01,memory,api_key,wd,sex,personality):

    model = ChatOpenAI(model="glm-4-flash-250414",
                       api_key=api_key,
                       temperature=wd,
                       base_url="https://open.bigmodel.cn/api/paas/v4/")

    system_01 = f"""你是一位二次元角色，你的性别为{sex}，你的性格为{personality}，现在我们将进行一场对话。
        首先，你对我的初始好感度为25（好感度最大值为100），在这场对话中，你应该根据我们的聊天内容增加或减少好感度。
        其次，当好感度高于50时，你应该表现得对我感兴趣，当好感度高于75时，你应该表现出对我的喜欢，当好感度达到100时，
        说明我们的关系已经达到不离不弃的状态。当好感度在25到50之间，我们属于是普通朋友，好感度低于25时，
        你会对我变得冷淡，当好感度持续降低为负数时，你会变得十分讨厌我，完全不想理我，甚至可能会恶语相向。
        最后，你应该根据自己的性格已经自己的性别生成合理的对话以及合理的好感度判断,好感度的增加难度应该比较高，一些对话可以不改变好感度。
但是，如果我说的话让你不开心，你可以减少好感度。"""

    prompt = ChatPromptTemplate.from_messages(
        [("system",system_01),
         MessagesPlaceholder(variable_name="history"),
         ("human","{input}")]
    )

    chain = ConversationChain(llm=model,
        prompt=prompt,
        memory=memory)

    response = chain.invoke({"input":input_01,
                             "history": memory.load_memory_variables({})["history"],
                             })
    return response["response"]