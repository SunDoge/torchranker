"""
host: 需指定
http_port: 需指定
dist_port: 默认12345

1 确认host是否为localhost
2 如果是localhost，就起一个http server，并返回rank_start=0，返回dist_url=host+dist_port
3 如果不是localhost，就请求host+http_port，请求成功，返回rank_start, dist_url
"""



