import json
import ros_api
import sys

# to execute, call the file with optional user and admin, default are admin and no password
# use this program to check each address with 8728 port (mikrotik device) and check if it still had default configuration, and dump it on different location
def mikrotik(usr='admin', pw=''):
    f = open("./8728.json")
    g = open("./mikrotikDefault.txt", "a")
    h = open("./mikrotik.txt", "a")
    parsed = json.load(f)
    parsedLen = len(parsed)
    count = 0

    while count < len(parsed):
        ip = parsed[count]['ip']
        try:
            router = ros_api.Api('192.168.1.3', user=usr, password=pw, port=8728)
            r = router.talk('/system/identity/print')
            #print(ip)
            # print(r)
        except :
            print(ip+"error banh")
            h.write(str(parsed[count]['ip'])+"#")
        else:
            print(parsed[count]['ip'])
            g.write(str(parsed[count]['ip'])+':'+r[0]['name']+ "#")
        count += 1

    g.close()
    h.close()
    
mikrotik(sys.argv[1])
