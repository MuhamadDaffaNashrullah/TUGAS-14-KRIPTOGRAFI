from .tables import SBOX, RCON


def _sub_nibble_single(nibble):
    row = (nibble >> 2) & 0x3
    col = nibble & 0x3
    return SBOX[row][col]


def _sub_word(word8bit):
    high = (word8bit >> 4) & 0xF
    low = word8bit & 0xF
    return ((_sub_nibble_single(high) & 0xF) << 4) | (_sub_nibble_single(low) & 0xF)


def _rot_word(word8bit):
    high = (word8bit >> 4) & 0xF
    low = word8bit & 0xF
    return ((low & 0xF) << 4) | (high & 0xF)


def _hex8(n):
    return format(n & 0xFF, "02X")


def _bin8(n):
    return format(n & 0xFF, "08b")


def key_expansion(key16bit):
    w0 = (key16bit >> 8) & 0xFF
    w1 = key16bit & 0xFF

    rot_w1 = _rot_word(w1)
    sub_rot_w1 = _sub_word(rot_w1)
    w2 = w0 ^ RCON[0] ^ sub_rot_w1
    w3 = w2 ^ w1

    rot_w3 = _rot_word(w3)
    sub_rot_w3 = _sub_word(rot_w3)
    w4 = w2 ^ RCON[1] ^ sub_rot_w3
    w5 = w4 ^ w3

    k0 = ((w0 & 0xFF) << 8) | (w1 & 0xFF)
    k1 = ((w2 & 0xFF) << 8) | (w3 & 0xFF)
    k2 = ((w4 & 0xFF) << 8) | (w5 & 0xFF)

    return {
        "w0": w0, "w1": w1, "w2": w2, "w3": w3, "w4": w4, "w5": w5,
        "K0": k0, "K1": k1, "K2": k2,
        "rot_w1": rot_w1, "sub_rot_w1": sub_rot_w1,
        "rot_w3": rot_w3, "sub_rot_w3": sub_rot_w3,
        "K0_matrix": [[(w0 >> 4) & 0xF, (w1 >> 4) & 0xF], [w0 & 0xF, w1 & 0xF]],
        "K1_matrix": [[(w2 >> 4) & 0xF, (w3 >> 4) & 0xF], [w2 & 0xF, w3 & 0xF]],
        "K2_matrix": [[(w4 >> 4) & 0xF, (w5 >> 4) & 0xF], [w4 & 0xF, w5 & 0xF]],
        "display": {
            "w0": _hex8(w0), "w1": _hex8(w1),
            "w2": _hex8(w2), "w3": _hex8(w3),
            "w4": _hex8(w4), "w5": _hex8(w5),
            "rot_w1": _hex8(rot_w1), "sub_rot_w1": _hex8(sub_rot_w1),
            "rot_w3": _hex8(rot_w3), "sub_rot_w3": _hex8(sub_rot_w3),
            "rcon1": _hex8(RCON[0]), "rcon2": _hex8(RCON[1]),
            "K0": format(k0, "04X"), "K1": format(k1, "04X"), "K2": format(k2, "04X"),
        },
        "trace": {
            "step1": {"label": "Initial Words", "w0": {"hex": _hex8(w0), "bin": _bin8(w0)}, "w1": {"hex": _hex8(w1), "bin": _bin8(w1)}},
            "step4": {"equation": f"{_hex8(w0)} ⊕ {_hex8(RCON[0])} ⊕ {_hex8(sub_rot_w1)} = {_hex8(w2)}"},
            "step5": {"equation": f"{_hex8(w2)} ⊕ {_hex8(w1)} = {_hex8(w3)}"},
            "step8": {"equation": f"{_hex8(w2)} ⊕ {_hex8(RCON[1])} ⊕ {_hex8(sub_rot_w3)} = {_hex8(w4)}"},
            "step9": {"equation": f"{_hex8(w4)} ⊕ {_hex8(w3)} = {_hex8(w5)}"},
        },
    }
