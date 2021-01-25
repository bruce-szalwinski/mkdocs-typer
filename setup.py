# Licensed under the Apache license (see LICENSE)
import re
from pathlib import Path
from setuptools import setup


def get_version(package: str) -> str:
    text = Path(package, "__version__.py").read_text()
    match = re.search('__version__ = "([^"]+)"', text)
    assert match is not None
    return match.group(1)


def get_long_description() -> str:
    readme = Path("README.md").read_text()
    changelog = Path("CHANGELOG.md").read_text()
    return f"{readme}\n\n{changelog}"


setup(
    name="mkdocs_typer",
    version=get_version("mkdocs_typer"),
    description="An MkDocs extension to generate documentation for Typer command line applications",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    keywords="mkdocs typer",
    url="https://github.com/bruce-szalwinski/mkdocs-typer",
    author="Bruce Szalwinski",
    author_email="bruce.szalwinski@gmail.com",
    license="Apache",
    packages=["mkdocs_typer"],
    install_requires=["typer==0.*", "markdown==3.*"],
    python_requires=">=3.7",
    include_package_data=True,
    zip_safe=False,
    entry_points={"markdown.extensions": ["mkdocs-typer = mkdocs_typer:MKTyperExtension"]},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ]
)
