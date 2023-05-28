#️from flask import Flask, jsonify

#️app = Flask(__name__)

#️@app.route('/api/data', methods=['GET'])
#️def get_data():
#️    data = {
#️        "sales": 100,
#️        "customers": 50,
#️        "revenue": 2000
#️    }
#️    return jsonify(data)

#️if __name__ == '__main__':
#️    app.run(debug=True)

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {"sales": 200, "customers": 50, "revenue": 5000}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5001)



