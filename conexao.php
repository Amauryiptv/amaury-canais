<?php
$host = "localhost";
$db = "cemcvgfc_Painelmaster";
$user = "SEU_USUARIO_DO_MYSQL";  // troque pelo seu
$pass = "SUA_SENHA_DO_MYSQL";    // troque pelo seu

$conn = new mysqli($host, $user, $pass, $db);
if ($conn->connect_error) { die("Erro de conexão: " . $conn->connect_error); }
$conn->set_charset("utf8mb4");
?>
