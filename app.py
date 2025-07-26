# app.py

from flask import Flask, render_template, request
from password_gen import generate_password, calculate_entropy

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    password = None
    entropy = 0
    if request.method == "POST":
        length = int(request.form.get("length", 10))
        use_letters = request.form.get("letters") == "on"
        use_numbers = request.form.get("numbers") == "on"
        use_symbols = request.form.get("symbols") == "on"

        password = generate_password(length, use_letters, use_numbers, use_symbols)

        charset_size = 0
        if use_letters:
            charset_size += len('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        if use_numbers:
            charset_size += len('0123456789')
        if use_symbols:
            charset_size += len('!@#$%^&*()_+-=[]{}|;:,.<>?/`~')  # You can tweak this

        entropy = calculate_entropy(length, charset_size)

    return render_template("index.html", password=password, entropy=entropy)

if __name__ == "__main__":
    app.run(debug=True)
