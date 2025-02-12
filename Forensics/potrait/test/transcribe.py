from pyshark import FileCapture
import re
import os

charmaps = {}
keymaps = {
    "0x35": [
        "`",
        "~"
    ],
    "0x00": [
        "<action key up>",
        "<action key up>"
    ],
    "0x1e": [
        "1",
        "!"
    ],
    "0x1f": [
        "2",
        "@"
    ],
    "0x20": [
        "3",
        "#"
    ],
    "0x21": [
        "4",
        "$"
    ],
    "0x22": [
        "5",
        "%"
    ],
    "0x23": [
        "6",
        "^"
    ],
    "0x24": [
        "7",
        "&"
    ],
    "0x25": [
        "8",
        "*"
    ],
    "0x26": [
        "9",
        "("
    ],
    "0x27": [
        "0",
        ")"
    ],
    "0x2d": [
        "-",
        "_"
    ],
    "0x2e": [
        "=",
        "+"
    ],
    "0x14": [
        "q",
        "Q"
    ],
    "0x1a": [
        "w",
        "W"
    ],
    "0x08": [
        "e",
        "E"
    ],
    "0x15": [
        "r",
        "R"
    ],
    "0x17": [
        "t",
        "T"
    ],
    "0x1c": [
        "y",
        "Y"
    ],
    "0x18": [
        "u",
        "U"
    ],
    "0x0c": [
        "i",
        "I"
    ],
    "0x12": [
        "o",
        "O"
    ],
    "0x13": [
        "p",
        "P"
    ],
    "0x2f": [
        "[",
        "{"
    ],
    "0x30": [
        "]",
        "}"
    ],
    "0x31": [
        "\\",
        "|"
    ],
    "0x04": [
        "a",
        "A"
    ],
    "0x16": [
        "s",
        "S"
    ],
    "0x07": [
        "d",
        "D"
    ],
    "0x09": [
        "f",
        "F"
    ],
    "0x0a": [
        "g",
        "G"
    ],
    "0x0b": [
        "h",
        "H"
    ],
    "0x0d": [
        "j",
        "J"
    ],
    "0x0e": [
        "k",
        "K"
    ],
    "0x0f": [
        "l",
        "L"
    ],
    "0x33": [
        ";",
        ":"
    ],
    "0x34": [
        "'",
        "\""
    ],
    "0x1d": [
        "z",
        "Z"
    ],
    "0x1b": [
        "x",
        "X"
    ],
    "0x06": [
        "c",
        "C"
    ],
    "0x19": [
        "v",
        "V"
    ],
    "0x05": [
        "b",
        "B"
    ],
    "0x11": [
        "n",
        "N"
    ],
    "0x10": [
        "m",
        "M"
    ],
    "0x36": [
        ",",
        "<"
    ],
    "0x37": [
        ".",
        ">"
    ],
    "0x38": [
        "/",
        "?"
    ],
    "0x28": [
        "enter",
        "enter"
    ],
    "0x50": [
        "left",
        "left"
    ],
    "0x4f": [
        "right",
        "right"
    ],
    "0x52": [
        "up",
        "up"
    ],
    "0x51": [
        "down",
        "down"
    ],
    "0x29": [
        "escape",
        "escape"
    ],
    "0x2b": [
        "\t",
        "\t"
    ],
    "0x65": [
        "launchapp1",
        "launchapp1"
    ],
    "0x49": [
        "insert",
        "insert"
    ],
    "0x46": [
        "prntscrn",
        "prntscrn"
    ],
    "0x4c": [
        "delete",
        "delete"
    ],
    "0x39": [
        "capslock",
        "capslock"
    ],
    "0x2c": [
        " ",
        " "
    ],
    "0x2a": [
        "backspace",
        "backspace"
    ]
}

mod = re.compile(r'enter|left|down|up|escape')
packets = FileCapture('portrait.pcapng', decode_as={"btl2cap.cid==0x41": "bthid"})
result = ['from pyautogui import *']

text = ''
for packet in packets:
    try:
        bthid = packet.bthid
        keycode1 = bthid.usbhid_boot_report_keyboard_keycode_1
        lshift = f'{bthid.usbhid_boot_report_keyboard_modifier_left_shift}'
        rshift = f'{bthid.usbhid_boot_report_keyboard_modifier_right_shift}'

        if eval(lshift) or eval(rshift):
            char = keymaps[keycode1][1]
        else:
            char = keymaps[keycode1][0]

        if char != '<action key up>':
            if (char == 'i' and mod.findall(result[-1]) \
             or(char == 'R' and mod.findall(result[-1])) \
             or(mod.findall(char))):
                if text:
                    result.append(f"write('{text}')")
                    text = ''
                result.append(f"press('{char}')")
            else:
                text += char
    except:
        pass

with open('macro.py', 'w') as f:
    f.write('\n'.join(result))

os.system('python macro.py')
os.system("sed 's/a/\\xe2/g;s/b/\\x96/g;s/c/\\x88/g' qr.txt")