# OpenTTD Mono
OpenTTD Mono is a heavy regular monospaced typeface designed for medium-sized text in a pixel art style.

OpenTTD Mono is derived from OpenTTD Sans, adjusted to a 7 pixel width (including bearings). Letters generally have a 6 pixel width, with a 1 pixel right bearing.

Verticals are generally 2 pixel wide and horizontals 1 pixel, like OpenTTD sans, but adjusted to fit in the target character width. Verticals are essentially all at least 1 pixel wide.

## Unicode coverage
OpenTTD Sans uses Unicode basic multilingual plane encoding.

Full coverage:
* Basic Latin (`U+0000..U+007F`)
* Latin-1 Supplement (`U+0080..U+00FF`)
* Latin Extended-A (`U+0100..U+017F`)
* Currency Symbols (`U+20A0..U+20CF`)

Targeted coverage:
* Greek and Coptic (`U+0384..U+03D7`) [contempary Greek only `U+0370..U+03FF`]
* Greek and Coptic (`U+0400..U+04FF`) [contempary Ukrainian, Russian and Belarusian `U+0400..U+045F`, with a few extra]
* Hebrew (`U+0590..U+05FF`) [Hebrew alphabet/abjad only `U+05D0..U05EA`, with a few extra]

Partial coverage:
* IPA Extensions (`U+0250–U+02AF`)
* Combining Diacritical Marks (`U+0300–U+036F`)
These ranges provide glyphs which are combined to build the full coverage core set.

Plus a few additional glyphs - stray small caps and glyphs of particular use in OpenTTD.

## Features
OpenTTD Mono is designed with the creation of standalone bitmap strikes in mind, for example for generation of an image/sprite-based font.

When used as a vector font, it comes with select improvements:
* Character pair kerning

## Technical details
SVG glyphs are drawn in Inkscape, for manual import into FontForge. Source SVGs, occasionally containing source paths pre-union, are included for convenience.

In FontForge, glyphs are composed from referenced copies wherever possible. Majuscule diacritics are generally placed on a "small caps" letter variant.

### Glyph units
SVGs are prepared at 1 pixel = 1 unit
* height: 1200 units
* width: 600 units (with a few exceptions at 700, or in extreme 800)
* baseline offset: 200 units
* x height: 600 units
* ascender: 100 units
* ascent: 900 units
* descender: 200 units
* overshoot: 0 units
The top 100 units are always empty. During TTF generation from the FontForge SFD file, height is set to 1000.

Bearings are optimised for pixel-perfect rendering:
* left bearing: 0 units
* right bearing: 200 units
Bearings are expanded symmetrically within this, eg. L 100, R 300; L 200, R 400, etc.

Diacritics are similarly positioned in steps of 100 units. They are, however, always well-centred due to the monospaced nature of the face.

This is designed for rendering at 10 pixel height:
* line height: 10 pixel
* baseline offset: 2 pixel
* x height: 6 pixel
* ascender: 1 pixel
* ascent: 9 pixel
* descender: 2 pixel

Diacritics are highly compressed to fit within the 10 pixel height.

### Glyph style
Glyphs are derived from OpenTTD Sans. In general:
* Upper case letters are narrowed to 600 unit with 200 unit verticals
* Lower case letters are widened to 600 unit with 200 unit verticals
* Wide letters (at least 3 verticals, like m) are fitted to 700 units, with ~150 unit verticals
* Very wide glyphs are adjusted more significantly with minimum 100 unit verticals

### Building
Run `build.sh` to build the output TTD and OTF files.

The master source file is the FontForge SFD file. SVG files are not automatically imported.
