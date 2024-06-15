import unittest

from alpha_miner import AlphaMiner

class TestAlphaMiner(unittest.TestCase):
    def setUp(self):
        # Example event log
        self.event_log = [
            ['a', 'c', 'b'],
            ['a', 'g', 'b'],
            ['a', 'd', 'e', 'f', 'b']
        ]
        self.alpha = AlphaMiner(self.event_log)

    def test_footprint(self):
        expected_footprint = {
            'a': {'a': '#', 'b': '#', 'c': '→', 'd': '→', 'e': '#', 'f': '#', 'g': '→'},
            'b': {'a': '#', 'b': '#', 'c': '←', 'd': '#', 'e': '#', 'f': '←', 'g': '←'},
            'c': {'a': '←', 'b': '→', 'c': '#', 'd': '#', 'e': '#', 'f': '||', 'g': '||'},
            'd': {'a': '←', 'b': '#', 'c': '#', 'd': '#', 'e': '→', 'f': '#', 'g': '#'},
            'e': {'a': '#', 'b': '#', 'c': '#', 'd': '←', 'e': '#', 'f': '→', 'g': '#'},
            'f': {'a': '#', 'b': '→', 'c': '||', 'd': '#', 'e': '←', 'f': '#', 'g': '||'},
            'g': {'a': '←', 'b': '→', 'c': '||', 'd': '#', 'e': '#', 'f': '||', 'g': '#'}
        }
        self.assertEqual(self.alpha.get_footprint(), expected_footprint)

    def test_YL(self):
        expected_YL = {
            (frozenset({'c', 'g', 'f'}), frozenset({'b'})),
            (frozenset({'e'}), frozenset({'f'})),
            (frozenset({'d'}), frozenset({'e'})),
            (frozenset({'a'}), frozenset({'c', 'd', 'g'}))
        }
        self.assertEqual(self.alpha.get_YL(), expected_YL)


if __name__ == '__main__':
    unittest.main()
