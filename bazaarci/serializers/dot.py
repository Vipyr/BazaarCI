from bazaarci.runner import Graph, Node, Product, Step, SubprocessStep

def graph_to_dot(graph):
    all_step_statements = "\n".join(step.to_dot() for step in graph)
    if graph.graph is None:  # if this is the top-level graph
        return f"digraph \"{graph.name}\" {{ compound=true; rankdir=LR; {all_step_statements} }}"
    else:  # this is a subgraph
        return f"subgraph \"{graph.name}\" {{ {all_step_statements} }}"

def step_to_dot(step):
    if step.thread is None:
        # thread not yet created
        color = "gray"
    elif step.thread.is_alive():
        if any(not consumed.is_set() for consumed in step.consumes()):
            # thread created but blocked
            color = "yellow"
        else:
            # thread created, not blocked
            color = "aqua"
    else:
        # thread exited
        color = "blue"
    this_node = f"\"{step.name}\" [shape=box style=filled color={color}];"
    all_consumed = (f"\"{cons.name}\" -> \"{step.name}\";" for cons in step.consumes())
    all_produced = (f"\"{step.name}\" -> \"{prod.name}\";" for prod in step.produces())
    return this_node \
            + "\n" + "\n".join(all_consumed) \
            + "\n" + "\n".join(all_produced) \
            + "\n" + "\n".join((p.to_dot() for p in step.produces())) \
            + "\n" + "\n".join((c.to_dot() for c in step.consumes()))

def subprocess_step_to_dot(step):
    if step.output is None:
        if step.thread is None:
            # thread not yet created
            step.color = "gray"
        elif step.thread.is_alive():
            if any(not consumed.is_set() for consumed in step.consumes()):
                # thread created but blocked
                color = "yellow"
            else:
                # thread created, not blocked
                color = "aqua"
        else:
            # thread exited
            step.color = "blue"
    else:
        rc = step.output.returncode
        if rc == 0:
            # subprocess returned zero
            color = "green"
        else:
            # subprocess returned non-zero
            color = "red"
    this_node = f"\"{step.name}\" [shape=box style=filled color={color}];"
    all_consumed = (f"\"{cons.name}\" -> \"{step.name}\";" for cons in step.consumes())
    all_produced = (f"\"{step.name}\" -> \"{prod.name}\";" for prod in step.produces())
    return this_node \
            + "\n" + "\n".join(all_consumed) \
            + "\n" + "\n".join(all_produced) \
            + "\n" + "\n".join((p.to_dot() for p in step.produces())) \
            + "\n" + "\n".join((c.to_dot() for c in step.consumes()))

def product_to_dot(product):
    color = "green" if product.is_set() else "yellow"
    return f"\"{product.name}\" [style=filled color={color}]"


def initialize():
    apply_serializer(Graph, "to_dot", graph_to_dot)
    apply_serializer(Step, "to_dot", step_to_dot)
    apply_serializer(SubprocessStep, "to_dot", subprocess_step_to_dot)
    apply_serializer(Product, "to_dot", product_to_dot)
