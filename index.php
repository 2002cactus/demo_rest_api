<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST["name"] ?? ""); // Nhận dữ liệu từ input name
    $email = htmlspecialchars($_POST["email"] ?? ""); // Nhận dữ liệu từ input email
    
    // Kiểm tra dữ liệu hợp lệ
    if (!empty($name) && filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo "<h3>✅ Dữ liệu đã nhận:</h3>";
        echo "Họ tên: " . $name . "<br>";
        echo "Email: " . $email;
    } else {
        echo "<h3>❌ Dữ liệu không hợp lệ!</h3>";
    }
}
?>

<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form POST PHP</title>
</head>
<body>
    <h2>Gửi dữ liệu bằng phương thức POST</h2>
    <form action="" method="POST">
        <label for="name">Họ Tên:</label>
        <input type="text" id="name" name="name" required><br><br>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br><br>

        <button type="submit">Gửi</button>
    </form>
</body>
</html>
