# All rights reserved
# Licensed under the Apache license (see LICENSE)
from typing import Iterator, List, Optional

import typer
import click
from typer.main import get_command

from ._exceptions import MkDocsTyperException


def make_command_docs(prog_name: str, command: typer.main.Typer, level: int = 0) -> Iterator[str]:
    """Create the Markdown lines for a command and its sub-commands."""
    cmd = get_command(command)
    for line in _recursively_make_command_docs(prog_name, cmd, level=level):
        yield line.replace("\b", "")


def _recursively_make_command_docs(
    prog_name: str, command: click.Command, parent: typer.Context = None, level: int = 0
) -> Iterator[str]:
    """Create the raw Markdown lines for a command and its sub-commands."""
    ctx = typer.Context(command, parent=parent)

    yield from _make_title(prog_name, level)
    yield from _make_description(ctx)
    yield from _make_usage(ctx)
    yield from _make_options(ctx)

    subcommands = _get_sub_commands(ctx.command, ctx)

    for command in sorted(subcommands, key=lambda cmd: cmd.name):
        yield from _recursively_make_command_docs(command.name, command, parent=ctx, level=level + 1)


def _get_sub_commands(command: click.Command, ctx: typer.Context) -> List[click.Command]:
    """Return subcommands of a Typer command."""
    subcommands = getattr(command, "commands", {})
    if subcommands:
        return subcommands.values()
    else:
        # MultiCommand not created by Typer.
        # See https://github.com/DataDog/mkdocs-click/blob/master/mkdocs_click/_docs.py#L45

        return []


def _make_title(prog_name: str, level: int) -> Iterator[str]:
    """Create the first markdown lines describing a command."""
    yield _make_header(prog_name, level)
    yield ""


def _make_header(text: str, level: int) -> str:
    """Create a markdown header at a given level"""
    return f"{'#' * (level + 1)} {text}"


def _make_description(ctx: click.Context) -> Iterator[str]:
    """Create markdown lines based on the command's own description."""
    help_string = ctx.command.help or ctx.command.short_help

    if help_string:
        yield from help_string.splitlines()
        yield ""


def _make_usage(ctx: click.Context) -> Iterator[str]:
    """Create the Markdown lines from the command usage string."""

    # Gets the usual 'Usage' string without the prefix.
    formatter = ctx.make_formatter()
    pieces = ctx.command.collect_usage_pieces(ctx)
    formatter.write_usage(ctx.command_path, " ".join(pieces), prefix="")
    usage = formatter.getvalue().rstrip("\n")

    # Generate the full usage string based on parents if any, i.e. `root sub1 sub2 ...`.
    full_path = []
    current: Optional[click.Context] = ctx
    while current is not None:
        name = current.command.name
        if name is None:
            raise MkDocsTyperException(f"command {current.command} has no `name`")
        full_path.append(name)
        current = current.parent

    full_path.reverse()
    usage_snippet = " ".join(full_path) + usage

    yield "Usage:"
    yield ""
    yield "```"
    yield usage_snippet
    yield "```"
    yield ""


def _make_options(ctx: typer.Context) -> Iterator[str]:
    """Create the Markdown lines describing the options for the command."""
    formatter = ctx.make_formatter()
    click.Command.format_options(ctx.command, ctx, formatter)
    # First line is redundant "Options"
    # Last line is `--help`
    option_lines = formatter.getvalue().splitlines()[1:-1]
    if not option_lines:
        return

    yield "Options:"
    yield ""
    yield "```"
    yield from option_lines
    yield "```"
    yield ""
