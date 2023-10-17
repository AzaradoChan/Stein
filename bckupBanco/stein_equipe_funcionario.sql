-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: stein
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `equipe_funcionario`
--

DROP TABLE IF EXISTS `equipe_funcionario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `equipe_funcionario` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `primeiro_nome` varchar(20) NOT NULL,
  `segundo_nome` varchar(80) NOT NULL,
  `cpf` varchar(14) NOT NULL,
  `ctps` varchar(14) NOT NULL,
  `dataNascimento` date NOT NULL,
  `tel` varchar(15) NOT NULL,
  `rua` varchar(30) NOT NULL,
  `numero` int NOT NULL,
  `bairro` varchar(15) NOT NULL,
  `cidade` varchar(30) NOT NULL,
  `bonusMensal` decimal(8,2) NOT NULL,
  `dataContratacao` date NOT NULL,
  `observacao` varchar(255) DEFAULT NULL,
  `dataDemicao` date DEFAULT NULL,
  `demitido` tinyint(1) NOT NULL,
  `funcao_id` bigint NOT NULL,
  `salTotal` decimal(10,2) DEFAULT NULL,
  `motivoDemicao` varchar(100) DEFAULT NULL,
  `email` varchar(254) DEFAULT '',
  `administrador` tinyint(1) NOT NULL,
  `contaFuncionario_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cpf` (`cpf`),
  UNIQUE KEY `ctps` (`ctps`),
  KEY `equipe_funcionario_contaFuncionario_id_92d758ca_fk_auth_user_id` (`contaFuncionario_id`),
  KEY `equipe_funcionario_funcao_id_e6f3164b_fk_equipe_cargo_id` (`funcao_id`),
  CONSTRAINT `equipe_funcionario_contaFuncionario_id_92d758ca_fk_auth_user_id` FOREIGN KEY (`contaFuncionario_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `equipe_funcionario_funcao_id_e6f3164b_fk_equipe_cargo_id` FOREIGN KEY (`funcao_id`) REFERENCES `equipe_cargo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipe_funcionario`
--

LOCK TABLES `equipe_funcionario` WRITE;
/*!40000 ALTER TABLE `equipe_funcionario` DISABLE KEYS */;
INSERT INTO `equipe_funcionario` VALUES (1,'William','Silva','111.111.111-11','111.111.111-11','2000-01-01','(44) 91111-1111','1',1,'1','1',150.00,'2022-10-01',NULL,NULL,0,1,4500.25,NULL,'wil.silva@gmail.com',1,12),
  (2,'Samantha','Maximoff','222.222.222-22','222.222.222-22','2000-01-01','(44) 22222-2222','2',2,'2','2',20.00,'2022-10-01',NULL,NULL,0,2,1995.00,NULL,'',0,13),
  (3,'William','Shakespirro','333.333.333-33','333.333.333-33','2000-01-01','(44) 33333-3333','3',3,'3','3',30.00,'2022-10-04',NULL,NULL,0,8,1454.25,NULL,'shakespirro@gmail.com',0,14),
  (4,'Godofredo','Fagundes','555.555.555-55','555.555.555-55','2000-01-01','(44) 55555-5555','5',5,'5','5',0.00,'2022-10-15',NULL,NULL,0,3,1051.00,NULL,'5@5.com',0,16),
  (5,'Fábio','Mendonça','666.666.666-66','666.666.666-66','2000-01-01','(44) 66666-6666','6',6,'6','6',1.59,'2022-10-19',NULL,NULL,0,4,2270.59,NULL,'fabio.mendonca@outlook.com',1,17),
  (6,'Auto','Atendimento','000.000.000-00','000.000.000-00','2000-01-01','(44) 00000-0000','0',0,'0','0',-1051.00,'2022-10-19',NULL,NULL,0,3,0.00,NULL,'',0,18),
  (7,'Thomas','da Silva','999.999.999-99','999.999.999-99','2000-01-01','(44) 99999-9999','9',9,'9','9',0.00,'2022-11-05',NULL,NULL,0,9,1227.38,NULL,'9@9gmail.com',0,20);
/*!40000 ALTER TABLE `equipe_funcionario` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-05 20:32:55
