# alpha-miner
The alpha-miner package implements the α-algorithm for process mining, transforming event logs into petri nets.


## Example Usage:

```
from alpha_miner import AlphaMiner

# Example event log
event_log = [
    ['a', 'c', 'b'],
    ['a', 'g', 'b'],
    ['a', 'd', 'e', 'f', 'b']
]

# Initialize AlphaMiner with the event log
miner = AlphaMiner(event_log)

# Retrieve and display footprint matrix
footprint_matrix = miner.get_footprint()
miner.display_footprint()

# Retrieve and display YL sets
YL_sets = miner.get_YL()
miner.display_YL()

# Retrieve and display Petri net representation
petri_net = miner.get_petri_net()
miner.display_petri_net()
```
