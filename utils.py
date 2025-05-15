from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate


def get_composition(api_key,subject,word_count,age,creativity):
    title_prompt = ChatPromptTemplate.from_messages([
        ("human","请为{subject}这个主题的作文想一个吸引人的标题")
    ])
    script_prompt = ChatPromptTemplate.from_messages([
        ("human",
         """你是一位优秀的作家，现在你需要根据以下标题和内容，写出一篇优秀的作文。
         作文标题：{title}，作文字数：{word_number},作文应该符合{level}水平。
         要求作文的内容必须完整，能够清晰地表达主题和观点，各部分之间要有逻辑上的连贯性。
         作文中应使用正确的词汇和语法，语句通顺流畅，能够恰当运用修辞手法和句式结构。作文的结构应合理，
         有明确的开头、中间和结尾，段落之间要有合适的过渡和衔接。确保作文字数误差在10个字以内。""")
    ])

    model = ChatOpenAI(model="glm-4-flash-250414",
                       api_key=api_key,
                       base_url="https://open.bigmodel.cn/api/paas/v4/",
                       temperature=creativity)

    title_chain = title_prompt | model
    script_chain = script_prompt | model

    title = title_chain.invoke({"subject":subject}).content
    script = script_chain.invoke({"title":title,"word_number":word_count,"level":age}).content

    return title,script