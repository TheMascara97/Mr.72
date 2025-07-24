from flask import Flask, request, jsonify  
import json
app = Flask(__name__)  
  
@app.route('/test', methods=['POST'])  
def receive_json():  
    data = request.get_json()  # 获取 POST 请求中的 JSON 数据  
    print(json.dumps(data, indent=4))
  
    # 构建返回的 JSON 数据，包含 key1 和 key2  
    response_data = {  
    #   "defaultSim":"2"
    #   "nextReportTime":"15"
    #   "nextReportTime":"15"
    # "forceReset":"0"
    }  
      
    return jsonify(response_data), 200  
  
if __name__ == '__main__':  
    # 设置端口为 8787，并指定 IP 地址为 192.168.1.100  
    app.run(debug=True, port=6666, host='192.168.42.159')

