import asyncio
from gmqtt import Client as MQTTClient
import json
import time
from datetime import datetime

BROKER_HOST = '10.8.6.26'  # 修改为你的 MQTT Broker 地址
BROKER_PORT = 1893  # 端口
MQTT_USERNAME = 'chibi01'  # 账号
MQTT_PASSWORD = 'chibi@!!'  # 密码
CLIENT_PREFIX = 'bms'  # 客户端前缀
CLIENT_COUNT = 600      # 客户端总数
TOPIC = 'mqtt/server/status/up'

clients = []


def generate_client_id(i):
    return f'{CLIENT_PREFIX}-sky{str(i).zfill(3)}'


def generate_client_id_not_prefix(i):
    return f'sky{str(i).zfill(3)}'


def generate_public_message(deviceId):
    payload_dict = {
        "deviceId": deviceId,
        "iccid": "89860858102440451104",
        "locationLat": "32.147557",
        "timestamp": int(time.time() * 1000),
        "imei": "860512075300544",
        "locationLng": "112.213686",
        "data": [
            {
                "happenTime": int(time.time()),
                "content": [
                    "26.313", "22.054", "3293", "3293", "3292", "3293", "3293",
                    "3293", "3292", "3292", "0.111", "55", "55", "100", "0", "4",
                    "200", "27", "27", "27", "3.293", "3.292", "1", "3", "0", "28",
                    "28", "28", "28", "29", "5", "1", "0", "1", "00000000",
                    "v1.0.3-1.0.1", "1.0.0", "0", "0", "0", "0", "0", "0", "0", "0",
                    "0", "0", "0", "0", "0", "13"
                ]
            }
        ]
    }
    return json.dumps(payload_dict)


async def connect_client(i):
    client_id = generate_client_id(i)
    client = MQTTClient(client_id)

    # 设置用户名密码
    client.set_auth_credentials(MQTT_USERNAME, MQTT_PASSWORD)

    # 可选事件回调
    client.on_connect = lambda *args: print(f'[{client_id}] Connected')
    client.on_disconnect = lambda *args: print(f'[{client_id}] Disconnected')

    await client.connect(BROKER_HOST, BROKER_PORT, keepalive=30)
    clients.append(client)


async def sub_send_message(client, i):
    client_id = client._client_id
    payload = generate_public_message(client_id[len(CLIENT_PREFIX) + 1:])
    client.publish(TOPIC, payload, qos=0)
    if i % 100 == 0:
        print(f'Published {i} messages')
    await asyncio.sleep(0.001)  # 小延迟避免阻塞


async def publish_messages():
    for j in range(1):
        start = time.time()
        # 构造所有任务
        tasks = [sub_send_message(client, i) for i, client in enumerate(clients)]
        # 并发执行所有任务
        await asyncio.gather(*tasks)
        end = time.time()
        print(f'Published {CLIENT_COUNT} messages in {end - start:.2f} seconds,CurrentTime: {datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]}')
        if end - start < 1:
            await asyncio.sleep(1 - (end - start))
            print(f'CurrentTime: {datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]}')


async def disconnect_clients():
    for i, client in enumerate(clients):
        await client.disconnect()
        if i % 100 == 0:
            print(f'Disconnected {i} clients')


async def main():
    print(f'=========Connecting {CLIENT_COUNT} clients...')
    await asyncio.gather(*(connect_client(i) for i in range(1, CLIENT_COUNT + 1)))

    print('=========All clients connected. Publishing messages...')
    await publish_messages()

    # 等待一段时间后断开连接
    await asyncio.sleep(60)

    print('=========Messages published. Disconnecting clients...')
    await disconnect_clients()
    print('==========All clients disconnected.')

# 测试函数
def test():
    print(f'CurrentTime: {datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]}')
    start = time.time()
    time.sleep(0.2)
    end = time.time()
    print(f'Time used: {end - start:.2f} seconds,CurrentTime: {datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]}')
    if end - start < 1:
        time.sleep(1 - (end - start))
        print(f'CurrentTime: {datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]}')

if __name__ == '__main__':
    asyncio.run(main())
    #test()
