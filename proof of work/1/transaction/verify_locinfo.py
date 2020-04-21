import math
import numpy as np
# 位置情報の偽装を検知する距離
check_dis = 3.3
# 時速120km

class VerifyLocinfo:

    def __init__(self):
        self.new_list = []
        self.old_lists = []
        self.newblock = []

    def verify_trlocinfo(self, new_list, old_lists):
        x1, y1, x2, y2 = self.extract_trlocinfo(new_list, old_lists)
        if self.get_distance(float(x1), float(y1), float(x2), float(y2)) <= check_dis:
            return True
        else:
            return False

    def extract_trlocinfo(self, new_list, old_lists):
        """
        トランザクションプールから新しいトランザクションと同じIDの１つ前のタイムスタンプの
        トランザクションからx座標とy座標を取り出す
        :param new_list:
        :param old_lists:
        :return: ntr_x, ntr_y, ptr_x, ptr_y
        """
        global prev_list
        ntr = new_list['vehicleinfo']
        ntr_id = [i['ID'] for i in ntr]
        ntr_ID = ntr_id[0] if len(ntr_id) else ''
        ntr_ts = [i['timestamp'] for i in ntr]
        ntr_timestamp = ntr_ts[0] if len(ntr_ts) else ''
        ntr_px = [i['x'] for i in ntr]
        ntr_x = ntr_px[0] if len(ntr_px) else ''
        ntr_py = [i['y'] for i in ntr]
        ntr_y = ntr_py[0] if len(ntr_py) else ''

        # 逆順走査でリストを調べていく
        for i in reversed(old_lists):
            otr = i['vehicleinfo']
            otr_id = [i['ID'] for i in otr]
            otr_ID = otr_id[0] if len(otr_id) else ''
            otr_ts = [i['timestamp'] for i in otr]
            otr_timestamp = otr_ts[0] if len(otr_ts) else ''
            # timestampが一番大きいものを１つ前の位置情報を比較するトランザクションとする
            # IDが同じ車両同士で比較する
            if otr_ID == ntr_ID and otr_timestamp < ntr_timestamp:
                index = old_lists.index(i)
                prev_list = old_lists[index]
                print("prev_transaction", prev_list)
                break  # 同じIDの1つ前のトランザクションだけを見ればいいからここでbreak

        ptr = prev_list['vehicleinfo']
        ptr_px = [i['x'] for i in ptr]
        ptr_x = ptr_px[0] if len(ptr_px) else ''
        ptr_py = [i['y'] for i in ptr]
        ptr_y = ptr_py[0] if len(ptr_py) else ''

        return ntr_x, ntr_y, ptr_x, ptr_y

    def get_distance(self, x1, y1, x2, y2):
        dis = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return dis

    def extract_newblockprocesstime(self, newblock):
        block_timestamp = newblock['timestamp']
        block_tr_list = newblock['transactions']
        block_tr_ts = []

        for t in block_tr_list:
            block_tr_ts = t[13:30]
            print(block_tr_ts)

        means_tr_ts = np.mean(float(block_tr_ts))
        return means_tr_ts
