"""Inject poem data into template to create epub source."""


from typing import List
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from ruyaml import YAML


BUILD_PATH = Path("build/OEBPS")


def get_data():
    """Get data from poem.yaml and validate it."""
    yaml = YAML(typ="safe")

    with open("poem.yaml") as fin:
        data = yaml.load(fin)

    # Validate data
    assert "title" in data
    assert "author" in data
    assert "poem" in data

    assert isinstance(data["poem"], list)

    for section in data["poem"]:
        assert isinstance(section, list)

        for line in section:
            assert isinstance(line, str)

    return data


def jinja2_env():
    """Create jinja2 env that can find templates under template/OEBPS."""
    loader = FileSystemLoader(searchpath="template/OEBPS")
    return Environment(loader=loader)


def inject_toc_html(title: str):
    """Inject title to create toc.html file."""
    env = jinja2_env()
    template = env.get_template("toc.html.template")

    content = template.render(title=title)

    file = BUILD_PATH / "toc.html"
    file.write_text(content)


def inject_toc_ncx(title: str, author: str):
    """Inject title and author to create tox.ncs file."""
    env = jinja2_env()
    template = env.get_template("toc.ncx.template")

    content = template.render(title=title, author=author)

    file = BUILD_PATH / "toc.ncx"
    file.write_text(content)


def process_line(line: str) -> str:
    """
    Process each line of the poem into HTML output.

    Split line into words based on whitespace.
    Surround each word with <span> tags.
    Concatenate all of them to create output line.

    Note: A space must be added after every word for the Urdu ligatures to be
          correctly rendered.
    """
    return "".join(f"<span>{word} </span>" for word in line.split())


def inject_poem_html(title: str, author: str, poem: List[List[str]]):
    """Inject the complete data into poem.html."""
    env = jinja2_env()
    template = env.get_template("poem.html.template")

    sections = [[process_line(line) for line in section] for section in poem]

    content = template.render(title=title, author=author, sections=sections)

    file = BUILD_PATH / "poem.html"
    file.write_text(content)


def main():
    """Entrypoint for script."""
    data = get_data()

    title = data["title"]
    author = data["author"]
    poem = data["poem"]

    inject_toc_html(title=title)
    inject_toc_ncx(title=title, author=author)
    inject_poem_html(title=title, author=author, poem=poem)


if "__main__" in __name__:
    main()
