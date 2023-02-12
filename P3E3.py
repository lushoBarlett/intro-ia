from bayes import BayesianNetwork as BN, P

bn = BN("Lluvia", "Riego", "CalleMojada", "PastoMojado", "TierraHúmeda", "RosasOK")

bn.priori("Riego", 0.4)
bn.priori("Lluvia", 0.25)

bn.cause("CalleMojada", ("Riego", "Lluvia"), {
    (True, True):   1,
    (True, False):  1,
    (False, True):  1,
    (False, False): 0,
})

bn.cause("PastoMojado", ("Riego", "Lluvia"), {
    (True, True):   1,
    (True, False):  1,
    (False, True):  1,
    (False, False): 0,
})

bn.cause("TierraHúmeda", ("PastoMojado",), {
    (True,):  0.9,
    (False,): 0.4,
})

bn.cause("RosasOK", ("TierraHúmeda",), {
    (True,):  0.7,
    (False,): 0.2,
})

print(bn.calculate(P("Lluvia", "¬Riego", "CalleMojada", "PastoMojado", "¬TierraHúmeda", "RosasOK")))
print(bn.belief_revision("RosasOK"))
print(bn.calculate(P("PastoMojado").given("RosasOK")))
