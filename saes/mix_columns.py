from .gf import gf_mul
from .tables import MIX_MATRIX, INV_MIX_MATRIX
from .state import copy_state, nibble_to_hex


def _mix_columns(state, matrix, name):
    state_before = copy_state(state)
    state_after = [[0, 0], [0, 0]]
    trace = []

    for col in range(2):
        s0 = state_before[0][col]
        s1 = state_before[1][col]

        m00 = gf_mul(matrix[0][0], s0)
        m01 = gf_mul(matrix[0][1], s1)
        m10 = gf_mul(matrix[1][0], s0)
        m11 = gf_mul(matrix[1][1], s1)

        new_s0 = m00 ^ m01
        new_s1 = m10 ^ m11
        state_after[0][col] = new_s0
        state_after[1][col] = new_s1

        trace.append({
            "col": col,
            "s0": s0,
            "s1": s1,
            "new_s0": new_s0,
            "new_s1": new_s1,
            "equations": [
                f"s0' = ({matrix[0][0]} × {nibble_to_hex(s0)}) ⊕ ({matrix[0][1]} × {nibble_to_hex(s1)}) = {nibble_to_hex(m00)} ⊕ {nibble_to_hex(m01)} = {nibble_to_hex(new_s0)}",
                f"s1' = ({matrix[1][0]} × {nibble_to_hex(s0)}) ⊕ ({matrix[1][1]} × {nibble_to_hex(s1)}) = {nibble_to_hex(m10)} ⊕ {nibble_to_hex(m11)} = {nibble_to_hex(new_s1)}",
            ],
        })

    return {
        "state_before": state_before,
        "state_after": state_after,
        "trace": trace,
        "name": name,
    }


def mix_columns(state):
    return _mix_columns(state, MIX_MATRIX, "MixColumns")


def inverse_mix_columns(state):
    return _mix_columns(state, INV_MIX_MATRIX, "InvMixColumns")
