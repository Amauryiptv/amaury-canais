<?php
include 'conexao.php';
session_start();

if(isset($_SESSION['user'])){
    header("Location: dashboard.php");
    exit;
}

if($_SERVER['REQUEST_METHOD'] == 'POST') {
    $login = $_POST['login'];
    $senha = md5($_POST['senha']); // senha MD5

    $sql = "SELECT * FROM usuario WHERE login_usuario='$login' AND senha_usuario='$senha' LIMIT 1";
    $res = $conn->query($sql);

    if($res->num_rows == 1){
        $_SESSION['user'] = $login;
        header("Location: dashboard.php");
        exit;
    } else {
        $erro = "Login ou senha incorretos!";
    }
}
?>

<h2>Login Master IPTV</h2>
<form method="post">
Login: <input type="text" name="login" required><br>
Senha: <input type="password" name="senha" required><br>
<input type="submit" value="Entrar">
</form>

<?php if(isset($erro)) echo "<p style='color:red;'>$erro</p>"; ?>
