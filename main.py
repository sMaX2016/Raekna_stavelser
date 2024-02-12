from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    user_text = data['text']

    # Beräkna antalet stavelser per ord
    syllables_per_word = calculate_syllables_per_word(user_text)

    return jsonify({'syllablesPerWord': syllables_per_word})

def calculate_syllables_per_word(text):
    # Enkel logik för att räkna stavelser per ord
    words = re.findall(r'\b\w+\b', text)
    total_syllables = sum(syllables(word) for word in words)

    if len(words) > 0:
        syllables_per_word = total_syllables / len(words)
    else:
        syllables_per_word = 0

    return syllables_per_word

def syllables(word):
    # Enkel logik för att räkna stavelser i ett ord
    vowels = "aeiouyäöå"
    count = 0

    for char in word.lower():
        if char in vowels:
            count += 1

    return count

if __name__ == '__main__':
    app.run(debug=True)
