# alpha_miner.py

class AlphaMiner:
    def __init__(self, event_log):
        # Store the event log
        self.event_log = event_log

        # Extract unique activities from the event log
        unique_activities = set()
        for trace in event_log:
            for activity in trace:
                unique_activities.add(activity)

        # Sort the unique activities
        self.activities = sorted(unique_activities)

        # Determine the footprint matrix
        self.footprint = self._determine_footprint()

        # Determine the set YL of pairs of sets A and B
        self.YL = self._determine_YL()

    def _determine_footprint(self):
        """
        Determines the footprint matrix for the given event log.
        """
        # Initialize empty footprint string matrix
        footprint = {}
        for activity1 in self.activities:
            footprint[activity1] = {}
            for activity2 in self.activities:
                footprint[activity1][activity2] = ''

        # Initialize empty dict for directly follows relations
        follows = {}
        for activity in self.activities:
            follows[activity] = set()

        # Determine directly follows relations from the event log
        for trace in self.event_log:
            for i in range(len(trace) - 1):
                current_activity = trace[i]
                next_activity = trace[i + 1]
                follows[current_activity].add(next_activity)

        # Populate the footprint matrix
        for activity1 in self.activities:
            for activity2 in self.activities:
                if activity1 == activity2:
                    footprint[activity1][activity2] = '#'

                # determine directly follows events
                elif activity2 in follows[activity1]:
                    footprint[activity1][activity2] = '→'

                # determine preceding events
                elif activity1 in follows[activity2]:
                    footprint[activity1][activity2] = '←'

                # determine parallel events
                elif len(
                            follows[activity1]
                        .intersection(
                            follows[activity2])
                ) > 0:
                    footprint[activity1][activity2] = '||'

                else:
                    footprint[activity1][activity2] = '#'

        return footprint

    def _find_causal_relationships(self):
        """
        Finds causal relationships based on directly follows relationships.
        """
        # Initialize a dict to count directly follows relationships
        directly_follows = {}
        for activity in self.activities:
            directly_follows[activity] = {}

        # Count directly follows relationships from the event log
        for trace in self.event_log:
            # iterate i over trace len
            for i in range(len(trace) - 1):
                current_activity = trace[i]
                next_activity = trace[i + 1]
                # if next_activity not in dict yet then assume not causal for each iteration first
                if next_activity not in directly_follows[current_activity]:
                    directly_follows[current_activity][next_activity] = 0
                # assume causal relation for next_activity of current_activity
                directly_follows[current_activity][next_activity] += 1

        # Store found causal pairs in a set
        causal_pairs = set()
        for activity in directly_follows:
            for follower in directly_follows[activity]:
                if directly_follows[activity][follower] > 0:
                    causal_pairs.add((activity, follower))

        return causal_pairs

    # alpha_miner.py

    @staticmethod
    def _find_maximal_pairs(causal_pairs):
        """
        Finds maximal pairs of sets A and B where elements in A are causally related to elements in B.
        """
        maximal_pairs = set()  # Initialize an empty set to store maximal pairs

        # Iterate over each pair of activities in causal_pairs
        for activity_a, activity_b in causal_pairs:
            set_a = {activity_a}  # Start with a set activity_a as A
            set_b = {activity_b}  # Start with a set activity_b as B

            # Iterate over causal_pairs again to find all related activities for A and B
            for other_activity_a, other_activity_b in causal_pairs:
                # Add other_activity_a to set A if not there yet when other_activity_b is in set B
                if other_activity_a not in set_a and other_activity_b in set_b:
                    set_a.add(other_activity_a)

                # Add other_activity_b to set B not already there yet and other_activity_a is in set A
                if other_activity_b not in set_b and other_activity_a in set_a:
                    set_b.add(other_activity_b)

            # Add the maximal pair to the maximal_pairs set
            maximal_pairs.add(
                (
                    frozenset(set_a),
                    frozenset(set_b)
                )
            )

        return maximal_pairs

    def _determine_YL(self):
        """
        Determines the set YL of pairs of sets A and B according to the Alpha algorithm.
        """
        # Find causal relationships
        causal_pairs = self._find_causal_relationships()

        # Find maximal pairs of sets A and B
        maximal_pairs = self._find_maximal_pairs(causal_pairs)

        return maximal_pairs

    def get_footprint(self):
        """
        Returns the footprint matrix.
        """
        return self.footprint

    def get_YL(self):
        """
        Returns the set YL of pairs of sets A and B.
        """
        return self.YL

    def get_petri_net(self):
        """
        Derives a Petri net from the set YL.
        """
        # Initialize lists for places, transitions, and arcs
        places = []
        transitions = []
        arcs = []

        # Create places and transitions based on YL
        for set_a, set_b in self.YL:
            place = f"P({set_a},{set_b})"
            places.append(place)
            transition = f"T({set_a},{set_b})"
            transitions.append(transition)

            for activity in set_a:
                arc_in = f"{activity} -> {place}"
                arcs.append(arc_in)
            for activity in set_b:
                arc_out = f"{place} -> {activity}"
                arcs.append(arc_out)

        # Return the Petri net structure
        return {"places": places, "transitions": transitions, "arcs": arcs}

    def display_footprint(self):
        """
        Displays the footprint matrix.
        """
        print("Footprint Matrix:")

        # Create and display header
        header = '  '
        for activity in self.activities:
            header += activity + ' '
        print(header)

        # Display each row of the footprint matrix
        for activity1 in self.activities:
            row = activity1 + ' '
            for activity2 in self.activities:
                row += self.footprint[activity1][activity2] + ' '
            print(row)

    def display_YL(self):
        """
        Displays the set YL of pairs of sets A and B.
        """
        print("\nYL:")

        # Display each pair of sets in YL
        for set_a, set_b in self.YL:
            set_a_str = set(set_a)
            set_b_str = set(set_b)
            print(f"({set_a_str}, {set_b_str})")

    def display_petri_net(self):
        """
        Displays the Petri net structure.
        """
        petri_net = self.get_petri_net()

        # Display places
        print("\nPetri Net:")
        print("Places:")
        for place in petri_net["places"]:
            print(place)

        # Display transitions
        print("\nTransitions:")
        for transition in petri_net["transitions"]:
            print(transition)

        # Display arcs
        print("\nArcs:")
        for arc in petri_net["arcs"]:
            print(arc)
