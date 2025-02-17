from flask import Flask, request, jsonify

response = Flask(__name__)

users = []  # Danh sách user lưu trong RAM (chỉ tồn tại trong quá trình chạy)

@response.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    
    # Kiểm tra dữ liệu đầu vào
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Missing 'name' or 'email'!"}), 400

    users.append(data)
    return jsonify({"message": "User added!", "user": data}), 201

@response.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)  # Trả về danh sách user đã gửi

if __name__ == '__main__':
    response.run(debug=True)
