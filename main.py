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
alpha_algorithm.display_footprint()

# Displays maximal causal pairs
alpha_algorithm.display_YL()

# Displays as petri net
alpha_algorithm.display_petri_net()
