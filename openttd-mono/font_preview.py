#!/usr/bin/python3

import os
import sys
from PIL import Image, ImageDraw, ImageFont

fontpath = "OpenTTD-Mono.ttf"
if len(sys.argv) > 1:
    fontpath = sys.argv[1]
outputpath = ""
if len(sys.argv) > 2:
    outputpath = sys.argv[2]
size = 10
line = size + 1
background = (100, 100, 136)
background_shade = [(172, 172, 192), (46, 46, 100)]
foreground = (252, 252, 252)
shadow = None

def shadowtext(draw, scale, position, string, font, foreground, background):
    if background is not None:
        draw.text(((position[0] + 1) * scale, (position[1] + 1) * scale), string, font=font, fill=background)
    draw.text((position[0] * scale, position[1] * scale), string, font=font, fill=foreground)

scales = [1, 2, 4]
fontmodes = [{
    "mode": None,
    "description": "anti-aliased"
}, {
    "mode": "1",
    "description": "aliased"
}]

for scale in scales:
    for fontmode in fontmodes:
        image = Image.new("RGB", (450 * scale, int(12.5 * line * scale)), background_shade[1])
        draw = ImageDraw.Draw(image)
        draw.rectangle((0, 0, image.size[0] - scale - 1, image.size[1] - scale - 1), fill=background_shade[0], outline=None)
        draw.rectangle((0 + scale, 0 + scale, image.size[0] - scale - 1, image.size[1] - scale - 1), fill=background, outline=None)
        if fontmode["mode"] is not None:
            draw.fontmode = fontmode["mode"]
        font = ImageFont.truetype(fontpath, size * scale)
        shadowtext(draw, scale, (3, 2 + line * 0), "OpenTTD Mono", font, (252, 176, 48), shadow)
        shadowtext(draw, scale, (3, 2 + line * 1), "A monospaced pixel art-style typeface for OᴘᴇɴTTD.", font, foreground, shadow)
        shadowtext(draw, scale, (3, 2 + line * 2), "Numerics: 0123456789 ⁰¹²³⁴ ½¾¾ 6×7=42 95%", font, foreground, shadow)
        shadowtext(draw, scale, (3, 2 + line * 3), "Upper case: ABCDEFGHIJKLMNOPQRSTUVWXYZ", font, foreground, shadow)
        shadowtext(draw, scale, (3, 2 + line * 4), "Lower case: abcdefghijklmnopqrstuvwxyz", font, foreground, shadow)
        shadowtext(draw, scale, (3, 2 + line * 5), "Symbols: !\"#$%@()*+,-.;/<=>?[\\]^_{|}~¡¤¦§©ª«¬­®", font, foreground, shadow)
        shadowtext(draw, scale, (3, 2 + line * 6), "Diacritics: ÀÁÂÃÄÅĀĂĄÆāàáâãäåăąæ ÇçÈèÍíÐðÑñÔôÜüÞþŊŋ", font, foreground, shadow)
        shadowtext(draw, scale, (3, 2 + line * 7), "Currencies: $£¥¢֏฿₠₡₢₣₤₥₦₧₨₩₪₫€₭₮₯₰₱₲₳₴₵₶₷₸₹₺₻₼₽₾₿", font, foreground, shadow)
        shadowtext(draw, scale, (3, 2 + line * 8), "Greek upper: ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ", font, foreground, shadow)
        shadowtext(draw, scale, (3, 2 + line * 9), "Greek lower: αβγδεζηθικλμνξοπρςστυφχψω", font, foreground, shadow)
        shadowtext(draw, scale, (3, 2 + line * 10), "Cyrillic upper: АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ", font, foreground, shadow)
        shadowtext(draw, scale, (3, 2 + line * 11), "Cyrillic lower: абвгдежзиклмнопрстуфхцчшщъыьэюя", font, foreground, shadow)
        image.save(os.path.join(outputpath, "OpenTTD-Mono-" + str(scale * size) + "px-" + fontmode["description"] + ".png"), "PNG")