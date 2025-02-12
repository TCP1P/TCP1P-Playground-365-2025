from fontTools.ttLib import TTFont
from binascii import unhexlify
from textwrap import wrap
from pwn import xor

import zipfile
import re
import os

with zipfile.ZipFile('Document.docx') as z:
    font_table = z.open('word/fontTable.xml').read()
    raw_font = z.open('word/fonts/font7.odttf').read()

rule = re.compile(rb'{([A-F0-9\-]+?)}')
key = rule.findall(font_table)[-1].replace(b'-', b'')
key = [int(i, 16) for i in wrap(key.decode(), 2)][::-1]
key = bytearray(key)

with open('Regular-Font.ttf', 'wb') as f:
    f.write(xor(raw_font[:32], key))
    f.write(raw_font[32:])

font = TTFont('Regular-Font.ttf')
cmap = font.get('cmap')
x, y, z = cmap.tables

# subtable = cmap.tables[0]
# maintable = cmap.tables[2]
# maintable.cmap = subtable.cmap

# font.save('subtable.ttf')

maps = {
    "afii10065": "a",
    "afii10094": "b",
    "afii10083": "c",
    "d": "d",
    "estimated": "e",
    "f": "f",
    "zero": "0",
    "onesuperior": "1",
    "twosuperior": "2",
    "threesuperior": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

flag = ''.join(maps.get(_, _) for _ in x.cmap.values())
with open('flag.png', 'wb') as f:
    f.write(unhexlify(flag))

os.system('zbarimg flag.png')