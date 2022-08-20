"""Inject poem data into template to create epub source."""


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


def main():
    """Entrypoint for script."""
    data = get_data()
    print(data)


if "__main__" in __name__:
    main()
