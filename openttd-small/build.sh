#!/bin/bash

# generate otf from fontforge sfd
fontforge ../build_font.py OpenTTD-Small.sfd config.json
fontforge ../build_font.py OpenTTD-SmallCaps.sfd config.json

# generate previews
python3 font_preview.py OpenTTD-Small
python3 font_preview.py OpenTTD-SmallCaps
