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