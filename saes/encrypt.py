from .state import to_state_matrix, from_state_matrix, int_to_binary, int_to_hex, copy_state
from .key_expansion import key_expansion
from .add_round_key import add_round_key
from .sub_nibble import sub_nibble
from .shift_rows import shift_rows
from .mix_columns import mix_columns


def _push(steps, step_id, round_num, operation, op_result, label, explanation, round_key=None):
    step = {
        "id": step_id,
        "round": round_num,
        "operation": operation,
        "label": label,
        "explanation": explanation,
        "state_before": op_result["state_before"],
        "state_after": op_result["state_after"],
        "trace": op_result.get("trace"),
    }
    if round_key:
        step["round_key"] = round_key
    steps.append(step)
    return op_result["state_after"]


def encrypt(plaintext, key):
    key_data = key_expansion(key)
    steps = []
    state = to_state_matrix(plaintext)
    initial_state = copy_state(state)

    state = _push(steps, "initial-ark", 0, "AddRoundKey",
                  add_round_key(state, key_data["K0_matrix"]),
                  "Initial AddRoundKey",
                  "State plaintext di-XOR dengan kunci ronde pertama (K0) sebelum ronde enkripsi dimulai.",
                  "K0")

    state = _push(steps, "r1-subnibble", 1, "SubNibble", sub_nibble(state),
                  "Ronde 1 — SubNibble",
                  "Setiap nibble (4 bit) dalam state diganti menggunakan tabel S-Box non-linier.")

    state = _push(steps, "r1-shiftrows", 1, "ShiftRows", shift_rows(state),
                  "Ronde 1 — ShiftRows",
                  "Baris kedua matriks state digeser secara siklis satu posisi ke kiri.")

    state = _push(steps, "r1-mixcols", 1, "MixColumns", mix_columns(state),
                  "Ronde 1 — MixColumns",
                  "Setiap kolom state dikalikan dengan matriks [[1,4],[4,1]] menggunakan aritmatika GF(2⁴).")

    state = _push(steps, "r1-ark", 1, "AddRoundKey",
                  add_round_key(state, key_data["K1_matrix"]),
                  "Ronde 1 — AddRoundKey",
                  "State hasil MixColumns di-XOR dengan kunci ronde kedua (K1).",
                  "K1")

    state = _push(steps, "r2-subnibble", 2, "SubNibble", sub_nibble(state),
                  "Ronde 2 — SubNibble",
                  "Substitusi S-Box dilakukan sekali lagi pada ronde akhir.")

    state = _push(steps, "r2-shiftrows", 2, "ShiftRows", shift_rows(state),
                  "Ronde 2 — ShiftRows",
                  "Baris kedua state kembali digeser siklis satu posisi ke kiri.")

    state = _push(steps, "r2-ark", 2, "AddRoundKey",
                  add_round_key(state, key_data["K2_matrix"]),
                  "Ronde 2 — AddRoundKey (Final)",
                  "State di-XOR dengan kunci ronde terakhir (K2). Hasil operasi ini adalah ciphertext 16-bit.",
                  "K2")

    ciphertext = from_state_matrix(state)

    return {
        "mode": "encrypt",
        "plaintext": plaintext,
        "key": key,
        "ciphertext": ciphertext,
        "plaintext_bin": int_to_binary(plaintext),
        "plaintext_hex": int_to_hex(plaintext),
        "ciphertext_bin": int_to_binary(ciphertext),
        "ciphertext_hex": int_to_hex(ciphertext),
        "key_data": key_data,
        "initial_state": initial_state,
        "final_state": state,
        "steps": steps,
    }
