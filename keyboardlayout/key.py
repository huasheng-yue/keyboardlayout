from enum import Enum

class Key(Enum):
    """
    These are generic platform independent key constants
    Each graphics backend maps from its own specific key codes to
    these constants
    """
    BACKQUOTE = '`'
    ASCII_TILDE = '~'
    DIGIT_1 = '1'
    EXCLAMATION = '!'
    DIGIT_2 = '2'
    AT = '@'
    DIGIT_3 = '3'
    NUMBER = '#'
    DIGIT_4 = '4'
    DOLLAR = '$'
    DIGIT_5 = '5'
    PERCENT = '%'
    DIGIT_6 = '6'
    CARET = '^'
    DIGIT_7 = '7'
    AMPERSAND = '&'
    DIGIT_8 = '8'
    ASTERISK = '*'
    DIGIT_9 = '9'
    DIGIT_0 = '0'
    MINUS = '-'
    UNDERSCORE = '_'
    EQUALS = '='
    PLUS = '+'
    BACKSPACE = 'backspace'
    TAB = 'tab'
    Q = 'q'
    Q_UPPER = 'Q'
    W = 'w'
    W_UPPER = 'W'
    E = 'e'
    E_UPPER = 'E'
    R = 'r'
    R_UPPER = 'R'
    T = 't'
    T_UPPER = 'T'
    Y = 'y'
    Y_UPPER = 'Y'
    U = 'u'
    U_UPPER = 'U'
    I = 'i'
    I_UPPER = 'I'
    O = 'o'
    O_UPPER = 'O'
    P = 'p'
    P_UPPER = 'P'
    LEFTPAREN = '('
    RIGHTPAREN = ')'
    LEFTBRACKET = '['
    RIGHTBRACKET = ']'
    BRACELEFT = '{'
    BRACERIGHT = '}'
    BACKSLASH = '\\'
    PIPE = '|'
    CAPSLOCK = 'caps lock'
    A = 'a'
    A_UPPER = 'A'
    S = 's'
    S_UPPER = 'S'
    D = 'd'
    D_UPPER = 'D'
    F = 'f'
    F_UPPER = 'F'
    G = 'g'
    G_UPPER = 'G'
    H = 'h'
    H_UPPER = 'H'
    J = 'j'
    J_UPPER = 'J'
    K = 'k'
    K_UPPER = 'K'
    L = 'l'
    L_UPPER = 'L'
    SEMICOLON = ';'
    COLON = ':'
    DOUBLEQUOTE = '"'
    SINGLEQUOTE = "'"
    RETURN = 'return'
    LEFT_SHIFT = 'left shift'
    Z = 'z'
    Z_UPPER = 'Z'
    X = 'x'
    X_UPPER = 'X'
    C = 'c'
    C_UPPER = 'C'
    V = 'v'
    V_UPPER = 'V'
    B = 'b'
    B_UPPER = 'B'
    N = 'n'
    N_UPPER = 'N'
    M = 'm'
    M_UPPER = 'M'
    COMMA = ','
    LESSTHAN = '<'
    PERIOD = '.'
    GREATERTHAN = '>'
    FORWARDSLASH = '/'
    QUESTION = '?'
    RIGHT_SHIFT = 'right shift'
    LEFT_CONTROL = 'left ctrl'
    LEFT_META = 'left meta'
    LEFT_ALT = 'left alt'
    SPACE = 'space'
    RIGHT_ALT = 'right alt'
    RIGHT_META = 'right meta'
    CONTEXT_MENU = 'context menu'  # windows key
    RIGHT_CONTROL = 'right ctrl'
    FUNCTION = 'function'
    LEFT_ARROW = 'left arrow'
    RIGHT_ARROW = 'right arrow'
    UP_ARROW = 'up arrow'
    DOWN_ARROW = 'down arrow'
    # azerty
    TWO_SUPERIOR = '²'
    U_GRAVE = 'ù'
    E_ACUTE = 'é'
    E_GRAVE = 'è'
    C_CEDILLE = 'ç'
    A_GRAVE = 'à'
    DEGREE = '°'
    DIACRATICAL = '¨'
    CIRCUMFLEX = 'ˆ'
    POUND = '£'
    A_CIRCUMFLEX = 'ậ'
    E_CIRCUMFLEX = 'ê'
    I_CIRCUMFLEX = 'î'
    O_CIRCUMFLEX = 'ô'
    U_CIRCUMFLEX = 'û'
    SECTION = '§'
    MU = 'μ'