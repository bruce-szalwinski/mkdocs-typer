# All rights reserved
# Licensed under the Apache license (see LICENSE)
from textwrap import dedent

import typer

from mkdocs_typer._docs import make_command_docs


app = typer.Typer(add_completion=False)


@app.command()
def hello(debug: bool = typer.Option(False, "--debug/--no-debug", "-d", help="Include debug output")):
    """Hello, world!"""


@app.command()
def goodbye(debug: bool = typer.Option(False, "--debug/--no-debug", "-d", help="Include debug output")):
    """Goodbye, world!"""


GOODBYE_DOCS = dedent(
    """
    ## goodbye

    Goodbye, world!

    Usage:

    ```
     goodbye [OPTIONS]
    ```

    Options:

    ```
      -d, --debug / --no-debug  Include debug output  [default: no-debug]
    ```
    """
).strip()


HELLO_DOCS = dedent(
    """
    ## hello

    Hello, world!

    Usage:

    ```
     hello [OPTIONS]
    ```

    Options:

    ```
      -d, --debug / --no-debug  Include debug output  [default: no-debug]
    ```
    """
).strip()


EXPECTED_FORMAT = dedent(
    """
    # hello

    Usage:

    ```
     [OPTIONS] COMMAND [ARGS]...
    ```

    {first}

    {second}
    """
).strip()


HELLO_EXPECTED = EXPECTED_FORMAT.format(first=GOODBYE_DOCS, second=HELLO_DOCS)


def test_make_command_docs():
    output = "\n".join(make_command_docs("hello", app)).strip()
    assert output == HELLO_EXPECTED


def test_depth():
    output = "\n".join(make_command_docs("hello", app, level=2)).strip()
    assert output == HELLO_EXPECTED.replace("# ", "### ")


def test_prog_name():
    output = "\n".join(make_command_docs("hello-world", app)).strip()
    assert output == HELLO_EXPECTED.replace("# hello", "# hello-world", 1)

