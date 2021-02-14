from torchranker import utils


def test_get_dist_url():
    dist_url = utils.get_dist_url('127.0.0.1', 12345)
    assert dist_url == 'tcp://127.0.0.1:12345'


def test_is_loopback():
    assert utils.is_loopback('127.0.0.1')
    assert not utils.is_loopback('baidu.com')


def test_find_free_port():
    free_port = utils.find_free_port()
    assert utils.is_free_port(free_port), free_port
