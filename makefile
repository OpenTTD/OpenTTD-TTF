# Default target
.PHONY: all
all: ttf preview

# Output TTFs
.PHONY: ttf
ttf: ttfs openttd-sans openttd-serif openttd-small openttd-mono 

# Output directory
ttfs:
	mkdir -p ttfs

# Fonts
.PHONY: openttd-sans
openttd-sans: ttfs/OpenTTD-Sans.ttf
.PHONY: openttd-serif
openttd-serif: ttfs/OpenTTD-Serif.ttf
.PHONY: openttd-small
openttd-small: ttfs/OpenTTD-Small.ttf ttfs/OpenTTD-SmallCaps.ttf
.PHONY: openttd-mono
openttd-mono: ttfs/OpenTTD-Mono.ttf

# TTF files
ttfs/OpenTTD-Sans.ttf: openttd-sans/OpenTTD-Sans.sfd openttd-sans/config.json build_font.py
	cd openttd-sans && fontforge ../build_font.py OpenTTD-Sans.sfd config.json && mv OpenTTD-Sans.ttf ../ttfs
ttfs/OpenTTD-Serif.ttf: openttd-serif/OpenTTD-Serif.sfd openttd-serif/config.json build_font.py
	cd openttd-serif && fontforge ../build_font.py OpenTTD-Serif.sfd config.json && mv OpenTTD-Serif.ttf ../ttfs
ttfs/OpenTTD-Small.ttf: openttd-small/OpenTTD-Small.sfd openttd-small/config.json build_font.py
	cd openttd-small && fontforge ../build_font.py OpenTTD-Small.sfd config.json OpenTTD-Small && mv OpenTTD-Small.ttf ../ttfs
ttfs/OpenTTD-SmallCaps.ttf: openttd-small/OpenTTD-SmallCaps.sfd openttd-small/config.json build_font.py
	cd openttd-small && fontforge ../build_font.py OpenTTD-SmallCaps.sfd config.json OpenTTD-SmallCaps && mv OpenTTD-SmallCaps.ttf ../ttfs
ttfs/OpenTTD-Mono.ttf: openttd-mono/OpenTTD-Mono.sfd openttd-mono/config.json build_font.py
	cd openttd-mono && fontforge ../build_font.py OpenTTD-Mono.sfd config.json && mv OpenTTD-Mono.ttf ../ttfs

# Preview PNGs
.PHONY: preview
preview: previews preview-sans preview-serif preview-small preview-mono

# Output directory
previews:
	mkdir -p previews

# PNG images
preview-sans: ttfs/OpenTTD-Sans.ttf openttd-sans/font_preview.py
	python3 openttd-sans/font_preview.py ttfs/OpenTTD-Sans.ttf previews/
preview-serif: ttfs/OpenTTD-Serif.ttf openttd-serif/font_preview.py
	python3 openttd-serif/font_preview.py ttfs/OpenTTD-Serif.ttf previews/
preview-small: ttfs/OpenTTD-Small.ttf ttfs/OpenTTD-SmallCaps.ttf openttd-small/font_preview.py
	python3 openttd-small/font_preview.py ttfs/OpenTTD-Small.ttf previews/
	python3 openttd-small/font_preview.py ttfs/OpenTTD-SmallCaps.ttf previews/
preview-mono: ttfs/OpenTTD-Mono.ttf openttd-mono/font_preview.py
	python3 openttd-mono/font_preview.py ttfs/OpenTTD-Mono.ttf previews/

# Clean
.PHONY: clean
clean:
	rm -rf ttfs previews

