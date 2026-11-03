#!/usr/bin/fontforge

import sys
import json

font = fontforge.open(sys.argv[1])
config = json.load(open(sys.argv[2], "r"))

# load size from config
size = config["size"]
print(f"Size: {size}")

# set ascent and descent if specified in config
if "ascent" in config:
	font.ascent = config["ascent"]
if "descent" in config:
	font.descent = config["descent"]
print(f"Ascent: {font.ascent}")
print(f"Descent: {font.descent}")

font.selection.all()

# generate bitmap strike
# handle fontforge nested tuple bug
try:
	font.bitmapSizes = ((size,),)
except (TypeError, SystemError):
	font.bitmapSizes = (size,)
font.regenBitmaps((size,))

# initial cleanup, for TTF
font.correctDirection()
font.addExtrema()
font.unlinkReferences()

# convert to quadratic bezier, used by TTF
font.layers["Fore"].is_quadratic = True

# initial autohint
font.autoHint()

# guess PS private fields
private_fields = [
	"BlueValues", 
	"OtherBlues", 
	"StdHW", 
	"StdVW", 
	"StemSnapH", 
	"StemSnapV"
]
for field in private_fields:
	font.private.guess(field)

# autohint with refined PS guesses
font.autoHint()

# TTF auto-instruct
font.autoInstr()

# generate TTF
font.generate(sys.argv[1][:-3] + "ttf", bitmap_type="ttf")
#font.generate(sys.argv[1][:-3] + "otf")
#font.save("tmp.sfd")
