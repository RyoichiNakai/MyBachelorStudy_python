import json
from time import sleep
from transaction.vehicleInfo import VehicleInfo
from transaction.vehicleInfo import Transaction
from transaction.transaction_pool import TransactionPool
from transaction.verify_locinfo import VerifyLocinfo

f = open('/home/ryoichi/Templates/BlockchainProjects/test/test10.json', 'r')
json_dict = json.load(f)
new_block = {'timestamp': 1566367320.4333398, 'transactions': ['{"sendtime": 1566367318.4016025, "vehicleinfo": [{"ID": "1", "TorF": "TRUE", "timestamp": 5.7, "x": "-307.038", "y": "342.152"}]}', '{"sendtime": 1566367318.502318, "vehicleinfo": [{"ID": "1", "TorF": "TRUE", "timestamp": 5.8, "x": "-305.498", "y": "342.150"}]}', '{"sendtime": 1566367318.603062, "vehicleinfo": [{"ID": "1", "TorF": "TRUE", "timestamp": 5.9, "x": "-303.958", "y": "342.148"}]}', '{"sendtime": 1566367318.7034523, "vehicleinfo": [{"ID": "1", "TorF": "TRUE", "timestamp": 6.0, "x": "-302.418", "y": "342.147"}]}', '{"sendtime": 1566367318.8041232, "vehicleinfo": [{"ID": "1", "TorF": "TRUE", "timestamp": 6.1, "x": "-300.878", "y": "342.145"}]}', '{"sendtime": 1566367318.9048822, "vehicleinfo": [{"ID": "1", "TorF": "TRUE", "timestamp": 6.2, "x": "-299.337", "y": "342.143"}]}', '{"sendtime": 1566367319.0062335, "vehicleinfo": [{"ID": "1", "TorF": "TRUE", "timestamp": 6.3, "x": "-297.795", "y": "342.141"}]}', '{"sendtime": 1566367319.1069624, "vehicleinfo": [{"ID": "1", "TorF": "TRUE", "timestamp": 6.4, "x": "-296.253", "y": "342.139"}]}', '{"sendtime": 1566367319.208106, "vehicleinfo": [{"ID": "1", "TorF": "TRUE", "timestamp": 6.5, "x": "-294.711", "y": "342.137"}]}', '{"sendtime": 1566367319.3099248, "vehicleinfo": [{"ID": "1", "TorF": "TRUE", "timestamp": 6.6, "x": "-293.169", "y": "342.135"}]}', '{"sendtime": 1566367319.4106162, "vehicleinfo": [{"ID": "1", "TorF": "TRUE", "timestamp": 6.7, "x": "-291.626", "y": "342.133"}]}', '{"sendtime": 1566367319.5117548, "vehicleinfo": [{"ID": "1", "TorF": "TRUE", "timestamp": 6.8, "x": "-290.082", "y": "342.132"}]}', '{"sendtime": 1566367319.61383, "vehicleinfo": [{"ID": "1", "TorF": "TRUE", "timestamp": 6.9, "x": "-288.538", "y": "342.130"}]}', '{"sendtime": 1566367319.7148943, "vehicleinfo": [{"ID": "1", "TorF": "TRUE", "timestamp": 7.0, "x": "-286.994", "y": "342.128"}]}', '{"sendtime": 1566367319.8157475, "vehicleinfo": [{"ID": "1", "TorF": "TRUE", "timestamp": 7.1, "x": "-285.449", "y": "342.126"}]}', '{"sendtime": 1566367319.9164839, "vehicleinfo": [{"ID": "1", "TorF": "TRUE", "timestamp": 7.2, "x": "-283.904", "y": "342.124"}]}', '{"sendtime": 1566367320.017227, "vehicleinfo": [{"ID": "1", "TorF": "TRUE", "timestamp": 7.3, "x": "-282.359", "y": "342.122"}]}', '{"sendtime": 1566367320.118309, "vehicleinfo": [{"ID": "1", "TorF": "TRUE", "timestamp": 7.4, "x": "-280.813", "y": "342.120"}]}', '{"sendtime": 1566367320.2190073, "vehicleinfo": [{"ID": "1", "TorF": "TRUE", "timestamp": 7.5, "x": "-279.267", "y": "342.119"}]}', '{"sendtime": 1566367320.319833, "vehicleinfo": [{"ID": "1", "TorF": "TRUE", "timestamp": 7.6, "x": "-277.720", "y": "342.117"}]}'], 'previous_block': 'a17540ceccaba099e53b633b0e3857532e9ad1f2fdd5e561e2690a3e0d3f0dd8', 'nonce': '3'}
tp = TransactionPool()
vl = VerifyLocinfo()
cnt = -1
c_cnt = 0

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

    to_be_signed = json.dumps(trx.to_dict(), sort_keys=True)
    new_tx = json.loads(to_be_signed)
    tx_strings = json.dumps(new_tx)
    """
    print(tx_strings)
    sleep(0.1)
    """
    new_transaction = json.loads(tx_strings)
    current_transactions = tp.get_stored_transactions()
    if len(current_transactions) > 0 and vl.verify_trlocinfo(new_transaction, current_transactions):
        c_cnt += 1

    tp.set_new_transaction(new_transaction)
    # print("cnt, c_cnt", cnt, c_cnt)

print(new_block)
block_processtime = vl.extract_newblockprocesstime(new_block)
print(block_processtime)

