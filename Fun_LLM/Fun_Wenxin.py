import requests
import json

#利用文心一言生成结论

API_KEY = "yMGCQEjqPGAyCFWsCJgHUuvf"
SECRET_KEY = "CDp9vYty7Sijgk1M6X5alsmvgrBBuXxe"
def fun_Wenxin(question):
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/yi_34b_chat?access_token=" + get_access_token()

    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": "{}".format(question)
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    response_data = response.json()  # 将响应转换为字典格式
    result = response_data.get("result")  # 提取result部分

    answer = result  # 将result赋值给channel_2_a4

    # print(answer)
    print(response)

    return answer

def get_access_token():
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


# if __name__ == '__main__':
#     question = "假设你是个数据分析师，请根据我给出的信息，给出对应电玩猩特定店铺的优化建议，我的问题是：盈客宝渠道套餐销售量较低，给出优化建议"
#     fun_Wenxin(question)
