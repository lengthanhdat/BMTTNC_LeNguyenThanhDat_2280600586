from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
app = Flask(_name_)

caesar_cipher = CaesarCipher()
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypt_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify ({'decrypted_message': decrypt_text})

if_name_=="_main_"