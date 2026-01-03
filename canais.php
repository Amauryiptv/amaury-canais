<?php
include 'conexao.php';
session_start();
if(!isset($_SESSION['user'])) { header("Location: index.php"); exit; }

// Adicionar canal
if(isset($_POST['adicionar'])){
    $nome = $_POST['nome'];
    $link = $_POST['link'];
    $id_categoria = $_POST['categoria'];
    $conn->query("INSERT INTO link (nome_link, link_link, id_categoria, logo, acessoLink, id_usuario) 
                  VALUES ('$nome','$link',$id_categoria,'','',1)");
    header("Location: canais.php");
}

// Excluir canal
if(isset($_GET['excluir'])){
    $id = $_GET['excluir'];
    $conn->query("DELETE FROM link WHERE id_link=$id");
    header("Location: canais.php");
}

// Listar canais
$result = $conn->query("SELECT l.id_link, l.nome_link, l.link_link, c.nome AS categoria
                        FROM link l LEFT JOIN categoria c ON l.id_categoria = c.id");
$cats = $conn->query("SELECT * FROM categoria");
?>

<h2>Canais/Links</h2>
<a href="dashboard.php">Voltar</a>
<table border="1">
<tr><th>ID</th><th>Nome</th><th>Link</th><th>Categoria</th><th>Ações</th></tr>
<?php while($row = $result->fetch_assoc()){ ?>
<tr>
<td><?= $row['id_link'] ?></td>
<td><?= $row['nome_link'] ?></td>
<td><?= $row['link_link'] ?></td>
<td><?= $row['categoria'] ?></td>
<td>
<a href="?excluir=<?= $row['id_link'] ?>">Excluir</a>
</td>
</tr>
<?php } ?>
</table>

<h3>Adicionar Canal</h3>
<form method="post">
Nome: <input type="text" name="nome" required><br>
Link: <input type="text" name="link" required><br>
Categoria: <select name="categoria">
<?php while($cat = $cats->fetch_assoc()){ ?>
<option value="<?= $cat['id'] ?>"><?= $cat['nome'] ?></option>
<?php } ?>
</select><br>
<input type="submit" name="adicionar" value="Adicionar">
</form>
