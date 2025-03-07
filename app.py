from flask import Flask, request, jsonify, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_report', methods=['POST'])
def generate_report():
    data = request.get_json()
    sugu = data['sugu']
    user_input = data['user_input']

    # Create a temporary input file for the Python script
    with open('input.txt', 'w') as f:
        f.write(f"{sugu}\n{user_input}")

    # Run the Python script and capture its output
    result = subprocess.run(['python', 'ehhovark.py'], capture_output=True, text=True)
    report = result.stdout

    return jsonify({'report': report})

if __name__ == '__main__':
    app.run(debug=True)
