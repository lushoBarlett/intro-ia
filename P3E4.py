from bayes import BayesianNetwork as BN, P

bn = BN("a", "b", "c", "d", "e")

bn.priori("a", 0.2)

bn.cause("b", ("a"), {
    (True,):  0.8,
    (False,): 0.2,
})

bn.cause("c", ("a",), {
    (True,):  0.2,
    (False,): 0.05,
})

bn.cause("e", ("c",), {
    (True,):  0.8,
    (False,): 0.6,
})

bn.cause("d", ("b", "c"), {
    (True, True):   0.8,
    (True, False):  0.8,
    (False, True):  0.8,
    (False, False): 0.05,
})

print(bn.calculate(P("a", "b", "c", "d", "e")))
print(bn.calculate(P("¬a", "b", "c", "d", "e")))
print(bn.calculate(P("a").given("d", "e")))
print(bn.calculate(P("a").given("¬d", "e")))
