import requests

# HTTPS URL
url = 'https://www.yingmakj.com/mini/device/test/cmd/861337071182863?cmd=24'

# 发送GET请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 打印网页内容
    print(response.text)
else:
    print('请求失败，状态码：', response.status_code)
    print(response.status_code)