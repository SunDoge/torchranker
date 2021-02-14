# TorchRanker

## Usage

```python
from torchranker import get_dist_info

dist_url, rank_start = get_dist_info(
    host=host,
    http_port=http_port,
    dist_port=dist_port,
    num_gpus=num_gpus,
    world_size=world_size,
)
```

## How it works

1. 如果num_gpus >= world_size，说明当前是单机多卡，返回dist_url, rank_start=0。
2. 如果num_gpus < world_size，说明当前是多节点
   1. 如果是单机多节点，第一个启动的进程为rank0，后续进程自动分配rank
   2. 如果是多机多节点，host对应的服务器为rank0，后续进程自动分配rank