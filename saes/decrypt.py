from .state import to_state_matrix, from_state_matrix, int_to_binary, int_to_hex, copy_state
from .key_expansion import key_expansion
from .add_round_key import add_round_key
from .sub_nibble import inverse_sub_nibble
from .shift_rows import inverse_shift_rows
from .mix_columns import inverse_mix_columns
from .encrypt import _push


def decrypt(ciphertext, key):
    key_data = key_expansion(key)
    steps = []
    state = to_state_matrix(ciphertext)
    initial_state = copy_state(state)

    state = _push(steps, "initial-ark", 0, "AddRoundKey",
                  add_round_key(state, key_data["K2_matrix"]),
                  "Initial AddRoundKey",
                  "State ciphertext di-XOR dengan kunci ronde terakhir (K2) untuk memulai proses dekripsi.",
                  "K2")

    state = _push(steps, "r1-invshiftrows", 1, "InvShiftRows", inverse_shift_rows(state),
                  "Ronde 1 — InvShiftRows",
                  "Baris kedua matriks state digeser secara siklis ke kanan sebanyak satu posisi nibble.")

    state = _push(steps, "r1-invsubnibble", 1, "InvSubNibble", inverse_sub_nibble(state),
                  "Ronde 1 — InvSubNibble",
                  "Setiap nibble dalam state dipetakan kembali menggunakan Inverse S-Box.")

    state = _push(steps, "r1-ark", 1, "AddRoundKey",
                  add_round_key(state, key_data["K1_matrix"]),
                  "Ronde 1 — AddRoundKey",
                  "State hasil substitusi di-XOR dengan kunci ronde K1.",
                  "K1")

    state = _push(steps, "r1-invmixcols", 1, "InvMixColumns", inverse_mix_columns(state),
                  "Ronde 1 — InvMixColumns",
                  "Kolom state dikalikan dengan matriks invers [[9,2],[2,9]] atas GF(2⁴).")

    state = _push(steps, "r2-invshiftrows", 2, "InvShiftRows", inverse_shift_rows(state),
                  "Ronde 2 — InvShiftRows",
                  "Pergeseran baris kedua secara siklis ke kanan satu posisi nibble.")

    state = _push(steps, "r2-invsubnibble", 2, "InvSubNibble", inverse_sub_nibble(state),
                  "Ronde 2 — InvSubNibble",
                  "Substitusi menggunakan Inverse S-Box diulangi kembali.")

    state = _push(steps, "r2-ark", 2, "AddRoundKey",
                  add_round_key(state, key_data["K0_matrix"]),
                  "Ronde 2 — AddRoundKey (Final)",
                  "State di-XOR dengan kunci ronde K0. Hasil akhir adalah plaintext biner 16-bit asli.",
                  "K0")

    plaintext = from_state_matrix(state)

    return {
        "mode": "decrypt",
        "ciphertext": ciphertext,
        "key": key,
        "plaintext": plaintext,
        "ciphertext_bin": int_to_binary(ciphertext),
        "ciphertext_hex": int_to_hex(ciphertext),
        "plaintext_bin": int_to_binary(plaintext),
        "plaintext_hex": int_to_hex(plaintext),
        "key_data": key_data,
        "initial_state": initial_state,
        "final_state": state,
        "steps": steps,
    }
