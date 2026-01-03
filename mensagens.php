<?php
include 'conexao.php';
session_start();
if(!isset($_SESSION['user'])) { header("Location: index.php"); exit; }

// Adicionar mensagem
if(isset($_POST['adicionar'])){
    $titulo = $_POST['titulo'];
    $mensagem = $_POST['mensagem'];
    $id_evento = $_POST['evento'];
    $id_criador = 1; // admin
    $data = date("Y-m-d H:i:s");

    $conn->query("INSERT INTO mensagens (id_criador, id_evento, titulo, mensagem, data) 
                  VALUES ($id_criador, $id_evento, '$titulo', '$mensagem', '$data')");
    header("Location: mensagens.php");
}

// Excluir mensagem
if(isset($_GET['excluir'])){
    $id = $_GET['excluir'];
    $conn->query("DELETE FROM mensagens WHERE id_mensagem=$id");
    header("Location: mensagens.php");
}

// Listar mensagens
$result = $conn->query("SELECT m.id_mensagem, m.titulo, m.mensagem, m.data, e.nome AS evento
                        FROM mensagens m LEFT JOIN eventos e ON m.id_evento = e.id_evento");
$eventos = $conn->query("SELECT * FROM eventos");
?>

<h2>Mensagens</h2>
<a href="dashboard.php">Voltar</a>
<table border="1">
<tr><th>ID</th><th>Título</th><th>Mensagem</th><th>Evento</th><th>Data</th><th>Ações</th></tr>
<?php while($row = $result->fetch_assoc()){ ?>
<tr>
<td><?= $row['id_mensagem'] ?></td>
<td><?= $row['titulo'] ?></td>
<td><?= $row['mensagem'] ?></td>
<td><?= $row['evento'] ?></td>
<td><?= $row['data'] ?></td>
<td><a href="?excluir=<?= $row['id_mensagem'] ?>">Excluir</a></td>
</tr>
<?php } ?>
</table>

<h3>Adicionar Mensagem</h3>
<form method="post">
Título: <input type="text" name="titulo" required><br>
Mensagem: <textarea name="mensagem" required></textarea><br>
Evento: <select name="evento">
<?php while($ev = $eventos->fetch_assoc()){ ?>
<option value="<?= $ev['id_evento'] ?>"><?= $ev['nome'] ?></option>
<?php } ?>
</select><br>
<input type="submit" name="adicionar" value="Adicionar Mensagem">
</form>
