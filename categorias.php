<?php
include 'conexao.php';
session_start();
if(!isset($_SESSION['user'])) { header("Location: index.php"); exit; }

// Adicionar categoria
if(isset($_POST['adicionar'])){
    $nome = $_POST['nome'];
    $conn->query("INSERT INTO categoria (nome, id_usuario) VALUES ('$nome', 1)");
    header("Location: categorias.php");
}

// Editar categoria
if(isset($_POST['editar'])){
    $id = $_POST['id'];
    $nome = $_POST['nome'];
    $conn->query("UPDATE categoria SET nome='$nome' WHERE id=$id");
    header("Location: categorias.php");
}

// Excluir categoria
if(isset($_GET['excluir'])){
    $id = $_GET['excluir'];
    $conn->query("DELETE FROM categoria WHERE id=$id");
    header("Location: categorias.php");
}

// Listar categorias
$result = $conn->query("SELECT * FROM categoria");
?>

<h2>Categorias</h2>
<a href="dashboard.php">Voltar</a>
<table border="1">
<tr><th>ID</th><th>Nome</th><th>Ações</th></tr>
<?php while($row = $result->fetch_assoc()){ ?>
<tr>
<td><?= $row['id'] ?></td>
<td><?= $row['nome'] ?></td>
<td>
<a href="?excluir=<?= $row['id'] ?>">Excluir</a>
</td>
</tr>
<?php } ?>
</table>

<h3>Adicionar Categoria</h3>
<form method="post">
Nome: <input type="text" name="nome" required><br>
<input type="submit" name="adicionar" value="Adicionar">
</form>
