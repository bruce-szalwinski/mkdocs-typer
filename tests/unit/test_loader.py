# All rights reserved
# Licensed under the Apache license (see LICENSE)
from contextlib import nullcontext

import pytest

from mkdocs_typer._exceptions import MkDocsTyperException
from mkdocs_typer._loader import load_command


@pytest.mark.parametrize(
    "module, command, exc",
    [
        pytest.param("tests.app.cli", "my_app", None, id="ok"),
        pytest.param("tests.app.cli", "doesnotexist", MkDocsTyperException, id="command-does-not-exist"),
        pytest.param("doesnotexist", "cli", ImportError, id="module-does-not-exist"),
        pytest.param("tests.app.cli", "NOT_A_COMMAND", MkDocsTyperException, id="not-a-command"),
    ],
)
def test_load_command(module: str, command: str, exc):
    with pytest.raises(exc) if exc is not None else nullcontext():  # type: ignore
        load_command(module, command)
