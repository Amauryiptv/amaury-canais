<?php
include 'conexao.php';
session_start();
if(!isset($_SESSION['user'])) { header("Location: index.php"); exit; }

// Listar logs
$result = $conn->query("SELECT * FROM logs ORDER BY id_log DESC");
?>

<h2>Logs de Acesso</h2>
<a href="dashboard.php">Voltar</a>
<table border="1">
<tr><th>ID</th><th>Usuário</th><th>Canal</th><th>Data</th></tr>
<?php while($row = $result->fetch_assoc()){ ?>
<tr>
<td><?= $row['id_log'] ?></td>
<td><?= $row['id_usuario'] ?></td>
<td><?= $row['canal'] ?></td>
<td><?= $row['data'] ?></td>
</tr>
<?php } ?>
</table>
