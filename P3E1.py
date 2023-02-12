from bayes import BayesianNetwork as BN, P

bn = BN("R", "T", "A", "J", "M")

bn.priori("R", 0.001)
bn.priori("T", 0.002)

bn.cause("A", ("R", "T"), {
    (True, True):   0.950,
    (True, False):  0.950,
    (False, True):  0.290,
    (False, False): 0.001,
})

bn.cause("J", ("A",), {
    (True,):  0.90,
    (False,): 0.05,
})

bn.cause("M", ("A",), {
    (True,):  0.70,
    (False,): 0.01,
})

print(bn.calculate(P("R").given("J")))
print(bn.calculate(P("R").given("J", "M")))
print(bn.calculate(P("J").given("R")))
