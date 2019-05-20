from functools import partial
from typing import Optional
import subprocess

from bazaarci.runner import Step


class SubprocessStep(Step):
    def __init__(self, name, graph: Optional["Graph"], *sp_args, **sp_kwargs):
        super().__init__(
            name,
            graph,
            target=partial(subprocess.run, *sp_args, **sp_kwargs),
        )
