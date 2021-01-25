# All rights reserved
# Licensed under the Apache license (see LICENSE)
import typer


app = typer.Typer()


@app.callback()
def bar():
    """The bar command"""
    pass


@app.command()
def hello(
    count: int = typer.Option(default=1, help="Number of greetings.", show_default=False),
    name: str = typer.Option(..., prompt="Your name", help="The person to greet."),
):
    """Simple program that greets NAME for a total of COUNT times."""
