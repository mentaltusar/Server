from flask import Flask, request, jsonify

app = Flask(__name__)

# Secure Results (Hidden from Frontend)
results = {
    "123": {"name": "Rahul Sharma", "dob": "2003-01-13", "atpo": "Bhubaneswar", "marks": 78, "pdf": "result_123.pdf"},
    "234": {"name": "Anjali Das", "dob": "1974-04-24", "atpo": "Cuttack Sadar, Bhadrak Town", "marks": 82, "pdf": "result_234.pdf"},
    "345": {"name": "Suresh Kumar", "dob": "1985-08-15", "atpo": "Puri Konark, Near Sun Temple", "marks": 90, "pdf": "result_345.pdf"}
}

@app.route('/get_result', methods=['POST'])
def get_result():
    data = request.json
    roll = data.get('roll')
    dob = data.get('dob')

    if roll in results and results[roll]["dob"] == dob:
        return jsonify(results[roll])
    return jsonify({"error": "No result found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
