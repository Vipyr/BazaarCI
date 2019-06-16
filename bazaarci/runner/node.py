from typing import Any, Optional, Set, Union


class Node:
    def __init__(self, name: str, graph: Optional["Graph"] = None):
        self.graph = graph
        self.name = name

    def produces(self, item: Union[None, str, "Product"] = None) -> Optional[Set["Product"]]:
        """ With no arguments, returns a `set` of all `Product`s this node produces.
            With an argument, adds the `Product` to it's produces set.
        """
        raise NotImplementedError(
            "Class `{}` has not implemented a `produces` method!".format(self.__class__.__name__)
        )

    def consumes(self, item: Union[None, str, "Product"] = None) -> Optional[Set["Product"]]:
        """ With no arguments, returns a `set` of all `Product`s this node consumes.
            With an argument, adds the `Product` to it's consumes set.
        """
        raise NotImplementedError(
            "Class `{}` has not implemented a `consumes` method!".format(self.__class__.__name__)
        )

    def start(self) -> None:
        """ Called in the main thread to create and start execution of new threads.
        """
        raise NotImplementedError(
            "Class `{}` has not implemented a `start` method!".format(self.__class__.__name__)
        )
