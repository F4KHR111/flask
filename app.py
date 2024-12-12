from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Mendapatkan data dari form
    input_text = request.form.get('text_field')
    return jsonify({"response": f"Anda memasukkan: {input_text}"})

if __name__ == '__main__':
    app.run(debug=True)
