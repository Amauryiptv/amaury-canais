CREATE DATABASE IF NOT EXISTS iptv
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE iptv;

SET FOREIGN_KEY_CHECKS = 0;

DROP TABLE IF EXISTS logs;
DROP TABLE IF EXISTS lidas;
DROP TABLE IF EXISTS mensagens;
DROP TABLE IF EXISTS eventos;
DROP TABLE IF EXISTS lista_usuario;
DROP TABLE IF EXISTS lista_global_categoria;
DROP TABLE IF EXISTS lista;
DROP TABLE IF EXISTS link;
DROP TABLE IF EXISTS categoria;
DROP TABLE IF EXISTS usuario;

SET FOREIGN_KEY_CHECKS = 1;

CREATE TABLE usuario (
  id_usuario INT AUTO_INCREMENT PRIMARY KEY,
  nome_usuario VARCHAR(255) NOT NULL,
  senha_usuario VARCHAR(255) NOT NULL,
  login_usuario VARCHAR(255) NOT NULL,
  admin TINYINT(1) DEFAULT 0,
  vendedor TINYINT(1) DEFAULT 0,
  estado_usuario TINYINT(1) DEFAULT 1,
  contato_usuario VARCHAR(255),
  acesso VARCHAR(255),
  id_criador INT DEFAULT 0,
  dia INT DEFAULT 0,
  uso INT DEFAULT 0,
  uso_dia INT DEFAULT 0,
  UNIQUE KEY login_usuario (login_usuario)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO usuario
(nome_usuario, senha_usuario, login_usuario, admin, acesso)
VALUES
('Administrador do Servidor',
 '29b2dcbc3c811bc5693c13df2764ea42',
 'admin',
 1,
 'masteriptv');

CREATE TABLE categoria (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(255) NOT NULL,
  id_usuario INT NOT NULL,
  UNIQUE KEY nome_usuario (nome, id_usuario),
  FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
  ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE link (
  id_link INT AUTO_INCREMENT PRIMARY KEY,
  nome_link VARCHAR(255) NOT NULL,
  link_link TEXT NOT NULL,
  id_categoria INT DEFAULT NULL,
  logo VARCHAR(255),
  acessoLink VARCHAR(255) NOT NULL,
  id_usuario INT NOT NULL,
  UNIQUE KEY acessoLink (acessoLink),
  FOREIGN KEY (id_categoria) REFERENCES categoria(id)
  ON DELETE SET NULL ON UPDATE CASCADE,
  FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
  ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE lista (
  id_lista INT AUTO_INCREMENT PRIMARY KEY,
  nome_lista VARCHAR(255) NOT NULL,
  global TINYINT(1) DEFAULT 0,
  id_usuario INT DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE lista_global_categoria (
  id INT AUTO_INCREMENT PRIMARY KEY,
  id_categoria INT NOT NULL,
  id_lista INT NOT NULL,
  FOREIGN KEY (id_categoria) REFERENCES categoria(id)
  ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (id_lista) REFERENCES lista(id_lista)
  ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE lista_usuario (
  id INT AUTO_INCREMENT PRIMARY KEY,
  id_lista INT NOT NULL,
  id_usuario INT NOT NULL,
  FOREIGN KEY (id_lista) REFERENCES lista(id_lista)
  ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
  ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE eventos (
  id_evento INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE mensagens (
  id_mensagem INT AUTO_INCREMENT PRIMARY KEY,
  id_criador INT NOT NULL,
  id_evento INT NOT NULL,
  titulo VARCHAR(255),
  mensagem TEXT,
  data DATETIME,
  FOREIGN KEY (id_criador) REFERENCES usuario(id_usuario)
  ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (id_evento) REFERENCES eventos(id_evento)
  ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE lidas (
  id_lida INT AUTO_INCREMENT PRIMARY KEY,
  id_mensagem INT NOT NULL,
  id_usuario INT NOT NULL,
  lida ENUM('sim','nao') DEFAULT 'nao',
  remover TINYINT(1) DEFAULT 0,
  FOREIGN KEY (id_mensagem) REFERENCES mensagens(id_mensagem)
  ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
  ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE logs (
  id_log INT AUTO_INCREMENT PRIMARY KEY,
  id_usuario INT NOT NULL,
  canal VARCHAR(255),
  data DATETIME,
  FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
  ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
