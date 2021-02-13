import ipaddress
import socket


def get_dist_url(host: str, port: int) -> str:
    dist_url = 'tcp://{host}:{port}'.format(host=host, port=port)
    return dist_url


def is_loopback(host: str) -> bool:
    """
    确认是否为localhost
    """
    address = socket.gethostbyname(host)
    addr: ipaddress.IPv4Address = ipaddress.ip_address(address)
    return addr.is_loopback
