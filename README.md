# Ebook for Urdu poem: `kutay`

This is a technical approach to typesetting an Urdu poem for the Kindle.
The process is slightly involved since the objectives are strict:

- Use a proper Urdu font: Jameel Noori Nastaleeq
- The lines of the poem should have the same width (by stretching the content)

## Approach

The custom font needs to be bundled with the ebook.
We start with an epub and use Calibre + Kindle Previewing 3 to
convert to the KFX format.
The KFX format is the only one that supports ligatures from custom fonts without which
Urdu text using Jameel Noori Nastaleeq doesn't render correctly.

All features of CSS3 are **not** supported in KFX so
quite a few acrobatics are required to get the inter-word spacing to stretch so that
all lines take up equal width in totality.

## Stretching the liens of poetry

A brute-force approach (that doesn't work fully) is to first generate `poem.html`,
then preview it in the browser,
open the console (Developer Tools),
and run the `calculateStretch()` function.

The function will output additional stretch css which if included in `urdu.css` will
stretch out the words in the lines of poetry correctly.
Once the extra css has been copied and stored in the file `stretch.css`,
at the root level,
running `make epub` will copy the extra css over and generate the epub file.
