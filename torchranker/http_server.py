import asyncio
from aiohttp import web
from . import utils
from contextvars import ContextVar
from asyncio import CancelledError


async def dist_handler(request: web.Request):
    # num_gpus = int(request.query['num_gpus'])
    num_gpus = int(request.match_info['num_gpus'])
    rank_start = request.app['rank_start']
    data = {
        'dist_url': request.app['dist_url'],
        'rank_start': rank_start,
    }
    new_rank_start = rank_start + num_gpus
    request.app['rank_start'] = new_rank_start
    return web.json_response(data)

    # try:
    #     return web.json_response(data)
    # finally:
    #     if new_rank_start >= request.app['world_size']:
    #         print('should shutdown')
    #         await asyncio.sleep(10)
    #         raise KeyboardInterrupt()


async def shutdown_handler(request: web.Request):
    raise KeyboardInterrupt()


def start_web_server(
    host: str,
    dist_port: int,
    http_port: int,
    # world_size: int,
    rank_start: int,
):
    app = web.Application()
    dist_url = utils.get_dist_url(host, dist_port)
    app['dist_url'] = dist_url
    app['rank_start'] = rank_start
    # app['world_size'] = world_size
    # app.add_routes([web.get('/', dist_handler)])
    app.router.add_get('/gpus/{num_gpus}', dist_handler)
    app.router.add_get('/shutdown', shutdown_handler)
    try:
        web.run_app(app, host=host, port=http_port)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':

    start_web_server(
        '127.0.0.1',
        12345,
        3000,
        2
    )

    print('fuck')
