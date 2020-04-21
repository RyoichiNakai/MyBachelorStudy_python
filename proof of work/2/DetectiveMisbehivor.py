import numpy as np
np.seterr(divide='ignore', invalid='ignore')
f = open('/home/ryoichi/Templates/BlockchainProjects/result/result_new_transaction.txt')
areas = f.read().split()
bf = open('/home/ryoichi/Templates/BlockchainProjects/result/result_new_block_time.txt')
b_areas = bf.read().split()
c = 0

v_fcnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 偽装されていると判断しているデータのうちのフォールスポジティブ
v_tcnt = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 偽装されていると判断したうちデータのうちの本当に偽装されているデータ
detective_means = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 各サーバの偽装検知の平均時間
all_detective_means = []  # すべてのサーバの偽装検知の平均時間
means_blocktime = []  # ブロックをマイニングした平均時間

for t in areas:
    a = t.split(',')
    if a[0] == '50070' and a[3] == 'TRUE':
        v_tcnt[0] += 1
    elif a[0] == '50070' and a[3] == 'FALSE':
        v_fcnt[0] += 1
        detective_means[0] += float(a[4])
    elif a[0] == '50072' and a[3] == 'TRUE':
        v_tcnt[1] += 1
    elif a[0] == '50072' and a[3] == 'FALSE':
        v_fcnt[1] += 1
        detective_means[1] += float(a[4])
    elif a[0] == '50074' and a[3] == 'TRUE':
        v_tcnt[2] += 1
    elif a[0] == '50074' and a[3] == 'FALSE':
        v_fcnt[2] += 1
        detective_means[2] += float(a[4])
    elif a[0] == '50076' and a[3] == 'TRUE':
        v_tcnt[3] += 1
    elif a[0] == '50076' and a[3] == 'FALSE':
        v_fcnt[3] += 1
        detective_means[3] += float(a[4])
    elif a[0] == '50078' and a[3] == 'TRUE':
        v_tcnt[4] += 1
    elif a[0] == '50078' and a[3] == 'FALSE':
        v_fcnt[4] += 1
        detective_means[4] += float(a[4])
    elif a[0] == '50080' and a[3] == 'TRUE':
        v_tcnt[5] += 1
    elif a[0] == '50080' and a[3] == 'FALSE':
        v_fcnt[5] += 1
        detective_means[5] += float(a[4])
    elif a[0] == '50082' and a[3] == 'TRUE':
        v_tcnt[6] += 1
    elif a[0] == '50082' and a[3] == 'FALSE':
        v_fcnt[6] += 1
        detective_means[6] += float(a[4])
    elif a[0] == '50084' and a[3] == 'TRUE':
        v_tcnt[7] += 1
    elif a[0] == '50084' and a[3] == 'FALSE':
        v_fcnt[7] += 1
        detective_means[7] += float(a[4])
    elif a[0] == '50086' and a[3] == 'TRUE':
        v_tcnt[8] += 1
    elif a[0] == '50086' and a[3] == 'FALSE':
        v_fcnt[8] += 1
        detective_means[8] += float(a[4])
    elif a[0] == '50088' and a[3] == 'TRUE':
        v_tcnt[9] += 1
    elif a[0] == '50088' and a[3] == 'FALSE':
        v_fcnt[9] += 1
        detective_means[9] += float(a[4])


for i in b_areas:
    b = i.split(',')
    means_blocktime.append(float(b[1]))

for i in range(10):
    if v_fcnt[i] != 0:
        detective_means[i] = detective_means[i]/v_fcnt[i]
        c = detective_means[i]
        all_detective_means.append(c)
        print(all_detective_means)


print("v_tcnt:", v_tcnt)
print("v_fcnt:", v_fcnt)
print("各検知時間:", detective_means)
print("偽装の検知時間:", np.mean(all_detective_means))
print("ブロックの生成時間:", np.mean(means_blocktime))

f.close()
bf.close()
