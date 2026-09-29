#!/usr/bin/fontforge

import sys
import json

font = fontforge.open(sys.argv[1])
config = json.load(open(sys.argv[2], "r"))

if "ascent" in config:
	font.ascent = config["ascent"]
if "descent" in config:
	font.descent = config["descent"]
print(f"Ascent: {font.ascent}")
print(f"Descent: {font.descent}")

font.selection.all()

# initial cleanup
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

font.generate(sys.argv[1][:-3] + "ttf")
#font.generate(sys.argv[1][:-3] + "otf")
#font.save("tmp.sfd")
