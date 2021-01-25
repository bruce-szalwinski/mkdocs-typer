# All rights reserved
# Licensed under the Apache license (see LICENSE)
import importlib
from typing import Any

import typer
from ._exceptions import MkDocsTyperException


def load_command(module: str, attribute: str) -> typer.main.Typer:
    """
    Load and return the Typer object located at '<module>:<attribute>'.
    """
    command = _load_obj(module, attribute)

    if not isinstance(command, typer.main.Typer):
        raise MkDocsTyperException(f"{attribute!r} must be a 'typer.main.Typer' object, got {type(command)}")

    return command


def _load_obj(module: str, attribute: str) -> Any:
    try:
        mod = importlib.import_module(module)
    except SystemExit:
        raise MkDocsTyperException("the module appeared to call sys.exit()")  # pragma: no cover

    try:
        return getattr(mod, attribute)
    except AttributeError:
        raise MkDocsTyperException(f"Module {module!r} has no attribute {attribute!r}")
