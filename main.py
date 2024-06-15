# main.py

from dist.alpha_miner import AlphaMiner

# Given event log
event_log = [
    ['a', 'c', 'b'],
    ['a', 'c', 'b'],
    ['a', 'c', 'b'],
    ['a', 'g', 'b'],
    ['a', 'g', 'b'],
    ['a', 'd', 'e', 'f', 'b']
]

# Instance
alpha_algorithm = AlphaMiner(event_log)

# Display the footprint matrix
alpha_algorithm.display_footprint()

# Displays maximal causal pairs
alpha_algorithm.display_YL()

# Displays as petri net
alpha_algorithm.display_petri_net()
