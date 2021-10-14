import requests, json,socket
from flask import Flask,request,abort

app = Flask(__name__)

@app.route('/fibonacci')
def US_driver_prog():
    hostname = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    num = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')
    #print(hostname,fs_port,num,as_ip,as_port)

    if hostname is None or fs_port is None or as_ip is None or as_port is None or num is None:
        abort(400)
   
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    US_dict= {
        'NAME': hostname,
        'TYPE': "A"
    }
    us_object = json.dumps(US_dict)
    s.sendto(us_object.encode(), (as_ip,int(as_port)))
    print('Response Sent')
    response, clientaddress = s.recvfrom(2048)
    print('Response received:',response)
    query_response = response.decode()
    query_response = json.loads(query_response)
   # print('Query response is: ',query_response)
    fs_path = "http://" + query_response["VALUE"] + ":" + fs_port + "/fibonacci?" + "number=" + num
    answer=requests.get(fs_path)
    return answer.text

app.run(host='0.0.0.0',
        port=8080,
        debug=True)