""" A simple two-node graph where a single product
serializes steps one and two.

Step1 --p-> Step2
"""

from bazaarci.runner import Graph, Product, Step

g = Graph("g")
p = Product("p")
s1 = Step("Step1", g, target=lambda: print("Step1"))
s2 = Step("Step2", g, target=lambda: print("Step2"))

s1.produces(p)  # Step 1 Produces p
s2.consumes(p)  # Step 2 Consumes p

g.start()  # Begin Thread Execution
