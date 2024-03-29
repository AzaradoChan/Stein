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
-- Table structure for table `mesas_comanda_produto`
--

DROP TABLE IF EXISTS `mesas_comanda_produto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mesas_comanda_produto` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `comanda_id` bigint NOT NULL,
  `produto_id` bigint NOT NULL,
  `quantidade` int NOT NULL,
  `quantidadeEntregue` int NOT NULL,
  `horaPedido` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mesas_comanda_produto_comanda_id_6565c6c2_fk_mesas_comanda_id` (`comanda_id`),
  KEY `mesas_comanda_produto_produto_id_192c8193_fk_estoque_produto_id` (`produto_id`),
  CONSTRAINT `mesas_comanda_produto_comanda_id_6565c6c2_fk_mesas_comanda_id` FOREIGN KEY (`comanda_id`) REFERENCES `mesas_comanda` (`id`),
  CONSTRAINT `mesas_comanda_produto_produto_id_192c8193_fk_estoque_produto_id` FOREIGN KEY (`produto_id`) REFERENCES `estoque_produto` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=346 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mesas_comanda_produto`
--

LOCK TABLES `mesas_comanda_produto` WRITE;
/*!40000 ALTER TABLE `mesas_comanda_produto` DISABLE KEYS */;
INSERT INTO `mesas_comanda_produto` VALUES (184,132,4,1,0,'2022-11-02 03:58:32.165370'),(185,133,4,1,1,'2022-11-02 04:07:27.654963'),(186,134,4,2,2,'2022-11-04 01:57:03.603554'),(187,134,3,1,1,'2022-11-04 01:57:03.606575'),(188,135,12,2,2,'2022-11-05 15:12:27.599985'),(191,137,9,3,3,'2022-11-05 16:07:46.063587'),(192,137,10,1,1,'2022-11-05 16:07:46.068603'),(193,137,4,2,2,'2022-11-05 16:34:27.869581'),(194,138,4,1,0,'2022-11-05 16:42:14.135435'),(195,139,4,2,2,'2022-11-05 16:48:54.500705'),(196,140,4,4,4,'2022-11-06 00:56:17.776258'),(197,141,4,2,0,'2022-11-06 01:37:45.032012'),(199,143,5,2,2,'2022-11-09 15:58:16.145400'),(200,143,17,5,5,'2022-11-09 15:58:16.150072'),(201,143,6,2,2,'2022-11-09 15:58:16.154067'),(202,143,13,1,1,'2022-11-09 15:58:16.157057'),(203,144,4,2,1,'2022-11-09 16:00:09.129466'),(204,144,9,2,2,'2022-11-09 16:00:09.133459'),(205,144,17,2,0,'2022-11-09 16:00:09.137304'),(206,144,18,3,3,'2022-11-09 16:00:09.139803'),(207,144,6,2,1,'2022-11-09 16:00:09.141801'),(208,144,8,2,2,'2022-11-09 16:00:09.144798'),(224,158,2,5,0,'2022-11-29 00:05:01.286005'),(225,158,4,1,0,'2022-11-29 00:05:01.287999'),(226,158,3,2,0,'2022-11-29 00:05:01.289995'),(233,161,2,5,0,'2022-11-29 00:12:07.239527'),(234,161,4,1,0,'2022-11-29 00:12:07.242520'),(235,161,3,2,0,'2022-11-29 00:12:07.244516'),(242,164,4,1,0,'2022-11-29 00:58:35.100309'),(243,164,22,1,0,'2022-11-29 00:58:35.103302'),(244,164,23,1,0,'2022-11-29 00:58:35.106294'),(245,164,24,1,0,'2022-11-29 00:58:35.108287'),(246,164,11,1,0,'2022-11-29 00:58:35.111282'),(247,164,25,1,0,'2022-11-29 00:58:35.114272'),(248,164,26,1,0,'2022-11-29 00:58:35.117266'),(249,164,27,1,0,'2022-11-29 00:58:35.121254'),(250,164,3,1,0,'2022-11-29 00:58:35.124245'),(251,164,30,1,0,'2022-11-29 00:58:35.127239'),(252,164,31,1,0,'2022-11-29 00:58:35.131226'),(253,164,32,1,0,'2022-11-29 00:58:35.134218'),(254,164,33,1,0,'2022-11-29 00:58:35.137211'),(255,164,9,1,0,'2022-11-29 00:58:35.140203'),(256,164,10,1,0,'2022-11-29 00:58:35.143195'),(257,164,5,1,0,'2022-11-29 00:58:35.146186'),(258,164,17,1,0,'2022-11-29 00:58:35.149187'),(259,164,18,1,0,'2022-11-29 00:58:35.151175'),(260,164,19,1,0,'2022-11-29 00:58:35.154165'),(261,164,20,1,0,'2022-11-29 00:58:35.158155'),(262,164,21,1,0,'2022-11-29 00:58:35.161147'),(263,164,6,1,0,'2022-11-29 00:58:35.165135'),(264,164,7,1,0,'2022-11-29 00:58:35.168135'),(265,164,13,1,0,'2022-11-29 00:58:35.171121'),(266,164,14,1,0,'2022-11-29 00:58:35.175111'),(267,164,15,1,0,'2022-11-29 00:58:35.178102'),(268,164,16,1,0,'2022-11-29 00:58:35.181095'),(269,164,12,1,0,'2022-11-29 00:58:35.184086'),(270,164,2,1,0,'2022-11-29 00:58:35.186080'),(271,164,28,1,0,'2022-11-29 00:58:35.189072'),(272,164,29,1,0,'2022-11-29 00:58:35.192063'),(273,164,8,1,0,'2022-11-29 00:58:35.195057'),(274,165,4,1,0,'2022-11-30 23:25:36.013784'),(275,165,22,1,0,'2022-11-30 23:25:36.016774'),(276,165,23,1,0,'2022-11-30 23:25:36.019768'),(277,165,11,1,0,'2022-11-30 23:25:36.021760'),(309,170,9,4,4,'2022-12-04 02:57:23.845301'),(310,170,11,1,1,'2022-12-04 02:57:23.847295'),(311,170,6,2,2,'2022-12-04 02:57:23.849290'),(316,170,3,4,4,'2022-12-04 03:10:39.647049'),(317,170,10,3,3,'2022-12-04 03:10:39.649045'),(318,170,17,2,2,'2022-12-04 03:10:39.650042'),(319,170,19,3,2,'2022-12-04 03:10:39.652036'),(327,170,4,4,0,'2022-12-04 03:15:23.679240'),(328,171,4,1,0,'2022-12-04 04:02:00.572079'),(329,172,4,1,0,'2022-12-04 04:05:19.254523'),(330,173,4,6,0,'2022-12-04 04:12:37.111984'),(331,173,23,4,0,'2022-12-04 04:12:37.114979'),(332,173,9,4,0,'2022-12-04 04:12:37.116972'),(333,174,9,2,0,'2022-12-04 04:12:56.738920'),(334,174,10,2,0,'2022-12-04 04:12:56.741913'),(335,174,4,2,0,'2022-12-04 04:13:23.031305'),(336,175,6,12,0,'2022-12-04 04:15:05.413732'),(337,175,13,1,0,'2022-12-04 04:15:05.415726'),(338,175,19,1,0,'2022-12-04 04:15:31.348262'),(339,175,17,21,0,'2022-12-04 04:15:31.351254'),(340,176,4,2,0,'2022-12-04 04:27:43.146606'),(341,175,4,14,0,'2022-12-04 04:28:29.651124'),(342,175,22,12,0,'2022-12-04 04:28:29.654117'),(343,175,23,10,0,'2022-12-04 04:28:29.657109'),(344,175,9,10,0,'2022-12-04 04:28:29.660100'),(345,175,20,20,0,'2022-12-04 04:28:29.661097');
/*!40000 ALTER TABLE `mesas_comanda_produto` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-05 20:32:53
