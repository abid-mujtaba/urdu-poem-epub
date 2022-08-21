/*
 * The purpose is to calculate the inter-word spacing per line of poetry so that
 * the lines end up lining up at the end.
 */

function calculateStretch() {
    const sections = document.getElementsByClassName("section");

    // Calculate the position of the end of the section (on the left for Urdu)
    const sectionEnd = sections[0].getBoundingClientRect().left;
    let output = "";

    for (let i = 0; i < sections.length; i++) {
        const section = sections[i];

        const lines = section.getElementsByClassName("stretch");

        for (let j = 0; j < lines.length; j++) {
            // Let us calculate the position of the end of the line
            const spans = lines[j].getElementsByTagName("span");
            const last = spans[spans.length - 1];
            const end = last.getBoundingClientRect().left;

            const lineGap = end - sectionEnd;

            // Divide the line gap per word and convert to em
            const wordGap = pixelsToEm(spans[0], lineGap / (spans.length - 1));

            output = output.concat(`\ndiv[id="${i}-${j}"].stretch>span.gap { margin-left: ${wordGap}em; }`)
        }
    }

    console.log(output);
}


function pixelsToEm(element, pixels) {
    // 1 em in pixels is equal to the fontSize of the element so first calculate that
    const fontSize = parseFloat(getComputedStyle(element).fontSize);
    return pixels / fontSize;
}
