def to_state_matrix(value):
    n0 = (value >> 12) & 0xF
    n1 = (value >> 8) & 0xF
    n2 = (value >> 4) & 0xF
    n3 = value & 0xF
    return [[n0, n2], [n1, n3]]


def from_state_matrix(state):
    n0, n2 = state[0]
    n1, n3 = state[1]
    return ((n0 & 0xF) << 12) | ((n1 & 0xF) << 8) | ((n2 & 0xF) << 4) | (n3 & 0xF)


def binary_to_int(bin_str):
    return int(bin_str, 2)


def int_to_binary(n, bits=16):
    return format(n & ((1 << bits) - 1), f"0{bits}b")


def int_to_hex(n, digits=4):
    return format(n & ((1 << (digits * 4)) - 1), f"0{digits}X")


def nibble_to_binary(n):
    return int_to_binary(n & 0xF, 4)


def nibble_to_hex(n):
    return format(n & 0xF, "X")


def copy_state(state):
    return [row[:] for row in state]
