<?php
include 'conexao.php';
session_start();
if(!isset($_SESSION['user'])) { header("Location: index.php"); exit; }

// Adicionar evento
if(isset($_POST['adicionar'])){
    $nome = $_POST['nome'];
    $conn->query("INSERT INTO eventos (nome) VALUES ('$nome')");
    header("Location: eventos.php");
}

// Excluir evento
if(isset($_GET['excluir'])){
    $id = $_GET['excluir'];
    $conn->query("DELETE FROM eventos WHERE id_evento=$id");
    header("Location: eventos.php");
}

// Listar eventos
$result = $conn->query("SELECT * FROM eventos");
?>

<h2>Eventos</h2>
<a href="dashboard.php">Voltar</a>
<table border="1">
<tr><th>ID</th><th>Nome</th><th>Ações</th></tr>
<?php while($row = $result->fetch_assoc()){ ?>
<tr>
<td><?= $row['id_evento'] ?></td>
<td><?= $row['nome'] ?></td>
<td>
<a href="?excluir=<?= $row['id_evento'] ?>">Excluir</a>
</td>
</tr>
<?php } ?>
</table>

<h3>Adicionar Evento</h3>
<form method="post">
Nome do Evento: <input type="text" name="nome" required><br>
<input type="submit" name="adicionar" value="Adicionar Evento">
</form>
