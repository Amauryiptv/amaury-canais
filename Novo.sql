-- Desativa checagem de chave estrangeira
SET FOREIGN_KEY_CHECKS = 0;

-- --------------------------------------------------------
-- Tabela: usuario
-- --------------------------------------------------------
DROP TABLE IF EXISTS usuario;
CREATE TABLE usuario (
  id_usuario INT(11) NOT NULL AUTO_INCREMENT,
  nome_usuario VARCHAR(255) NOT NULL,
  senha_usuario VARCHAR(255) DEFAULT '29b2dcbc3c811bc5693c13df2764ea42',
  login_usuario VARCHAR(255) NOT NULL,
  admin INT(1) NOT NULL DEFAULT 0,
  vendedor INT(11) NOT NULL DEFAULT 0,
  estado_usuario INT(1) NOT NULL DEFAULT 1,
  contato_usuario VARCHAR(255) NOT NULL,
  acesso VARCHAR(255) NOT NULL,
  id_criador INT(11) NOT NULL,
  dia INT(255) NOT NULL,
  uso INT(255) NOT NULL DEFAULT 0,
  uso_dia INT(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (id_usuario),
  UNIQUE KEY email_usuario (login_usuario)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO usuario 
(id_usuario, nome_usuario, senha_usuario, login_usuario, admin, vendedor, estado_usuario, contato_usuario, acesso, id_criador, dia, uso, uso_dia) 
VALUES (1, 'Administrador do Servidor', '29b2dcbc3c811bc5693c13df2764ea42', 'admin', 1, 0, 1, '', 'bddf35069c88dcad8925f56ad43d8680', 0, 0, 1, 4);

-- --------------------------------------------------------
-- Tabela: categoria
-- --------------------------------------------------------
DROP TABLE IF EXISTS categoria;
CREATE TABLE categoria (
  id INT(11) NOT NULL AUTO_INCREMENT,
  nome VARCHAR(255) NOT NULL,
  id_usuario INT(11) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY nome (nome)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------
-- Tabela: link
-- --------------------------------------------------------
DROP TABLE IF EXISTS link;
CREATE TABLE link (
  id_link INT(11) NOT NULL AUTO_INCREMENT,
  nome_link VARCHAR(255) NOT NULL,
  link_link VARCHAR(255) NOT NULL,
  id_categoria INT(11) DEFAULT NULL,
  logo VARCHAR(255) NOT NULL,
  acessoLink VARCHAR(255) NOT NULL,
  id_usuario INT(11) NOT NULL,
  PRIMARY KEY (id_link),
  UNIQUE KEY acessoLink (acessoLink),
  UNIQUE KEY nome_link (nome_link),
  KEY id_categoria_fk (id_categoria)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE link
ADD CONSTRAINT id_categoria_fk FOREIGN KEY (id_categoria) REFERENCES categoria(id) ON DELETE SET NULL ON UPDATE SET NULL;

-- --------------------------------------------------------
-- Tabela: lista
-- --------------------------------------------------------
DROP TABLE IF EXISTS lista;
CREATE TABLE lista (
  id_lista INT(11) NOT NULL AUTO_INCREMENT,
  nome_lista VARCHAR(255) NOT NULL,
  global INT(11) NOT NULL DEFAULT 0,
  id_usuario INT(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (id_lista)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------
-- Tabela: lista
