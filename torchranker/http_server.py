from aiohttp import web
from . import utils


def get_app(
    host: str,
    http_port: int,
    dist_port: int,
    world_size: int,
    
):
    app = web.Application()
    app['host'] = host
    app['http_port'] = http_port
    app['dist_port'] = dist_port
    dist_url = utils.get_dist_url(host, dist_port)
    app['dist_url'] = dist_url
    app['']
    web.run_app
