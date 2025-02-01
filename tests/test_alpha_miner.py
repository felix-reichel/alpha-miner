import unittest
from src.alpha_miner import AlphaMiner


class TestAlphaMiner(unittest.TestCase):
    def setUp(self):
        self.event_log1 = [
            ['a', 'c', 'b'],
            ['a', 'g', 'b'],
            ['a', 'd', 'e', 'f', 'b']
        ]
        self.alpha1 = AlphaMiner(self.event_log1)

        self.event_log2 = [
            ['a', 'b', 'c'],
            ['a', 'b', 'c'],
            ['a', 'b', 'c'],
            ['a', 'c', 'b'],
            ['a', 'c', 'b'],
            ['a', 'c', 'b'],
            ['a', 'b', 'd'],
            ['a', 'b', 'd']
        ]
        self.alpha2 = AlphaMiner(self.event_log2)

    def test_footprint_case1(self):
        expected_footprint1 = {
            'a': {'a': '#', 'b': '#', 'c': '→', 'd': '→', 'e': '#', 'f': '#', 'g': '→'},
            'b': {'a': '#', 'b': '#', 'c': '←', 'd': '#', 'e': '#', 'f': '←', 'g': '←'},
            'c': {'a': '←', 'b': '→', 'c': '#', 'd': '#', 'e': '#', 'f': '#', 'g': '#'},
            'd': {'a': '←', 'b': '#', 'c': '#', 'd': '#', 'e': '→', 'f': '#', 'g': '#'},
            'e': {'a': '#', 'b': '#', 'c': '#', 'd': '←', 'e': '#', 'f': '→', 'g': '#'},
            'f': {'a': '#', 'b': '→', 'c': '#', 'd': '#', 'e': '←', 'f': '#', 'g': '#'},
            'g': {'a': '←', 'b': '→', 'c': '#', 'd': '#', 'e': '#', 'f': '#', 'g': '#'}
        }
        self.assertEqual(self.alpha1.get_footprint(), expected_footprint1)

    def test_YL_case1(self):
        expected_YL1 = {
            (frozenset({'c', 'g', 'f'}), frozenset({'b'})),
            (frozenset({'e'}), frozenset({'f'})),
            (frozenset({'d'}), frozenset({'e'})),
            (frozenset({'a'}), frozenset({'c', 'd', 'g'}))
        }
        self.assertEqual(self.alpha1.get_YL(), expected_YL1)

    def test_footprint_case2(self):
        expected_footprint2 = {
            'a': {'a': '#', 'b': '→', 'c': '→', 'd': '#'},
            'b': {'a': '←', 'b': '#', 'c': '||', 'd': '→'},
            'c': {'a': '←', 'b': '||', 'c': '#', 'd': '#'},
            'd': {'a': '#', 'b': '←', 'c': '#', 'd': '#'}
        }
        self.assertEqual(self.alpha2.get_footprint(), expected_footprint2)

    def test_YL_case2(self):
        expected_YL2 = {
            (frozenset({'b'}), frozenset({'d'})),
            (frozenset({'a'}), frozenset({'b', 'c'}))
        }
        self.assertEqual(self.alpha2.get_YL(), expected_YL2)


if __name__ == '__main__':
    unittest.main()
