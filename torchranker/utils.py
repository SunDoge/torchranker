import ipaddress
import socket


def find_free_port() -> int:
    """
    Find a free port
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        _host, port = s.getsockname()
    return port


def is_free_port(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('127.0.0.1', port)) != 0


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


def host_is_local(hostname, port=None):
    """returns True if the hostname points to the localhost, otherwise False."""
    if port is None:
        port = 22  # no port specified, lets just use the ssh port
    hostname = socket.getfqdn(hostname)
    if hostname in ("localhost", "0.0.0.0"):
        return True
    localhost = socket.gethostname()
    localaddrs = socket.getaddrinfo(localhost, port)
    targetaddrs = socket.getaddrinfo(hostname, port)
    for (family, socktype, proto, canonname, sockaddr) in localaddrs:
        for (rfamily, rsocktype, rproto, rcanonname, rsockaddr) in targetaddrs:
            if rsockaddr[0] == sockaddr[0]:
                return True
    return False