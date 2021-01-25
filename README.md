# mkdocs-typer

![Tests](https://github.com/bruce-szalwinski/mkdocs-typer/workflows/Tests/badge.svg?branch=main)
![Python versions](https://img.shields.io/pypi/pyversions/mkdocs-typer.svg)
[![Package version](https://badge.fury.io/py/mkdocs-typer.svg)](https://pypi.org/project/mkdocs-typer)

An MkDocs extension to generate documentation for Typer command line applications.

## Installation

Install from PyPI:

```bash
pip install mkdocs-typer
```

## Quickstart

Add `mkdocs-typer` to Markdown extensions in your `mkdocs.yml` configuration:

```yaml
site_name: Example
theme: readthedocs

markdown_extensions:
    - mkdocs-typer
```

Add a CLI application, e.g.:

```python
# app/cli.py
import typer


my_app = typer.Typer()


@my_app.command()
def foo():
    """do something fooey"""


@my_app.callback()
def cli():
    """
    Main entrypoint for this dummy program
    """
```

Add a `mkdocs-typer` block in your Markdown:

```markdown
# CLI Reference

This page provides documentation for our command line tools.

::: mkdocs-typer
    :module: app.cli
    :command: cli
```

Start the docs server:

```bash
mkdocs serve
```

Tada! 💫

![](https://raw.githubusercontent.com/bruce-szalwinski/mkdocs-typer/master/docs/example.png)

## Usage

### Documenting commands

To add documentation for a command, add a `mkdocs-typer` block where the documentation should be inserted.

Example:

```markdown
::: mkdocs-typer
    :module: app.cli
    :command: main
```

For all available options, see the [Block syntax](#block-syntax).

### Multi-command support

When pointed at a group (or any other multi-command), `mkdocs-typer` will also generate documentation for sub-commands.

This allows you to generate documentation for an entire CLI application by pointing `mkdocs-typer` at the root command.

### Tweaking header levels

By default, `mkdocs-typer` generates Markdown headers starting at `<h1>` for the root command section. This is generally what you want when the documentation should fill the entire page.

If you are inserting documentation within other Markdown content, you can set the `:depth:` option to tweak the initial header level. Note that this applies even if you are just adding a heading.

By default it is set to `0`, i.e. headers start at `<h1>`. If set to `1`, headers will start at `<h2>`, and so on. Note that if you insert your own first level heading and leave depth at its default value of 0, the page will have multiple `<h1>` tags, which is not compatible with themes that generate page-internal menus such as the ReadTheDocs and mkdocs-material themes.

## Reference

### Block syntax

The syntax for `mkdocs-typer` blocks is the following:

```markdown
::: mkdocs-typer
    :module: <MODULE>
    :command: <COMMAND>
    :prog_name: <PROG_NAME>
    :depth: <DEPTH>
```

Options:

- `module`: path to the module where the command object is located.
- `command`: name of the command object.
- `prog_name`: _(Optional, default: same as `command`)_ the name to display for the command.
- `depth`: _(Optional, default: `0`)_ Offset to add when generating headers.
