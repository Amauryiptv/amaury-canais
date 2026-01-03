<?php
include 'conexao.php';
session_start();
if(!isset($_SESSION['user'])) { header("Location: index.php"); exit; }

// Adicionar usuário
if(isset($_POST['adicionar'])){
    $nome = $_POST['nome'];
    $login = $_POST['login'];
    $senha = md5($_POST['senha']);
    $admin = isset($_POST['admin']) ? 1 : 0;

    $sql = "INSERT INTO usuario (nome_usuario, login_usuario, senha_usuario, admin) 
            VALUES ('$nome', '$login', '$senha', $admin)";
    $conn->query($sql);
    header("Location: usuarios.php");
}

// Editar usuário
if(isset($_POST['editar'])){
    $id = $_POST['id'];
    $nome = $_POST['nome'];
    $login = $_POST['login'];
    $senha = md5($_POST['senha']);
    $admin = isset($_POST['admin']) ? 1 : 0;

    $sql = "UPDATE usuario SET nome_usuario='$nome', login_usuario='$login', senha_usuario='$senha', admin=$admin WHERE id_usuario=$id";
    $conn->query($sql);
    header("Location: usuarios.php");
}

// Excluir usuário
if(isset($_GET['excluir'])){
    $id = $_GET['excluir'];
    $conn->query("DELETE FROM usuario WHERE id_usuario=$id");
    header("Location: usuarios.php");
}

// Listar usuários
$result = $conn->query("SELECT * FROM usuario");
?>

<h2>Usuários</h2>
<a href="dashboard.php">Voltar</a>
<table border="1">
<tr><th>ID</th><th>Nome</th><th>Login</th><th>Admin</th><th>Ações</th></tr>
<?php while($row = $result->fetch_assoc()){ ?>
<tr>
<td><?= $row['id_usuario'] ?></td>
<td><?= $row['nome_usuario'] ?></td>
<td><?= $row['login_usuario'] ?></td>
<td><?= $row['admin'] ? 'Sim' : 'Não' ?></td>
<td>
<a href="?excluir=<?= $row['id_usuario'] ?>">Excluir</a>
</td>
</tr>
<?php } ?>
</table>

<h3>Adicionar Usuário</h3>
<form method="post">
Nome: <input type="text" name="nome" required><br>
Login: <input type="text" name="login" required><br>
Senha: <input type="password" name="senha" required><br>
Admin: <input type="checkbox" name="admin"><br>
<input type="submit" name="adicionar" value="Adicionar">
</form>
