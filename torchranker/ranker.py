"""
host: 需指定
http_port: 需指定
dist_port: 默认12345

1 确认host是否为localhost
2 如果是localhost，就起一个http server，并返回rank_start=0，返回dist_url=host+dist_port
3 如果不是localhost，就请求host+http_port，请求成功，返回rank_start, dist_url
"""

from typing import Optional, Tuple
from . import http_client, http_server, utils
import logging

_logger = logging.getLogger(__name__)


def get_dist_info(
    host: str,
    http_port: int,
    num_gpus: int,
    world_size: int,
    dist_port: Optional[int] = None,
) -> Tuple[str, int]:
    if dist_port is None:
        dist_port = utils.find_free_port()
        _logger.debug('find free dist_port: %s', dist_port)

    if utils.host_is_local(host):
        _logger.debug('this is node0, start http server')
        return http_server.start_web_server(
            host=host,
            dist_port=dist_port,
            http_port=http_port,
            rank_start=num_gpus
        )
    else:
        _logger.debug('this is not node0, try to get dist info')
        return http_client.get_dist_info(
            host=host,
            http_port=http_port,
            num_gpus=num_gpus,
            world_size=world_size
        )
