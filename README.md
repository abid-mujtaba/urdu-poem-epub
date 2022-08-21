# Ebook for Urdu poem: `kutay`

This is a technical approach to typesetting an Urdu poem for the Kindle.
The process is slightly involved since the objectives are strict:

1. Use a proper Urdu font: Jameel Noori Nastaleeq
2. The lines of the poem should have the same width (by stretching the content)

Unfortunately the second objective is currently unachievable on the Kindle,
specifically the KFX format,
because it doesn't support all of the feature of CSS-3.

## Approach

The custom font needs to be bundled with the ebook.
We start with an epub and use Calibre + Kindle Previewing 3 to
convert to the KFX format.
The KFX format is the only one that supports ligatures from custom fonts without which
Urdu text using Jameel Noori Nastaleeq doesn't render correctly.

## Template and Scripting

This project is setup with a template and a Python script that
reads the poem data from a yaml file and
injects the information into the template to
create all of the files required for a complete epub.

## Local Development

The project includes a `Makefile` with inter-dependent targets that will
generate the epub for you.
Additionally, one can run `make preview`, and point their browser to
`http://localhost:8000` to preview the output.

*Note:* Since KFX doesn't support all CSS-3 features (particularly `flex`)
the preview will not match the KFX output but
is fairly representative of the epub output.
