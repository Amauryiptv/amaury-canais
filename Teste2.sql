USE cemcvgfc_xtserveropensource;

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

SET NAMES utf8mb4;

DROP TABLE IF EXISTS `admin`;
CREATE TABLE `admin` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user` varchar(255) NOT NULL,
  `pass` varchar(255) NOT NULL,
  `admin` varchar(255) DEFAULT NULL,
  `creditos` varchar(255) NOT NULL,
  `creditos_usados` varchar(255) NOT NULL DEFAULT '0',
  `criado_por` varchar(255) DEFAULT '0',
  `servidores` varchar(255) DEFAULT '0',
  `importacao` varchar(255) DEFAULT 'nao',
  `plano` varchar(255) NOT NULL,
  `email` text,
  `telegram` text,
  `whatsapp` text,
  `tipo_link` varchar(20) DEFAULT NULL,
  `saldo_devedor` varchar(255) DEFAULT NULL,
  `token` varchar(255) DEFAULT NULL,
  `data_criado` date DEFAULT NULL,
  `Vencimento` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user` (`user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `admin` VALUES
(11,'admin','admin','1','0','0','0','0','nao','4','teste@gmail.com','efr','43543534','padrao','315','93cec20a5a2d9ccb6e57c79c76b823c6181c04476b73413ec974d0be7808886f',NULL,'2025-08-31');

DROP TABLE IF EXISTS `categoria`;
CREATE TABLE `categoria` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) DEFAULT NULL,
  `parent_id` int DEFAULT 0,
  `type` text,
  `is_adult` int DEFAULT 0,
  `bg` text,
  `admin_id` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

DROP TABLE IF EXISTS `clientes`;
CREATE TABLE `clientes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` text,
  `usuario` varchar(255),
  `senha` varchar(255),
  `Criado_em` datetime,
  `Ultimo_pagamento` datetime,
  `Vencimento` timestamp NULL,
  `is_trial` int NOT NULL DEFAULT 0,
  `adulto` int NOT NULL DEFAULT 0,
  `conexoes` int NOT NULL DEFAULT 1,
  `bloqueio_conexao` varchar(255) NOT NULL DEFAULT 'sim',
  `admin_id` varchar(255) NOT NULL DEFAULT '0',
  `ip` varchar(255),
  `ultimo_acesso` datetime,
  `user_agent` text,
  `ultimo_ip` varchar(255),
  `Dispositivo` varchar(255) NOT NULL DEFAULT 'Desconhecido',
  `App` varchar(255) NOT NULL DEFAULT 'Desconhecido',
  `Forma_de_pagamento` text,
  `nome_do_pagador` varchar(255),
  `Whatsapp` varchar(255),
  `plano` varchar(255) NOT NULL,
  `V_total` varchar(255) NOT NULL DEFAULT '20',
  `c_ocultar_fonte` varchar(255) NOT NULL DEFAULT 'nao',
  `msg` varchar(255),
  `indicado_por` varchar(255),
  `device_mac` varchar(17),
  `device_key` char(6),
  `email_app` varchar(255),
  `senha_app` varchar(255),
  `validade_app` date,
  PRIMARY KEY (`id`),
  UNIQUE KEY `usuario` (`usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

COMMIT;
