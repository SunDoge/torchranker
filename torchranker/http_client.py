import asyncio
import logging
from typing import Tuple

import aiohttp

_logger = logging.getLogger(__name__)


# def send_num_gpus(url: str, num_gpus: int) -> Tuple[str, int]:
#     async def _send():
#         success = False
#         while not success:
#             try:
#                 pass

async def send_num_gpus(url: str, num_gpus: int):
    async with aiohttp.ClientSession() as session:
        # success = False
        while True:
            try:
                async with session.get(url, params=dict(num_gpus=num_gpus)) as resp:
                    data = await resp.json()
                    return data
            except:
                _logger.debug('wait for 5 seconds')
                await asyncio.sleep(5)


async def send_shutdown(url: str):
    async with aiohttp.ClientSession() as session:
        try:
            await session.get(url)
        except:
            _logger.warning('send shutdown')


def get_dist_info(
    host: str,
    http_port: int,
    num_gpus: int,
    world_size: int,
) -> Tuple[str, int]:
    url = f'http://{host}:{http_port}'

    
    loop = asyncio.get_event_loop()
    data = loop.run_until_complete(send_num_gpus(url, num_gpus))

    dist_url = data['dist_url']
    rank_start = data['rank_start']

    if rank_start + num_gpus >= world_size:
        loop.run_until_complete(send_shutdown(url + '/shutdown'))

    return dist_url, rank_start


if __name__ == '__main__':
    dist_url, rank_start = get_dist_info(
        '127.0.0.1', 3000, 2, 8,
    )
    print('dist_url', dist_url)
    print('rank_start', rank_start)
