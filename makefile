# Default target
.PHONY: all
all: openttd-sans openttd-serif openttd-small openttd-mono

# Output directory
ttf:
	mkdir -p ttf

# Fonts
.PHONY: openttd-sans
openttd-sans: ttf/OpenTTD-Sans.ttf
.PHONY: openttd-serif
openttd-serif: ttf/OpenTTD-Serif.ttf
.PHONY: openttd-small
openttd-small: ttf/OpenTTD-Small.ttf ttf/OpenTTD-SmallCaps.ttf
.PHONY: openttd-mono
openttd-mono: ttf/OpenTTD-Mono.ttf

# TTF files
ttf/OpenTTD-Sans.ttf: ttf openttd-sans/OpenTTD-Sans.sfd
	cd openttd-sans && fontforge -c 'import fontforge; f=fontforge.open("OpenTTD-Sans.sfd"); f.ascent=800; f.generate("OpenTTD-Sans.ttf")' && mv OpenTTD-Sans.ttf ../ttf
ttf/OpenTTD-Serif.ttf: ttf openttd-serif/OpenTTD-Serif.sfd
	cd openttd-serif && fontforge -c 'import fontforge; f=fontforge.open("OpenTTD-Serif.sfd"); f.ascent=800; f.generate("OpenTTD-Serif.ttf")' && mv OpenTTD-Serif.ttf ../ttf
ttf/OpenTTD-Small.ttf: ttf openttd-small/OpenTTD-Small.sfd
	cd openttd-small && fontforge -c 'import fontforge; f=fontforge.open("OpenTTD-Small.sfd"); f.ascent=800; f.generate("OpenTTD-Small.ttf")' && mv OpenTTD-Small.ttf ../ttf
ttf/OpenTTD-SmallCaps.ttf: ttf openttd-small/OpenTTD-SmallCaps.sfd
	cd openttd-small && fontforge -c 'import fontforge; f=fontforge.open("OpenTTD-SmallCaps.sfd"); f.ascent=800; f.generate("OpenTTD-SmallCaps.ttf")' && mv OpenTTD-SmallCaps.ttf ../ttf
ttf/OpenTTD-Mono.ttf: ttf openttd-mono/OpenTTD-Mono.sfd
	cd openttd-mono && fontforge -c 'import fontforge; f=fontforge.open("OpenTTD-Mono.sfd"); f.ascent=800; f.generate("OpenTTD-Mono.ttf")' && mv OpenTTD-Mono.ttf ../ttf

# Preview PNGs
.PHONY: preview
preview: preview-sans preview-serif preview-small preview-mono

# Output directory
previews:
	mkdir -p previews

# PNG images
preview-sans: previews ttf/OpenTTD-Sans.ttf
	python3 openttd-sans/font_preview.py ttf/OpenTTD-Sans.ttf previews/
preview-serif: previews ttf/OpenTTD-Serif.ttf
	python3 openttd-serif/font_preview.py ttf/OpenTTD-Serif.ttf previews/
preview-small: previews ttf/OpenTTD-Small.ttf ttf/OpenTTD-SmallCaps.ttf
	python3 openttd-small/font_preview.py ttf/OpenTTD-Small.ttf previews/
	python3 openttd-small/font_preview.py ttf/OpenTTD-SmallCaps.ttf previews/
preview-mono: previews ttf/OpenTTD-Mono.ttf
	python3 openttd-mono/font_preview.py ttf/OpenTTD-Mono.ttf previews/
