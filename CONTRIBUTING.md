# Contributing guidelines

Thank you for being interested in contributing to this project! Here's how to get started.

## Setup

To start developing on this project, create a fork of this repository on GitHub, then clone your fork on your machine:

```bash
git clone https://github.com/<USERNAME>/mkdocs-typer
```

You can now install development dependencies using:

```bash
cd mkdocs-typer
scripts/install
```

## Example docs site

You can run the example docs site that lives in `example/` locally using:

```bash
scripts/docs serve
```

## Testing and linting

Once dependencies are installed, you can run the test suite using:

```bash
scripts/test
```

You can run code auto-formatting using:

```bash
scripts/format
```

To run style checks, use:

```bash
scripts/style
```

## Releasing

_This section is for maintainers._

Before releasing a new version, create a pull request with:

- An update to the changelog.
- A version bump: see `__version__.py`.

Merge the release PR, then create a release on GitHub. A tag will be created which will trigger a GitHub action to publish the new release to PyPI.
