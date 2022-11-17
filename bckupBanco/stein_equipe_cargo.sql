CREATE DATABASE  IF NOT EXISTS `stein` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `stein`;
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
-- Table structure for table `equipe_cargo`
--

DROP TABLE IF EXISTS `equipe_cargo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `equipe_cargo` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  `descricao` varchar(150) DEFAULT NULL,
  `salario` decimal(8,2) NOT NULL,
  `setor_id` bigint NOT NULL,
  `administrador` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nome` (`nome`),
  KEY `equipe_cargo_setor_id_9a81fe3f_fk_equipe_setor_id` (`setor_id`),
  CONSTRAINT `equipe_cargo_setor_id_9a81fe3f_fk_equipe_setor_id` FOREIGN KEY (`setor_id`) REFERENCES `equipe_setor` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipe_cargo`
--

LOCK TABLES `equipe_cargo` WRITE;
/*!40000 ALTER TABLE `equipe_cargo` DISABLE KEYS */;
INSERT INTO `equipe_cargo` VALUES (1,'Gerente',NULL,4350.25,1,1),(2,'Operador de Caixa',NULL,1975.00,1,0),(3,'Garçom',NULL,1051.00,2,0),(4,'Maítre',NULL,2269.00,2,0),(5,'Bartender',NULL,1354.00,2,0),(6,'Cumim',NULL,1198.00,2,0),(7,'Chef',NULL,3514.00,3,0),(8,'Cozinheiro(a)',NULL,1424.25,3,0),(9,'Auxiliar de Cozinha',NULL,1227.38,3,0),(10,'Auxiliar de Limpeza',NULL,1130.74,3,0);
/*!40000 ALTER TABLE `equipe_cargo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-16 23:48:18
