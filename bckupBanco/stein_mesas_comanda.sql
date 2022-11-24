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
-- Table structure for table `mesas_comanda`
--

DROP TABLE IF EXISTS `mesas_comanda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mesas_comanda` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `valorTotal` decimal(10,2) DEFAULT NULL,
  `dataHoraCriada` datetime(6) NOT NULL,
  `atualizada` datetime(6) DEFAULT NULL,
  `funcionario_id` bigint NOT NULL,
  `nmrMesa_id` bigint NOT NULL,
  `encerrada` tinyint(1) NOT NULL,
  `observacao` varchar(255) DEFAULT NULL,
  `dataHoraEncerrada` datetime(6) DEFAULT NULL,
  `valorPago` decimal(10,2) DEFAULT NULL,
  `dataCriada` date NOT NULL,
  `contaAnon_id` varchar(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `mesas_comanda_nmrMesa_id_297c7fb1_fk_mesas_mesa_id` (`nmrMesa_id`),
  KEY `mesas_comanda_contaAnon_id_16735714_fk_moduloEma` (`contaAnon_id`),
  KEY `mesas_comanda_funcionario_id_cd49d19a_fk_equipe_funcionario_id` (`funcionario_id`),
  CONSTRAINT `mesas_comanda_contaAnon_id_16735714_fk_moduloEma` FOREIGN KEY (`contaAnon_id`) REFERENCES `moduloemail_emailanonimo` (`codigoUnico`),
  CONSTRAINT `mesas_comanda_funcionario_id_cd49d19a_fk_equipe_funcionario_id` FOREIGN KEY (`funcionario_id`) REFERENCES `equipe_funcionario` (`id`),
  CONSTRAINT `mesas_comanda_nmrMesa_id_297c7fb1_fk_mesas_mesa_id` FOREIGN KEY (`nmrMesa_id`) REFERENCES `mesas_mesa` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=149 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mesas_comanda`
--

LOCK TABLES `mesas_comanda` WRITE;
/*!40000 ALTER TABLE `mesas_comanda` DISABLE KEYS */;
INSERT INTO `mesas_comanda` VALUES (132,5.80,'2022-11-02 03:58:32.159386',NULL,17,1,1,'','2022-11-02 04:02:32.839027',5.80,'2022-11-02',NULL),(133,5.80,'2022-11-02 04:07:27.651967',NULL,17,4,1,'','2022-11-05 16:15:22.076215',5.80,'2022-11-02',NULL),(134,13.10,'2022-11-04 01:57:03.599574',NULL,23,3,1,'','2022-11-05 16:15:27.889278',13.10,'2022-11-03',NULL),(135,17.00,'2022-11-05 15:12:27.596994',NULL,23,1,1,'','2022-11-05 17:36:21.297607',17.00,'2022-11-05',NULL),(137,101.90,'2022-11-05 16:07:46.060624',NULL,23,9,1,'','2022-11-05 17:36:29.056986',101.90,'2022-11-05','945859'),(138,5.80,'2022-11-05 16:42:14.132445',NULL,23,4,1,'','2022-11-05 17:36:33.180513',5.80,'2022-11-05','723916'),(139,11.60,'2022-11-05 16:48:54.497714',NULL,23,3,1,'','2022-11-05 17:36:37.294894',11.60,'2022-11-05','506290'),(140,23.20,'2022-11-06 00:56:17.771273',NULL,23,4,1,'','2022-11-07 23:48:09.787985',23.20,'2022-11-05','077305'),(141,11.60,'2022-11-06 01:37:45.029021',NULL,23,1,1,'','2022-11-07 23:48:06.470001',11.60,'2022-11-05','723916'),(143,205.80,'2022-11-09 15:58:16.142376',NULL,23,1,1,'','2022-11-09 15:59:02.062676',205.80,'2022-11-09','506290'),(144,364.40,'2022-11-09 16:00:09.126823',NULL,23,4,1,'','2022-11-09 16:03:34.600305',364.40,'2022-11-09','506290'),(145,60.30,'2022-11-09 16:03:15.156000',NULL,20,7,0,'','2022-11-09 16:03:15.180873',0.00,'2022-11-09',NULL),(146,30.10,'2022-11-09 16:08:21.861331',NULL,21,1,0,'Sem cebola','2022-11-09 16:08:32.942369',15.00,'2022-11-09',NULL),(147,55.50,'2022-11-16 23:43:09.946889',NULL,23,4,0,'','2022-11-16 23:43:09.970824',0.00,'2022-11-16','723916'),(148,162.00,'2022-11-18 23:39:13.007540','2022-11-18 23:39:13.024492',21,19,0,'',NULL,0.00,'2022-11-18',NULL);
/*!40000 ALTER TABLE `mesas_comanda` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-23 22:36:25
