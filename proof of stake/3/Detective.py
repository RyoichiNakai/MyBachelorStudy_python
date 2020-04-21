import json
import collections as cl

f = open('/home/ryoichi/Templates/BlockchainProjects/vehicle/vehicle2.json', 'r')
json_dict = json.load(f)  # loadはファイルの読み込み
cnt = 0
dcnt = 0
for t in json_dict:
    cnt += 1
    if cnt % 10 == 0 :
        json_dict[str(t)]['TorF'] = 'FALSE'
        json_dict[str(t)]['x'] = '0.5'
        json_dict[str(t)]['y'] = '0.5'

for t in json_dict:
    if json_dict[str(t)]['TorF'] == 'FALSE':
        dcnt += 1

print(dcnt)
fw = open('/home/ryoichi/Templates/BlockchainProjects/vehicle/misvehicle2.json', 'w')
json.dump(json_dict, fw)
