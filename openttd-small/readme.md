# OpenTTD Small
OpenTTD Small is a specialised typeface designed for very small text in a pixel art style. Drawn to broadly capture the look and feel of the small pixel font in Transport Tycoon Deluxe.

The glyphs are designed with a pixel art aesthetic, with most fitted to a 3 by 6 pixel glyph size. Pixel-perfect appearance when rendered at a height of 6 pixel (or multiples thereof).

## Unicode coverage
OpenTTD Small uses Unicode basic multilingual plane encoding.

Full coverage:
* Basic Latin (`U+0000..U+007F`)
* Latin-1 Supplement (`U+0080..U+00FF`)
* Latin Extended-A (`U+0100..U+017F`)
* Currency Symbols (`U+20A0..U+20CF`)

Targeted coverage:
* General Punctuation (`U+2000..U+206F`)
* Greek and Coptic (`U+0384..U+03D7`) [contempary Greek only `U+0370..U+03FF`]
* Greek and Coptic (`U+0400..U+04FF`) [contempary Ukrainian, Russian and Belarusian `U+0400..U+045F`, with a few extra]
* Hebrew (`U+0590..U+05FF`) [Hebrew alphabet/abjad only `U+05D0..U05EA`, with a few extra]

Partial coverage:
* IPA Extensions (`U+0250–U+02AF`)
* Combining Diacritical Marks (`U+0300–U+036F`)
These ranges provide glyphs which are combined to build the full coverage core set.

Plus a few additional glyphs - stray small caps and glyphs of particular use in OpenTTD.

## Features
OpenTTD Small is designed with the creation of standalone bitmap strikes in mind, for example for generation of an image/sprite-based font.

When used as a vector font, it comes with select improvements:
* Character pair kerning

## Technical details
SVG glyphs are drawn in Inkscape, for manual import into FontForge. Source SVGs, occasionally containing source paths pre-union, are included for convenience.

In FontForge, glyphs are composed from referenced copies wherever possible. Majuscule diacritics are generally placed on a "small caps" letter variant.

### Glyph units
SVGs are prepared at 1 pixel = 1 unit
* height: 800 units
* baseline offset: 200 units
* x height: 400 units
* ascender: 100 units
* ascent: 600 units
* descender: 100 units
* overshoot: 0 units
The top and bottom 100 units are always empty. During TTF generation from the FontForge SFD file, height is set to 600 and descent to 0.

Glyphs are almost always, unless necessary for uniqueness:
* width: 300 units
* height: 500 units

Bearings are optimised for pixel-perfect rendering:
* left bearing: 0 units
* right bearing: 100 units
And, kerning adjusts spacing in steps of 100 units.

Diacritics are similarly positioned in steps of 100 units.

This is designed for rendering at 6 pixel height:
* line height: 7 pixel
* baseline offset: 1 pixel
* x height: 4 pixel
* ascender: 1 pixel
* ascent: 6 pixel
* descender: 1 pixel

The recommended line height of 7 pixel is the same as the potential glyph height of 7 pixel. It is intended for diacritics to overflow out of the top of the 6 px nominal glyph height.

### Building
Run `build.sh` to build the output TTD and OTF files.

The master source file is the FontForge SFD file. SVG files are not automatically imported.
