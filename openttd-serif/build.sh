#!/bin/bash

# generate ttf from fontforge sfd
fontforge ../build_font.py OpenTTD-Serif.sfd config.json

# generate previews
python3 font_preview.py
