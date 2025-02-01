from collections import defaultdict


class AlphaMiner:
    def __init__(self, event_log):
        self.event_log = event_log
        self.activities = self.collect_activities()
        self.direct_follows = self.determine_direct_follows()
        self.footprint = self.construct_footprint()

    def collect_activities(self):
        activities = set()
        for trace in self.event_log:
            activities.update(trace)
        return sorted(activities)

    def determine_direct_follows(self):
        follows = defaultdict(lambda: defaultdict(int))
        for trace in self.event_log:
            seen = set()
            for i in range(len(trace) - 1):
                if (trace[i], trace[i + 1]) not in seen:
                    follows[trace[i]][trace[i + 1]] += 1
                seen.add((trace[i], trace[i + 1]))
        return follows

    def construct_footprint(self):
        footprint = {x: {y: '#' for y in self.activities} for x in self.activities}
        for a in self.activities:
            for b in self.activities:
                if a != b:
                    a_to_b = self.direct_follows[a][b] > 0
                    b_to_a = self.direct_follows[b][a] > 0
                    if a_to_b and b_to_a:
                        footprint[a][b] = '||'
                    elif a_to_b:
                        footprint[a][b] = '→'
                    elif b_to_a:
                        footprint[a][b] = '←'
        return footprint

    def get_footprint(self):
        return self.footprint

    def get_YL(self):
        inputs_to_outputs = defaultdict(set)
        outputs_to_inputs = defaultdict(set)

        for x in self.activities:
            for y in self.activities:
                if self.footprint[x][y] == '→':
                    inputs_to_outputs[x].add(y)
                    outputs_to_inputs[y].add(x)

        YL = set()

        reverse_map = defaultdict(set)
        for inputs, outputs in inputs_to_outputs.items():
            reverse_map[frozenset(outputs)].add(inputs)

        for outputs, inputs in reverse_map.items():
            YL.add((frozenset(inputs), outputs))

        return YL

