<?php
include 'conexao.php';
session_start();
if(!isset($_SESSION['user'])) { header("Location: index.php"); exit; }

echo "<h1>Bem-vindo ao Painel Master IPTV</h1>";
echo "<p>Usuário logado: ".$_SESSION['user']."</p>";
echo "<nav>
<a href='usuarios.php'>Usuários</a> | 
<a href='categorias.php'>Categorias</a> | 
<a href='canais.php'>Canais</a> | 
<a href='listas.php'>Listas</a> | 
<a href='eventos.php'>Eventos</a> | 
<a href='mensagens.php'>Mensagens</a> | 
<a href='logs.php'>Logs</a> | 
<a href='logout.php'>Sair</a>
</nav>";
