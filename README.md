# Bazaar CI


## Backend - bazaar

A simple example, two steps where the first step produces a product `p` that is consumed by the second step.

```python
from bazaar import Graph, Step, Product

g = Graph()
p = Product("p")
s1 = Step(g, "Step1", target=lambda: print("Step1"))
s2 = Step(g, "Step2", target=lambda: print("Step2"))

s1.produces.add(p)
s2.consumes.add(p)
```

## Frontend - bazaarci

