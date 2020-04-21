from time import time

class VehicleInfo:
    """
    車両の現在のタイムスタンプの位置情報をOutput(マイナーノードと位置情報)を管理する
    """
    def __init__(self, id, vehicle_nowX, vehicle_nowY, timestamp, TorF):
        self.id = id
        self.vehicle_nowX = vehicle_nowX
        self.vehicle_nowY = vehicle_nowY
        self.timestamp = timestamp
        self.TorF = TorF

    def to_dict(self):
        d = {
            'ID': self.id,
            'x': self.vehicle_nowX,
            'y': self.vehicle_nowY,
            'timestamp': self.timestamp,
            'TorF': self.TorF
        }
        return d


class Transaction:
    """
    同じ車両の位置情報のInputとOutputを比較し、位置情報を偽装してるものがあれば検知する。
    正当なトランザクションと判断した場合,マイナーノードまで送るようにする。
    """
    def __init__(self, vehicleinfo):
        self.vehicleinfo = vehicleinfo
        self.sendtime = time()

    def to_dict(self):
        # mapは関数を引数として渡してくれる高階関数
        d = {
            'vehicleinfo': list(map(VehicleInfo.to_dict, self.vehicleinfo)),
            'sendtime': self.sendtime
        }
        return d
