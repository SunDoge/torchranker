import torch
import argparse
from torchranker import get_dist_info
import logging

_logger = logging.getLogger(__name__)


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', type=str, required=True)
    parser.add_argument('--dist-port', type=int)
    parser.add_argument('--http-port', type=int, required=True)
    parser.add_argument('--world-size', type=int, required=True)
    return parser


def main():
    logging.basicConfig(level=logging.DEBUG)

    parser = get_parser()
    args = parser.parse_args()
    num_gpus = torch.cuda.device_count()
    host = args.host
    dist_port = args.dist_port
    http_port = args.http_port
    world_size = args.world_size

    dist_url, rank_start = get_dist_info(
        host=host,
        http_port=http_port,
        dist_port=dist_port,
        num_gpus=num_gpus,
        world_size=world_size,
    )

    _logger.info('dist_url: %s', dist_url)
    _logger.info('rank_start: %s', rank_start)


if __name__ == '__main__':
    main()
