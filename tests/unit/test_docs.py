# All rights reserved
# Licensed under the Apache license (see LICENSE)
from textwrap import dedent

import typer
import pytest

from mkdocs_typer._docs import make_command_docs
from mkdocs_typer._exceptions import MkDocsTyperException


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


# TODO: multicommaands
# class MultiCLI(click.MultiCommand):
#     def list_commands(self, ctx):
#         return ["single-command"]
#
#     def get_command(self, ctx, name):
#         return hello
#
#
# def test_custom_multicommand():
#     """
#     Custom `MultiCommand` objects are supported (i.e. not just `Group` multi-commands).
#     """
#
#     multi = MultiCLI("multi", help="Multi help")
#
#     expected = dedent(
#         """
#         # multi
#
#         Multi help
#
#         Usage:
#
#         ```
#         multi [OPTIONS] COMMAND [ARGS]...
#         ```
#
#         ## hello
#
#         Hello, world!
#
#         Usage:
#
#         ```
#         multi hello [OPTIONS]
#         ```
#
#         Options:
#
#         ```
#           -d, --debug TEXT  Include debug output
#         ```
#         """
#     ).lstrip()
#
#     output = "\n".join(make_command_docs("multi", multi))
#     assert output == expected
#
#
# def test_custom_multicommand_name():
#     """Custom multi commands must be given a name."""
#     multi = MultiCLI()
#     with pytest.raises(MkDocsTyperException):
#         list(make_command_docs("multi", multi))
