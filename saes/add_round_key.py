from .state import copy_state, nibble_to_hex


def add_round_key(state, round_key):
    state_before = copy_state(state)
    key_matrix = copy_state(round_key)
    state_after = [[0, 0], [0, 0]]
    trace = []

    for r in range(2):
        for c in range(2):
            s = state_before[r][c]
            k = key_matrix[r][c]
            result = s ^ k
            state_after[r][c] = result
            trace.append({
                "position": [r, c],
                "state": s,
                "key": k,
                "result": result,
                "state_bin": format(s, "04b"),
                "key_bin": format(k, "04b"),
                "result_bin": format(result, "04b"),
                "state_hex": nibble_to_hex(s),
                "key_hex": nibble_to_hex(k),
                "result_hex": nibble_to_hex(result),
                "equation": f"{nibble_to_hex(s)} ⊕ {nibble_to_hex(k)} = {nibble_to_hex(result)}",
            })

    return {
        "state_before": state_before,
        "state_after": state_after,
        "key_matrix": key_matrix,
        "trace": trace,
        "name": "AddRoundKey",
    }
