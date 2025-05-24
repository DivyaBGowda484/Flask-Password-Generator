from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    char_pool = ""
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    if not char_pool:
        return "⚠️ Select at least one character type!"

    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ""
    if request.method == 'POST':
        length = int(request.form.get('length', 8))
        use_upper = 'upper' in request.form
        use_lower = 'lower' in request.form
        use_digits = 'digits' in request.form
        use_symbols = 'symbols' in request.form

        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)

    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
