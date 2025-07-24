from flask import Flask, request, jsonify  
import json
app = Flask(__name__)  
  
@app.route('/dss-accept.jl-iot.net/site-api/hdw-receive/PINSU/api', methods=['GET'])  
def receive_json():  
    #data = request.get_json()  # 获取 POST 请求中的 JSON 数据  
    data = request.args.to_dict()
    print(json.dumps(data, indent=4))
  
    # 构建返回的 JSON 数据，包含 key1 和 key2  
    response_data = {  
       
          
            "limitSpeed":"1024",
            "wifiStatus":"0",
            "wifiStatus5G":"0",
            "ssidPass5G":"你好",
            "ssidPass":"你好",
            "nextReportTime":"10",
            "mainSim":"0",

             #"ssidName":"asdfdgdg",
            # "apEncryptType_5g": "0",
             
       
        
    }  
      
    return jsonify(response_data), 200  
  
if __name__ == '__main__':  
    # 设置端口为 8787，并指定 IP 地址为 192.168.1.100  
    app.run(debug=True, port=8787, host='192.168.1.161')

