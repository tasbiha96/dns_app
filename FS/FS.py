import requests, json,socket
from flask import Flask,request

app = Flask(__name__)

@app.route('/fibonacci')
def driver_program():
    num = int(request.args.get('number'))
    result = Fibonacci(num)
    return str(result)

def Fibonacci(n):
   
    if n == 0:
        return 0
 
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

@app.route('/register')
def RegisterFS():
    hostname = request.args.get('hostname') 
    ip = request.args.get('ip')
    as_ip = request.args.get('as_ip')
    as_port =request.args.get('as_port') 

    out_dict = {
        "TYPE": "A",
        "NAME": hostname,
        "VALUE":ip,
        "TTL": 10        
    }
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    fs_object = json.dumps(out_dict)
    s.sendto(fs_object.encode(),(as_ip,int(as_port)))
    return_code , clientaddress = s.recvfrom(2048)
    code = return_code.decode('utf-8')       # recvfrom returns result of type byte. Hence decoding required
    if code == '201':
        return str(201)
    else:
        return ('Error')

app.run(host='0.0.0.0',
        port=9090,
        debug=True)