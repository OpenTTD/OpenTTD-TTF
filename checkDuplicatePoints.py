#!/usr/bin/python3

# Scan FontForge .sfd files and report glyphs with exactly co-located (duplicate) points

# Usage:
# python3 checkDuplicatePoints.py

import glob, os, sys
from collections import defaultdict

scriptpath = os.path.dirname(os.path.realpath(__file__))

# find all sfd files recursively
suffix = ".sfd"
sfd_files = glob.glob(os.path.join(scriptpath, "**", "*" + suffix), recursive=True)

# parse each .sfd file and collect duplicate point reports
all_reports = []

for sfd_file in sorted(sfd_files):
  # read file
  with open(sfd_file, "r", encoding="utf-8") as handle:
    lines = handle.readlines()

  # extract font name from header
  font_name = None
  for line in lines:
    if line.startswith("FullName:"):
      font_name = line.split(":", 1)[1].strip()
      break
    if line.startswith("FamilyName:"):
      font_name = line.split(":", 1)[1].strip()
      break
  if font_name is None:
    font_name = os.path.basename(sfd_file)

  # parse glyphs and their spline points
  current_glyph = None
  in_spline_set = False
  glyphs = []

  for line in lines:
    line = line.rstrip("\n")

    # start of a new character
    if line.startswith("StartChar:"):
      current_glyph = {
        "name": line.split(":", 1)[1].strip(),
        "points": []
      }
      in_spline_set = False
      continue

    # end of character
    if line.startswith("EndChar"):
      if current_glyph is not None:
        glyphs.append(current_glyph)
        current_glyph = None
      in_spline_set = False
      continue

    # enter SplineSet block
    if current_glyph is not None and not in_spline_set:
      if line.strip() == "SplineSet":
        in_spline_set = True
        continue

    # parse points inside SplineSet
    if in_spline_set and current_glyph is not None:
      if line.strip() == "EndSplineSet":
        in_spline_set = False
        continue

      stripped = line.strip()
      if not stripped:
        continue

      parts = stripped.split()
      try:
        if parts[-2] in ("m", "l"):
          # move or line: one point
          x = float(parts[0])
          y = float(parts[1])
          current_glyph["points"].append((x, y))
        elif parts[-2] == "c":
          # cubic bezier: three points per line
          for i in range(0, 6, 2):
            x = float(parts[i])
            y = float(parts[i + 1])
            current_glyph["points"].append((x, y))
      except (ValueError, IndexError):
        continue

  # for each glyph, find duplicate points
  for glyph in glyphs:
    point_counts = defaultdict(int)
    for point in glyph["points"]:
      point_counts[point] += 1
    duplicates = {pt: cnt for pt, cnt in point_counts.items() if cnt > 1}
    if duplicates:
      total_dupes = sum(cnt - 1 for cnt in duplicates.values())
      all_reports.append({
        "file": os.path.basename(sfd_file),
        "glyph": glyph["name"],
        "duplicate_count": total_dupes,
        "duplicate_details": dict(duplicates)
      })

# output results in table
if not all_reports:
  print("No duplicate points found in any glyph.")
  sys.exit(0)

header = f"{'Font File':<30} {'Glyph ID':<30} {'Dupes':<8} {'Duplicate Coordinates'}"
print(header)

for report in all_reports:
  coords = ", ".join(
    f"({x}, {y})x{count}"
    for (x, y), count in sorted(report["duplicate_details"].items())
  )
  print(f"{report['file']:<30} {report['glyph']:<30} {report['duplicate_count']:<8} {coords}")

print(f"Total: {len(all_reports)} glyph(s) with duplicate points")
