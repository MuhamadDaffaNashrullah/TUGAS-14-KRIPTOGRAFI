from .tables import SBOX, INV_SBOX
from .state import copy_state, nibble_to_hex


def _sub(state, sbox, name):
    state_before = copy_state(state)
    state_after = [[0, 0], [0, 0]]
    trace = []

    for r in range(2):
        for c in range(2):
            nibble = state[r][c]
            row = (nibble >> 2) & 0x3
            col = nibble & 0x3
            sub = sbox[row][col]
            state_after[r][c] = sub
            trace.append({
                "position": [r, c],
                "input": nibble,
                "input_bin": format(nibble, "04b"),
                "row": row,
                "col": col,
                "output": sub,
                "output_bin": format(sub, "04b"),
                "input_hex": nibble_to_hex(nibble),
                "output_hex": nibble_to_hex(sub),
                "description": f"S[{row}][{col}] = 0x{sub:X}" if name == "SubNibble" else f"INV_S[{row}][{col}] = 0x{sub:X}",
            })

    return {
        "state_before": state_before,
        "state_after": state_after,
        "trace": trace,
        "name": name,
    }


def sub_nibble(state):
    return _sub(state, SBOX, "SubNibble")


def inverse_sub_nibble(state):
    return _sub(state, INV_SBOX, "InvSubNibble")
