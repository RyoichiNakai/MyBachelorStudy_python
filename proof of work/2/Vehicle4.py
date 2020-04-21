import signal
from time import sleep
import json

from core.client_core import ClientCore
from transaction.vehicleInfo import VehicleInfo
from transaction.vehicleInfo import Transaction
from p2p.message_manager import MSG_NEW_TRANSACTION

my_p2p_client = None
f = open('/home/ryoichi/Templates/BlockchainProjects/vehicle/vehicle4.json', 'r')
json_dict = json.load(f)  # loadはファイルの読み込み


def signal_handler(signal, frame):
    shutdown_client()


def shutdown_client():
    global my_p2p_client
    my_p2p_client.shutdown()


def main():
    """
    clientCoreに直接書いても良さそう位置情報を処理をよみこむ処理とか
    :return:
    """
    signal.signal(signal.SIGINT, signal_handler)
    global my_p2p_client
    my_p2p_client = ClientCore(50089, '172.20.69.204', 50076)
    my_p2p_client.start()

    cnt = -1
    for t in json_dict:
        cnt += 1
        x = json_dict[str(t)]['x']
        y = json_dict[str(t)]['y']
        id = json_dict[str(t)]['ID']
        timestamp = json_dict[str(t)]['timestamp']
        TorF = json_dict[str(t)]['TorF']
        trx = Transaction(
            [VehicleInfo(id, x, y, timestamp, TorF)]
        )

        # ソートしてJSON文字列を辞書型に変換し,もう一度JSON形式にする
        to_be_signed = json.dumps(trx.to_dict(), sort_keys=True)
        # loadsはJSON文字列を辞書型にデコードしてくれる
        new_tx = json.loads(to_be_signed)
        # dumpsは辞書型をJSON文字列にエンコードしてくれる
        tx_strings = json.dumps(new_tx)
        my_p2p_client.send_message_to_my_core_node(MSG_NEW_TRANSACTION, tx_strings)
        print(tx_strings)
        with open('/home/ryoichi/Templates/BlockchainProjects/result/result_4.txt', 'w') as file:
            file.write(str(cnt))
        sleep(0.1)


if __name__ == '__main__':
    main()
    f.close()
