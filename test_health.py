def test_zookeeper():

    from kazoo.client import KazooClient
    from kazoo.exceptions import KazooException

    zk = KazooClient(hosts='localhost:2181')

    try:
        zk.start()
        assert zk.state == 'CONNECTED'
    finally:
        zk.stop()