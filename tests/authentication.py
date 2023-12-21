import json
import os

import requests
from dotenv import load_dotenv

# 加载.env文件
load_dotenv()

# 从环境变量获取凭证
username = os.getenv('API_USERNAME', 'default_username')
password = os.getenv('API_PASSWORD', 'default_password')
# 设置请求头
headers = {'Content-Type': 'application/json'}

# 请求体数据
data = {
    "username": username,
    "password": password
}

try:
    # 向API发送POST请求
    response = requests.post('http://localhost:8500/login', headers=headers, data=json.dumps(data))

    # 检查请求是否成功
    if response.status_code == 200:
        token = response.json().get('token')
        print("Token:", token)
    else:
        # 处理未成功的请求
        print("认证失败。状态码:", response.status_code, "响应文本:", response.text)

except requests.RequestException as e:
    # 处理请求过程中出现的任何异常
    print("发生错误:", e)
