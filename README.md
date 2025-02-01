# alpha-miner
The alpha-miner package implements the α-algorithm for process mining, transforming event logs into petri nets.


## Example Usage:

```
# main.py

from src.alpha_miner import AlphaMiner

# Given event log
event_log = [
    ['a', 'b', 'c'],
    ['a', 'c', 'b'],
    ['a', 'b', 'd']
]

# Instance
alpha_algorithm = AlphaMiner(event_log)

# Display the footprint matrix
print(alpha_algorithm.get_footprint())

# Displays maximal causal pairs
print(alpha_algorithm.get_YL())

# Displays as petri net
petri_net = alpha_algorithm.get_petri_net()
petri_net.render('output/petri_net', view=False)
```
