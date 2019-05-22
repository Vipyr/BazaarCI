from bazaarci.runner import Graph, Step

g = Graph("g")
s1 = Step("Step1", g, target=lambda: print("Step1"))
s2 = Step("Step2", g, target=lambda: print("Step2"))

s1.produces("p")  # Step 1 Produces "p"
s2.consumes("p")  # Step 2 Consumes "p"

g.start()  # Begin Thread Execution
