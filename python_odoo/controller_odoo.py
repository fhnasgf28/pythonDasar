from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/test', methods=['GET'])
def test_controller():
    return jsonify({'message': 'This is a test controller in Odoo'})


if __name__ == "__main__":
    app.run(debug=True)