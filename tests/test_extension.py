# All rights reserved
# Licensed under the Apache license (see LICENSE)
from pathlib import Path
from textwrap import dedent

import pytest
from markdown import Markdown

import mkdocs_typer

EXPECTED = (Path(__file__).parent / "app" / "expected.md").read_text()


def test_extension():
    """
    Markdown output for a relatively complex Typer application is correct.
    """
    md = Markdown(extensions=[mkdocs_typer.makeExtension()])

    source = dedent(
        """
        ::: mkdocs-typer
            :module: tests.app.cli
            :command: my_app
        """
    )

    assert md.convert(source) == md.convert(EXPECTED)


def test_prog_name():
    """
    The :prog_name: attribute determines the name to display for the command.
    """
    md = Markdown(extensions=[mkdocs_typer.makeExtension()])

    source = dedent(
        """
        ::: mkdocs-typer
            :module: tests.app.cli
            :command: my_app
            :prog_name: custom
        """
    )

    expected = EXPECTED.replace("# my_app", "# custom")

    assert md.convert(source) == md.convert(expected)


def test_depth():
    """
    The :depth: attribute increases the level of headers.
    """
    md = Markdown(extensions=[mkdocs_typer.makeExtension()])

    source = dedent(
        """
        # CLI Reference

        ::: mkdocs-typer
            :module: tests.app.cli
            :command: my_app
            :depth: 1
        """
    )

    expected = f"# CLI Reference\n\n{EXPECTED.replace('# ', '## ')}"

    assert md.convert(source) == md.convert(expected)


@pytest.mark.parametrize("option", ["module", "command"])
def test_required_options(option):
    """
    The module and command options are required.
    """
    md = Markdown(extensions=[mkdocs_typer.makeExtension()])

    source = dedent(
        """
        ::: mkdocs-typer
            :module: tests.app.cli
            :command: my_app
        """
    )

    source = source.replace(f":{option}:", ":somethingelse:")

    with pytest.raises(mkdocs_typer.MkDocsTyperException):
        md.convert(source)
