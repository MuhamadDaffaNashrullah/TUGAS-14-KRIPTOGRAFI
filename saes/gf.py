def _to_hex(n):
    return "0x" + format(n & 0xF, "X")


def gf_multiply(a, b):
    steps = []
    product = 0
    multiplier = a & 0xF
    multiplicand = b & 0xF

    steps.append({
        "description": f"Mulai: {_to_hex(a)} × {_to_hex(b)} di GF(2⁴)",
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
                "description": f"Bit ke-{i} dari b bernilai 1: XOR hasil sementara dengan {_to_hex(multiplier)} (a yang telah digeser)",
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
                "description": "MSB bernilai 1: reduksi dengan XOR 0x3 (bagian x+1 dari polinomial ireduksibel x⁴+x+1)",
                "a": multiplier,
                "b": multiplicand,
                "product": product,
                "reduction": True,
                "before": before,
                "shift": i,
            })

        multiplicand >>= 1

    steps.append({
        "description": f"Hasil akhir: {_to_hex(a)} × {_to_hex(b)} = {_to_hex(product)}",
        "a": a,
        "b": b,
        "product": product,
        "final": True,
    })


    return {"result": product & 0xF, "steps": steps}


def gf_mul(a, b):
    return gf_multiply(a, b)["result"]
