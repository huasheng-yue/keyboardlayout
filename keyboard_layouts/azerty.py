# tuple of upper txt and lower text
rows = [
    # 'functions': {},
    # upper text, lower txt, key_name for key detection
    {
        "name": 'numbers',
        "location": (0, 0),
        "keys": [
            ('', '2', 'code notknown'),
            ('1', '&', '1'),
            ('2', 'é ~', '2'),
            ('3', '" #', '3'),
            ('4', '\' {', '4'),
            ('5', '( [', '5'),
            ('6', '- |', '6'),
            ('7', 'è `', '7'),
            ('8', '_ \\', '8'),
            ('9', 'ç ^', '9'),
            ('0', 'à @', '0'),
            ('°', ') ]', '°'),
            ('+', '= }', '+'),
            ('Backspace', '', 'backspace'),
        ],
    },
    {
        "name": 'letters_1',
        "location": (0, 1),
        "keys": [
            ('Tab', '', 'tab'),
            ('A', '', 'a'),
            ('Z', '', 'z'),
            ('E', '', 'e'),
            ('R', '', 'r'),
            ('T', '', 't'),
            ('Y', '', 'y'),
            ('U', '', 'u'),
            ('I', '', 'i'),
            ('O', '', 'o'),
            ('P', '', 'p'),
            ('¨', '^', '^'),
            ('£', '$ ¤', '$'),
            ('Entrée', '', 'return'),
        ],
    },
    {
        "name": 'letters_2',
        "location": (0, 2),
        "keys": [
            ('Caps Lock', '', 'caps lock'),
            ('Q', '', 'q'),
            ('S', '', 's'),
            ('D', '', 'd'),
            ('F', '', 'f'),
            ('G', '', 'g'),
            ('H', '', 'h'),
            ('J', '', 'j'),
            ('K', '', 'k'),
            ('L', '', 'l'),
            ('M', '', 'm'),
            ('%', 'ù', 'ù'),
            ('μ', "*", "*"),
            ('', '', 'return'),
        ],
    },
    {
        "name": 'letters_3',
        "location": (0, 3),
        "keys": [
            ('Shift', '', 'left shift'),
            ('>', '<', '<'),
            ('W', '', 'w'),
            ('X', '', 'x'),
            ('C', '', 'c'),
            ('V', '', 'v'),
            ('B', '', 'b'),
            ('N', '', 'n'),
            ('?', ',', ','),
            ('.', ';', ';'),
            ('/', ':', ':'),
            ('§', '!', '!'),
            ('Shift', '', 'right shift'),
        ],
    },
    {
        "name": 'spacebar_row',
        "location": (0, 4),
        "keys": [
            ('Ctr', '', 'left control'),
            ('Fn', '', 'function'),
            ('Win', '', 'left windows'),
            ('Alt', '', 'left alt'),
            ('', '', 'space bar'),
            ('AltGr', '', 'right alt'),
            ('Control', '', 'right control'),
        ],
    },
    {
        "name": 'lower arrows',
        "location": (11.2, 4.6),
        "keys": [
            ('◄', '', 'left arrow'),
            ('▼', '', 'down arrow'),
            ('►', '', 'right arrow'),
        ]
    },
    {
        "name": 'upper arrows',
        "location": (12.3, 4.0),
        "keys": [
            ('▲', '', 'up arrow'),
        ]
    },
]
key_sizes = {
    'tab': (1.5, 1),
    'caps lock': (1.7, 1),
    'right shift': (2.3, 1),
    'left shift': (1.2, 1),
    'space bar': (5, 1.2),
    'left control': (1.2, 1.2),
    'alt': (1, 1.2),
    'arrow': (1.1, 0.6)
}
# 14.5 - 11 = 3.5 - 2.3 = 1.2
key_width_percent_remainder_sizes = {
    'return': 100,
}
key_to_key_size = {
    'right shift': 'right shift',
    'left shift': 'left shift',
    'caps lock': 'caps lock',
    'backspace': 'tab',
    'tab': 'tab',
    '\\': 'tab',
    'left control': 'left control',
    'function': 'alt',
    'left alt': 'alt',
    'left windows': 'alt',
    'space bar': 'space bar',
    'right alt': 'alt',
    'right control': 'alt',
    'left arrow': 'arrow',
    'down arrow': 'arrow',
    'right arrow': 'arrow',
    'up arrow': 'arrow',
}
# if key size is not defined, 1 key x by 1 key y size is assumed
