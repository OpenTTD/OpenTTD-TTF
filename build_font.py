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
font.unlinkReferences()
font.correctDirection()
font.addExtrema()

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

# convert to quadratic bezier for TTF
font.layers["Fore"].is_quadratic = True

def is_on_grid(hint, grid=100, tol=0.5):
	start, width = hint
	return (
		min(start % grid, grid - (start % grid)) <= tol
		and min(width % grid, grid - (width % grid)) <= tol
	)

# Remove hints that are not on the grid, marking as manually hinted when changed
# Record glyphs with all vertical hints removed
strip_x_glyphs = set()
for g in font.glyphs():
	if not g.isWorthOutputting() or g.foreground.isEmpty():
		continue

	xmin = g.boundingBox()[0]
	kept_v = tuple(h for h in g.vhints if is_on_grid(h))
	kept_h = tuple(h for h in g.hhints if is_on_grid(h))

	if not kept_v or not any(abs(min(s, s + w) - xmin) <= 1 for s, w in kept_v):
		strip_x_glyphs.add(g.glyphname)

	if kept_v != g.vhints or kept_h != g.hhints:
		g.vhints = kept_v
		g.hhints = kept_h
		g.manualHints = True
		print("Hints removed:", g.glyphname)

# TTF auto-instruct
font.autoInstr()

def strip_x_instructions(glyph):
	if not glyph.ttinstrs:
		glyph.ttinstrs = fontforge.parseTTInstrs("IUP[x]\nIUP[y]")
		return

	text = fontforge.unParseTTInstrs(glyph.ttinstrs)
	if isinstance(text, bytes):
		text = text.decode("ascii")
	lines = text.splitlines()
	y_lines = []
	in_x_block = False

	for line in lines:
		cmd = line.strip()
		if cmd == "SVTCA[x-axis]":
			in_x_block = True
			continue
		if cmd == "SVTCA[y-axis]":
			in_x_block = False
		if not in_x_block:
			y_lines.append(line)

	if not y_lines:
		y_lines = ["IUP[x]", "IUP[y]"]
	elif "IUP[x]" not in [l.strip() for l in y_lines]:
		y_lines.insert(0, "IUP[x]")

	glyph.ttinstrs = fontforge.parseTTInstrs("\n".join(y_lines))
	#print("Stripped x instructions:", glyph.glyphname)

# Strip x-axis instructions from glyphs that had all horizontal hints removed
for name in strip_x_glyphs:
	strip_x_instructions(font[name])

# Ensure glyphs with no remaining instructions still keep FreeType's auto-hinter off
for g in font.glyphs():
	if g.isWorthOutputting() and not g.foreground.isEmpty() and not g.ttinstrs:
		g.ttinstrs = fontforge.parseTTInstrs("IUP[x]\nIUP[y]")

font.generate(sys.argv[1][:-3] + "ttf")
