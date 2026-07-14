def _to_hex(n):
    return "0x" + format(n & 0xF, "X")


def gf_multiply(a, b):
    steps = []
    product = 0
    multiplier = a & 0xF
    multiplicand = b & 0xF

    steps.append({
        "description": f"Start: {_to_hex(a)} × {_to_hex(b)} in GF(2⁴)",
        "a": multiplier,
        "b": multiplicand,
        "product": 0,
        "shift": 0,
    })

    for i in range(4):
        if multiplicand & 1:
            before = product
            product ^= multiplier
            steps.append({
                "description": f"Bit {i} of b is 1: XOR result with {_to_hex(multiplier)} (shifted a)",
                "a": multiplier,
                "b": multiplicand,
                "product": product,
                "xor_with": multiplier,
                "before": before,
                "shift": i,
            })

        msb = multiplier & 0x8
        multiplier = (multiplier << 1) & 0xF

        if msb:
            before = multiplier
            multiplier ^= 0x3
            steps.append({
                "description": "MSB was 1: reduce by XOR with 0x3 (x+1 part of irreducible poly)",
                "a": multiplier,
                "b": multiplicand,
                "product": product,
                "reduction": True,
                "before": before,
                "shift": i,
            })

        multiplicand >>= 1

    steps.append({
        "description": f"Final result: {_to_hex(a)} × {_to_hex(b)} = {_to_hex(product)}",
        "a": a,
        "b": b,
        "product": product,
        "final": True,
    })

    return {"result": product & 0xF, "steps": steps}


def gf_mul(a, b):
    return gf_multiply(a, b)["result"]
