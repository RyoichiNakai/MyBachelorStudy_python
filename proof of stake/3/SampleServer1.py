import signal
import os
from core.server_core import ServerCore

my_p2p_server = None


def signal_handler(signal, frame):
    shutdown_server()


def shutdown_server():
    global my_p2p_server
    my_p2p_server.shutdown()


def handler(func, *args):
    return func(*args)


def main():
    signal.signal(signal.SIGINT, signal_handler)
    global my_p2p_server

    # os.remove('/home/ryoichi/Templates/BlockchainProjects/result/result_c_cnt.txt')
    # os.remove('/home/ryoichi/Templates/BlockchainProjects/result/result_bc_cnt.txt')
    # os.remove('/home/ryoichi/Templates/BlockchainProjects/result/result_false_cnt.txt')
    # os.remove('/home/ryoichi/Templates/BlockchainProjects/result/result_new_transaction.txt')
    # os.remove('/home/ryoichi/Templates/BlockchainProjects/result/result_new_block.txt')
    # os.remove('/home/ryoichi/Templates/BlockchainProjects/result/result_new_block_time.txt')

    # 始原のCoreノードとして起動する
    my_p2p_server = ServerCore(50070, 1)
    my_p2p_server.start()


if __name__ == '__main__':
    main()