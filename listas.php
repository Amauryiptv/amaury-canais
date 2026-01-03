<?php
include 'conexao.php';
session_start();
if(!isset($_SESSION['user'])) { header("Location: index.php"); exit; }

// Adicionar lista
if(isset($_POST['adicionar'])){
    $nome = $_POST['nome'];
    $global = isset($_POST['global']) ? 1 : 0;
    $id_usuario = 1; // admin criador

    $conn->query("INSERT INTO lista (nome_lista, global, id_usuario) VALUES ('$nome', $global, $id_usuario)");
    header("Location: listas.php");
}

// Excluir lista
if(isset($_GET['excluir'])){
    $id = $_GET['excluir'];
    $conn->query("DELETE FROM lista WHERE id_lista=$id");
    header("Location: listas.php");
}

// Listar listas
$result = $conn->query("SELECT * FROM lista");
?>

<h2>Listas M3U</h2>
<a href="dashboard.php">Voltar</a>

<table border="1">
<tr><th>ID</th><th>Nome</th><th>Global</th><th>Ações</th></tr>
<?php while($row = $result->fetch_assoc()){ ?>
<tr>
<td><?= $row['id_lista'] ?></td>
<td><?= $row['nome_lista'] ?></td>
<td><?= $row['global'] ? 'Sim' : 'Não' ?></td>
<td>
<a href="?excluir=<?= $row['id_lista'] ?>">Excluir</a>
</td>
</tr>
<?php } ?>
</table>

<h3>Adicionar Lista M3U</h3>
<form method="post">
Nome da Lista: <input type="text" name="nome" required><br>
Global: <input type="checkbox" name="global"><br>
<input type="submit" name="adicionar" value="Adicionar Lista">
</form>
