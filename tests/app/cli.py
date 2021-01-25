# All rights reserved
# Licensed under the Apache license (see LICENSE)
import typer

from tests.app import bar

my_app = typer.Typer(add_completion=False)
my_app.add_typer(bar.app, name="bar")


@my_app.command()
def foo():
    pass


@my_app.callback()
def cli():
    """
    Main entrypoint for this dummy program
    """
    pass


if __name__ == "__main__":
    my_app()
