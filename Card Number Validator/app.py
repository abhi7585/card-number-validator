from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
    card_number = request.form['card_number']
    is_valid = validate_card_number(card_number)
    return jsonify({'is_valid': is_valid})

def validate_card_number(card_number):
    # Remove any non-digit characters
    card_number = ''.join(filter(str.isdigit, card_number))
    
    if len(card_number) != 16:
        return False

    # Implement Luhn's algorithm
    sum = 0
    is_even = False
    for digit in reversed(card_number):
        digit = int(digit)
        if is_even:
            digit *= 2
            if digit > 9:
                digit -= 9
        sum += digit
        is_even = not is_even

    return sum % 10 == 0

if __name__ == '__main__':
    app.run(debug=True)