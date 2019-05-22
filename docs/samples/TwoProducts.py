""" A simple three-node graph where two products
serialize the steps

Step1 --p1-> Step2 --p2-> Step3
         \_______________/
"""

from bazaarci.runner import Graph, Product, Step

g = Graph("g")
p1 = Product("p1")
p2 = Product("p2")
s1 = Step("Step1", g, target=lambda: print("Step1"))
s2 = Step("Step2", g, target=lambda: print("Step2"))
s3 = Step("Step3", g, target=lambda: print("Step3"))

s1.produces(p1)  # Step 1 Produces p1
s2.consumes(p1)  # Step 2 Consumes p1
s2.produces(p2)  # Step 2 Produces p2
s3.consumes(p1)  # Step 3 Consumes p1 and p2
s3.consumes(p2)  # Step 3 Consumes p1 and p2

g.start()  # Begin Thread Execution
