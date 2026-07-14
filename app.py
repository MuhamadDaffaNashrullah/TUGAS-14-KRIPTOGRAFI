import re

from saes import encrypt, decrypt, TEST_PLAINTEXT, TEST_KEY
from saes.state import binary_to_int
from saes.gf import gf_multiply
from saes.tables import SBOX, INV_SBOX, MIX_MATRIX, INV_MIX_MATRIX, RCON

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

from theme import THEME, OP_COLORS


def validate_binary(value, field_name):
    if not value:
        return f"{field_name} wajib diisi"
    if not re.fullmatch(r"[01]+", value):
        return f"{field_name} hanya boleh berisi 0 dan 1"
    if len(value) != 16:
        return f"{field_name} harus tepat 16 bit (saat ini {len(value)})"
    return ""


def bin_to_hex_label(bin_str):
    if bin_str and len(bin_str) == 16:
        return "0x" + format(int(bin_str, 2), "04X")
    return None


@app.template_filter("bin_pad")
def bin_pad(value, width=16):
    mask = (1 << width) - 1
    return format(int(value) & mask, f"0{width}b")


@app.template_filter("hex_pad")
def hex_pad(value, width=1):
    mask = (1 << (width * 4)) - 1
    return format(int(value) & mask, f"0{width}X")


@app.context_processor
def inject_globals():
    return {
        "OP_COLORS": OP_COLORS,
        "theme": THEME,
        "SBOX": SBOX,
        "INV_SBOX": INV_SBOX,
        "MIX_MATRIX": MIX_MATRIX,
        "INV_MIX_MATRIX": INV_MIX_MATRIX,
        "RCON": RCON,
        "bin_to_hex_label": bin_to_hex_label,
    }


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/docs")
def docs():
    return render_template("docs.html")


@app.route("/simulator", methods=["GET", "POST"])
def simulator():
    mode = request.form.get("mode", "encrypt")
    plaintext_bin = request.form.get("plaintext", "")
    key_bin = request.form.get("key", "")
    action = request.form.get("action", "")
    errors = {"plaintext": "", "key": ""}
    result = None
    show_key_exp = request.form.get("show_key_exp") == "1"
    show_gf = request.form.get("show_gf") == "1"
    gf_a = int(request.form.get("gf_a", 4))
    gf_b = int(request.form.get("gf_b", 5))
    active_step = request.form.get("active_step", "")

    if action == "reset":
        return redirect(url_for("simulator"))

    if action == "test_vector":
        plaintext_bin = TEST_PLAINTEXT
        key_bin = TEST_KEY
        errors = {"plaintext": "", "key": ""}
    elif request.method == "POST":
        if action in ("encrypt", "decrypt"):
            mode = action
        field = "Plaintext" if mode == "encrypt" else "Ciphertext"
        errors["plaintext"] = validate_binary(plaintext_bin, field)
        errors["key"] = validate_binary(key_bin, "Kunci")

        if action not in ("test_vector",) and not errors["plaintext"] and not errors["key"]:
            pt = binary_to_int(plaintext_bin)
            k = binary_to_int(key_bin)
            result = encrypt(pt, k) if mode == "encrypt" else decrypt(pt, k)

    gf_result = gf_multiply(gf_a & 0xF, gf_b & 0xF)

    return render_template(
        "simulator.html",
        mode=mode,
        plaintext_bin=plaintext_bin,
        key_bin=key_bin,
        errors=errors,
        result=result,
        show_key_exp=show_key_exp,
        show_gf=show_gf,
        gf_a=gf_a & 0xF,
        gf_b=gf_b & 0xF,
        gf_result=gf_result,
        active_step=active_step,
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
