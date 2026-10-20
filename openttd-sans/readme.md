# OpenTTD Sans
OpenTTD Sans is a heavy regular typeface designed for medium-sized text in a pixel art style. Drawn to broadly capture the look and feel of the medium pixel font in Transport Tycoon Deluxe.

The glyphs are designed with a pixel art aesthetic, heavily aligned to a pixel grid but with some flourishes for character. Pixel-perfect appearance when rendered at a height of 10 pixel (or multiples thereof).

The small ascender height and heavy weight give a dense, compact feel. This is enhanced by the peculiarity of majuscules with diacritics being compressed to fit the diacritic within the ascender space.

## Unicode coverage
OpenTTD Sans uses Unicode basic multilingual plane encoding.

Full coverage:
* Basic Latin (`U+0000..U+007F`)
* Latin-1 Supplement (`U+0080..U+00FF`)
* Latin Extended-A (`U+0100..U+017F`)
* Currency Symbols (`U+20A0..U+20CF`)

Targeted coverage:
* General Punctuation (`U+2000..U+206F`)
* Greek and Coptic (`U+0384..U+03D7`) [contempary Greek only `U+0370..U+03FF`]
* Cyrillic (`U+0400..U+04FF`) [contempary Ukrainian, Russian and Belarusian `U+0400..U+045F`, with a few extra]
* Hebrew (`U+0590..U+05FF`) [Hebrew alphabet/abjad only `U+05D0..U05EA`, with a few extra]

Partial coverage:
* IPA Extensions (`U+0250–U+02AF`)
* Combining Diacritical Marks (`U+0300–U+036F`)
These ranges provide glyphs which are combined to build the full coverage core set.

Plus a few additional glyphs - stray small caps and glyphs of particular use in OpenTTD.

## Features
OpenTTD Sans is designed with the creation of standalone bitmap strikes in mind, for example for generation of an image/sprite-based font.
This comes with some pixel "charm", like some unusual character spacing and off-centre diacritics.

When used as a vector font, it comes with key improvements:
* Character pair kerning
* Select ligatures/contextual alternates
* Combining diacritics for basic Latin and Cyrillic alphabets
* Tabular numerals and normal lining numerals as an alternate

Provides tabular numerals, and proportional numerals (matching the TTD style) as an alternate.

## Technical details
SVG glyphs are drawn in Inkscape, for manual import into FontForge. Source SVGs, occasionally containing source paths pre-union, are included for convenience.

In FontForge, glyphs are composed from referenced copies wherever possible. Majuscule diacritics are generally placed on a "small caps" letter variant.

### Glyph units
SVGs are prepared at 1 pixel = 1 unit
* height: 1200 units
* baseline offset: 200 units
* x height: 600 units
* ascender: 100 units
* ascent: 900 units
* descender: 200 units
* overshoot: 0 units
The top 100 units are always empty. During TTF generation from the FontForge SFD file, height is set to 1000.

Bearings are optimised for pixel-perfect rendering:
* left bearing: 0 units
* right bearing: 100 units
And, kerning adjusts spacing in steps of 100 units.

Diacritics are similarly positioned in steps of 100 units. This can lead to them being off-centre.

This is designed for rendering at 10 pixel height:
* line height: 10 pixel
* baseline offset: 2 pixel
* x height: 6 pixel
* ascender: 1 pixel
* ascent: 9 pixel
* descender: 2 pixel

Diacritics are highly compressed to fit within the 10 pixel height.

### Building
Run `build.sh` to build the output TTD and OTF files.

The master source file is the FontForge SFD file. SVG files are not automatically imported.
