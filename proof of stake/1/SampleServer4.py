import signal

from core.server_core import ServerCore


my_p2p_server = None


def signal_handler(signal, frame):
    shutdown_server()


def shutdown_server():
    global my_p2p_server
    my_p2p_server.shutdown()


def main():
    signal.signal(signal.SIGINT, signal_handler)
    global my_p2p_server
    my_p2p_server = ServerCore(50076, '172.20.69.203', 50072, 4)
    my_p2p_server.start()
    my_p2p_server.join_network()


if __name__ == '__main__':
    main()