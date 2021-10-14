import requests,socket
import json

localPort   = 53533

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', localPort))

while True:
    print ('Waiting to receive input***********************')
    message, clientaddress = s.recvfrom(2048)
    
    message = message.decode()
    message = json.loads(message)
    #print('Load:',message)

    if len(message) == 2:                            #DNS Query
        with open("out.json", "r") as outfile:
            dictionary = json.load(outfile)
        DNS_response = dictionary[message["NAME"]]
        dns_object = json.dumps(DNS_response)
        s.sendto(dns_object.encode(),clientaddress)

    else:
        database = {message["NAME"]: message}         #Registration
        as_object = json.dumps(database)
        with open("out.json", "w") as outfile:
            outfile.write(as_object)
        s.sendto(str(201).encode(), clientaddress)


       


      