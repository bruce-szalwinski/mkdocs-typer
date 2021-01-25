# All rights reserved
# Licensed under the Apache license (see LICENSE)
from textwrap import dedent

import typer

from mkdocs_typer._docs import make_command_docs


app = typer.Typer(add_completion=False)


@app.command()
def hello(debug: bool = typer.Option(False, "--debug/--no-debug", "-d", help="Include debug output")):
    """Hello, world!"""


HELLO_EXPECTED = dedent(
    """
    # hello

    Hello, world!

    Usage:

    ```
    hello [OPTIONS]
    ```

    Options:

    ```
      -d, --debug / --no-debug  Include debug output  [default: False]
    ```

    """
).strip()


def test_make_command_docs():
    output = "\n".join(make_command_docs("hello", app)).strip()
    assert output == HELLO_EXPECTED


def test_depth():
    output = "\n".join(make_command_docs("hello", app, level=2)).strip()
    assert output == HELLO_EXPECTED.replace("# ", "### ")


def test_prog_name():
    output = "\n".join(make_command_docs("hello-world", app)).strip()
    assert output == HELLO_EXPECTED.replace("# hello", "# hello-world")
