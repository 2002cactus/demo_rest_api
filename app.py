from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Cho phép CORS để tránh lỗi trên trình duyệt

users = []  # Danh sách user lưu trong RAM

@app.route('/home')
def home():
    return render_template("index.html")  # Giao diện chính

@app.route('/users', methods=['POST'])
def add_user():
    data = request.json
    if "name" in data and "email" in data:
        users.append(data)
        return jsonify({"message": "User added!", "user": data}), 201
    else:
        return jsonify({"error": "Missing data!"}), 400

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
