from flask import Flask, request, jsonify  
import json
app = Flask(__name__)  
  
@app.route('/push/tianruan', methods=['POST'])  
def receive_json():  
    data = request.get_json()  # 获取 POST 请求中的 JSON 数据  
    print(json.dumps(data, indent=4))
  
    # 构建返回的 JSON 数据，包含 key1 和 key2  
    response_data = {  
        'data':{
          
             #"Wifi_filter_type":"2",
             #"Blacklist":"33:06:B0:CA:33:CD",
             "lockExtSim":"0",
            # "apEncryptType_5g": "0",
             
       
        }
    }  
      
    return jsonify(response_data), 200  
  
if __name__ == '__main__':  
    # 设置端口为 8787，并指定 IP 地址为 192.168.1.100  
    app.run(debug=True, port=8787, host='192.168.1.159')

