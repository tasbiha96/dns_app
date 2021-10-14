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

    if hostname == '' or fs_port == '' or as_ip == '' or as_port == '' or num == '' or not num.isdigit():
        return abort(400,'Bad Request')
   
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    US_dict= {
        'hostname': hostname,
        'type': "A"
    }
    us_object = json.dumps(US_dict)
    s.sendto(us_object.encode(), (as_ip,int(as_port)))
    response, clientaddress = s.recvfrom(2048)
    query_response = response.decode()
    query_response = json.loads(query_response)
   # print('Query response is: ',query_response)
    fs_path = 'http://' + query_response["ip"] + ':' + fs_port + '/fibonacci?' + 'number=' + num
    answer=requests.get(fs_path)
    return answer.text

app.run(host='0.0.0.0',
        port=8080,
        debug=True)