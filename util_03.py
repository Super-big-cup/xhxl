from zhipuai import ZhipuAI

def get_img(prompt:str,api_key:str,):
    client = ZhipuAI(api_key=api_key)

    response = client.images.generations(
        model="cogview-3-flash",
        prompt=f"根据{prompt}这些提示词生成一张符合人类逻辑的图片",
    )

    return response.data[0].url