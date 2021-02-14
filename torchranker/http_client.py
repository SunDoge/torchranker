from socket import timeout
from typing import Tuple
import requests
import logging
import time

_logger = logging.getLogger(__name__)


def get_dist_info(
    host: str,
    http_port: int,
    num_gpus: int,
    world_size: int,
) -> Tuple[str, int]:
    url = f'http://{host}:{http_port}'

    success = False
    while not success:
        try:
            resp = requests.get(url, params=dict(num_gpus=num_gpus))
            success = True
        except:
            time.sleep(5)

    data = resp.json()
    dist_url = data['dist_url']
    rank_start = data['rank_start']

    if rank_start + num_gpus >= world_size:
        try:
            resp = requests.get(url + '/shutdown')
        except:
            _logger.warning('shutdown server with stats: %s', resp.status_code)

    return dist_url, rank_start


if __name__ == '__main__':
    dist_url, rank_start = get_dist_info(
        '127.0.0.1', 3000, 2, 8,
    )
    print('dist_url', dist_url)
    print('rank_start', rank_start)
