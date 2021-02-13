from aiohttp import web
from . import utils
from contextvars import ContextVar


async def dist_handler(request: web.Request):
    num_gpus = int(request.query['num_gpus'])
    data = {
        'dist_url': request.app['dist_url'],
        'rank_start': request.app['rank_start'],
    }
    request.app['rank_start'] += num_gpus
    return web.json_response(data)


def start_web_server(
    host: str,
    dist_port: int,
    http_port: int,
    rank_start: int,
):
    app = web.Application()
    dist_url = utils.get_dist_url(host, dist_port)
    app['dist_url'] = dist_url
    app['rank_start'] = rank_start
    # app.add_routes([web.get('/', dist_handler)])
    app.router.add_get('/', dist_handler)
    web.run_app(app, host=host, port=http_port)
    return app


if __name__ == '__main__':
    start_web_server(
        '127.0.0.1',
        12345,
        3000,
        2
    )
