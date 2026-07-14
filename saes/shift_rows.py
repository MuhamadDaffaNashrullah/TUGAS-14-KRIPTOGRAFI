from .state import copy_state


def shift_rows(state):
    state_before = copy_state(state)
    state_after = [
        [state_before[0][0], state_before[0][1]],
        [state_before[1][1], state_before[1][0]],
    ]
    return {
        "state_before": state_before,
        "state_after": state_after,
        "trace": {
            "row0": {
                "before": [state_before[0][0], state_before[0][1]],
                "after": [state_after[0][0], state_after[0][1]],
                "shifted": False,
            },
            "row1": {
                "before": [state_before[1][0], state_before[1][1]],
                "after": [state_after[1][0], state_after[1][1]],
                "shifted": True,
            },
        },
        "name": "ShiftRows",
    }


def inverse_shift_rows(state):
    result = shift_rows(state)
    result["name"] = "InvShiftRows"
    return result
