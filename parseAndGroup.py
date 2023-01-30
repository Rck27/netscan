import json
from random import randint
f = open("80.json")
# because of the first half of the octet would be the same, we would just discard it
hasil = {
}
# '3rd octet':[array of active host]

raw = ['192.168.1.7', '192.168.2.44', '192.168.1.5']
for i in range(1, 20):
    raw.append("192.168."+str(randint(1, 254))+"."+str(randint(1,254)))
print(raw)
parsed = json.load(f)

for i in raw:
    splt = i.split(".")
    if hasil.get(splt[2]) is None : hasil[splt[2]] = [splt[3]]
    else : hasil[splt[2]].append(splt[3])
    #if hasil[i].count() > 0 : print(i)#hasil[i].append(i.split(".")[3])

print(hasil)
# li = [1,7,7,23,5,12]
# for i in :
#     print(hasil['192.168.1.0'].count(1))
#     hasil[str(i)] = [123,123123]
# print(hasil)
# for i in parsed:
#     i['ip'].split(".")[3] += i['ip']
#     # parsed["tess"] = "{}"
#     print(hasil)
# print(parsed[0]['ip'].split(".")[2])
