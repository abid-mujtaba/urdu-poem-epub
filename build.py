"""Inject poem data into template to create epub source."""


from jinja2 import Environment, FileSystemLoader
from pathlib import Path
from ruyaml import YAML


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


def inject_toc_html(title: str):
    """Inject title to create toc.html file."""
    loader = FileSystemLoader(searchpath="template/OEBPS")
    env = Environment(loader=loader)
    template = env.get_template("toc.html.template")

    content = template.render(title=title)

    Path("build/OEBPS/toc.html").write_text(content)


def main():
    """Entrypoint for script."""
    data = get_data()

    inject_toc_html(title=data["title"])


if "__main__" in __name__:
    main()
