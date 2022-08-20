/*
 * The purpose is to calculate the inter-word spacing per line of poetry so that
 * the lines end up lining up at the end.
 */

function calculateStretch() {
    const sections = document.getElementsByClassName("section");
    console.log(`Number of sections: ${sections.length}`);

    for (let i = 0; i < sections.length; i++) {
        const section = sections[i];

        const lines = section.getElementsByClassName("stretch");

        for (let j = 0; j < lines.length; j++) {
            console.log(`Line id: ${i}.${j}`);
        }
    }
}
