def test_zookeeper():

    from kazoo.client import KazooClient
    from kazoo.exceptions import KazooException

    zk = KazooClient(hosts='localhost:2181')

    try:
        zk.start()
        assert zk.state == 'CONNECTED'
    finally:
        zk.stop()


def test_ozone():
    import boto3

    s3 = boto3.client('s3', endpoint_url='http://localhost:9878',
        aws_access_key_id='-', aws_secret_access_key='-')

    print(s3.list_buckets())