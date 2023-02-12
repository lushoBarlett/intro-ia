from itertools import product

class BayesianNetwork:
    def __init__(self, *events):
        self.events = set(events)
        self.priori_event = {}
        self.caused_event = {}

    def priori(self, event, probability):
        self.priori_event[event] = probability

    def cause(self, event, causes, probabilities):
        self.caused_event[event] = (causes, probabilities)

    def all_events_accounted_for(self):
        return all(event in self.priori_event or event in self.caused_event for event in self.events)

    def events_included(self, events):
        return all(event.lstrip("¬") in self.events for event in events)

    def priori_probability_of(self, event):
        if event.startswith("¬"):
            return 1 - self.priori_probability_of(event.lstrip("¬"))

        return self.priori_event[event]

    def caused_probability_of(self, event, events):
        if event.startswith("¬"):
            return 1 - self.caused_probability_of(event.lstrip("¬"), events)

        causes, probabilities = self.caused_event[event]
        truth_values = tuple([cause in events for cause in causes])
        return probabilities[truth_values]

    def calculate_completion(self, events):
        probability = 1

        for event in events:
            probability *= (
                self.priori_probability_of(event)
                if event.lstrip("¬") in self.priori_event else
                self.caused_probability_of(event, events)
            )

        return probability

    def undetermined(self, determined):
        return self.events - set(d.lstrip("¬") for d in determined)

    def possible_assignments(self, determined):
        return ((event, "¬" + event) for event in self.undetermined(determined))

    def sum_completions(self, determined):
        return sum(
            self.calculate_completion(determined | set(determination_case))
            for determination_case in product(*self.possible_assignments(determined))
        )

    def maximum_completion(self, determined):
        return max(
            (determined | set(determination_case)
            for determination_case in product(*self.possible_assignments(determined))),

            key=lambda events: self.calculate_completion(events)
        )

    def calculate(self, pexpr):
        assert self.all_events_accounted_for()
        assert pexpr.subset_of_events(self.events)

        if len(pexpr.assumptions):

            ptop, pbot = pexpr.bayes_rule()

            return self.calculate(ptop) / self.calculate(pbot)

        return self.sum_completions(pexpr.events)

    def belief_update(self, priori, evidence):
        assert priori in self.priori_event
        self.priori_event[priori] = self.calculate(P(priori).given(*evidence))
        return self.priori_event[priori]

    def belief_revision(self, *evidence):
        evidence = set(evidence)
        assert self.all_events_accounted_for()
        assert self.events_included(evidence)

        return self.maximum_completion(evidence)


class PExpr:
    def __init__(self, *events):
        self.events = set(events)
        self.assumptions = set()

    def given(self, *assumptions):
        self.assumptions = set(assumptions)
        return self

    def bayes_rule(self):
        return PExpr(*(self.events | self.assumptions)), PExpr(*self.assumptions)

    def subset_of_events(self, events):
        return all(event.lstrip("¬") in events for event in self.events | self.assumptions)


def P(*events):
    p = PExpr(*events)
    return p
