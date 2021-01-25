# All rights reserved
# Licensed under the Apache license (see LICENSE)
from typing import Any, List, Iterator

from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor

from ._docs import make_command_docs
from ._exceptions import MkDocsTyperException
from ._loader import load_command
from ._processing import replace_blocks


def replace_command_docs(**options: Any) -> Iterator[str]:
    for option in ("module", "command"):
        if option not in options:
            raise MkDocsTyperException(f"Option {option!r} is required")

    module = options["module"]
    command = options["command"]
    prog_name = options.get("prog_name", command)
    depth = int(options.get("depth", 0))

    command_obj = load_command(module, command)

    return make_command_docs(prog_name=prog_name, command=command_obj, level=depth)


class TyperProcessor(Preprocessor):
    def run(self, lines: List[str]) -> List[str]:
        return list(replace_blocks(lines, title="mkdocs-typer", replace=replace_command_docs))


class MKTyperExtension(Extension):
    """
    Replace blocks like the following:

    ::: mkdocs-typer
        :module: example.main
        :command: app

    by Markdown documentation generated from the specified Typer application.
    """

    def extendMarkdown(self, md: Any) -> None:
        md.registerExtension(self)
        processor = TyperProcessor(md.parser)
        md.preprocessors.register(processor, "mk_typer", 142)


def makeExtension() -> Extension:
    return MKTyperExtension()
