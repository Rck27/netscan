import json
import ros_api

python -m pip install laiarturs-ros-api


#check if theres any unchanged mikrotik on network
# must have json file of port 8728 using masscan

f = open("/home/deeric/bin/masscan/tes.json")
g = open("/home/deeric/bin/masscan/hasil.txt", "a")
parsed = json.load(f)
parsedLen = len(parsed)
count = 0
while count < parsedLen:
    # print(parsed[count]['ip'])
    # router = ros_api.Api('192.168.2.1', user='admin', password='admin', port=8728)
    # r = router.talk('/ip/address/print')
    # print(r)
    # if(ConnectionRefusedError) : print("hooh")
    try:
        router = ros_api.Api(parsed[count]['ip'], user='admin', password='admin', port=8728)
        r = router.connection
        # print(r)
    except :
        print("hooh")
    else:
        print(parsed[count]['ip'])
        g.write(str(parsed[count]['ip'])+ "#")
    count += 1

g.close()
