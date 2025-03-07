from flask import Flask, request, jsonify, render_template
import subprocess
import json

app = Flask(__name__, template_folder='.')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_report', methods=['POST'])
def generate_report():
    data = request.get_json()
    sugu = data['sugu']
    user_input = data['user_input']

    # Run the Python script and pass the input data
    result = subprocess.run(
        ['python', 'ehhovark.py'],
        input=json.dumps({'sugu': sugu, 'user_input': user_input}),
        capture_output=True,
        text=True
    )

    report = result.stdout

    return jsonify({'report': report})

if __name__ == '__main__':
    app.run(debug=True)
