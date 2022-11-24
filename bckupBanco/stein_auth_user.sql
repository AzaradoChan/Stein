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
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (7,'pbkdf2_sha256$390000$Ze011l8TwLTp9awAGrryAP$ifvsqOIXSkuegwb05nOGCB9z0YgoUWAKrf06QYtOrKE=','2022-11-18 23:30:34.210831',1,'admin','','','',1,1,'2022-10-01 19:22:06.000000'),(12,'pbkdf2_sha256$390000$O2hpzdocrZSeVkXV7RIGaT$4UErT2oPKOnE/gPFoTdYePkK3Tw0nQkkDptxaNjLxME=','2022-11-24 01:34:51.299228',0,'11111111111','William','Silva','wil.silva@gmail.com',1,1,'2022-10-01 20:10:09.000000'),(13,'pbkdf2_sha256$390000$W5NdR8KExO0NuVowpSuGJq$SMTKZirAyhmtZyadjCpbUhwynAyxp8UjFNd3i9eljus=','2022-11-24 01:32:37.989927',0,'22222222222','Samantha','Maximoff','',0,1,'2022-10-01 20:16:02.000000'),(14,'pbkdf2_sha256$390000$6a3fsAV9WvBcMoWR9pf0jm$X1vL4IwTa0n2yFFOZGvrlgVNiPn+Y7AJNCkDHfZzWjQ=','2022-11-24 01:32:49.303252',0,'33333333333','William','Shakespirro','shakespirro@gmail.com',0,1,'2022-10-04 23:31:43.000000'),(15,'pbkdf2_sha256$390000$jxoIUEw2znF2dfsuNYfeOI$HXzGqHSNMaL/KBkOMHY+Zpb4CSyqkwpV5RXLW/UIlMk=','2022-11-17 02:54:36.879748',0,'44444444444','Tobias','Vidraçaria','vidros@gmail.com',0,1,'2022-10-04 23:39:23.000000'),(16,'pbkdf2_sha256$390000$emVTBiL0cdx3FUBLeebQzO$ycbgACe6jnfitiu3G4XmAGh60L8YK1UYbWRBg2UYSPs=','2022-11-17 02:54:46.492193',0,'55555555555','Godofredo','Fagundes','5@5.com',0,1,'2022-10-15 19:30:16.000000'),(17,'pbkdf2_sha256$390000$1sp6YfAfWDShOAHlMwJHPX$1ElJrsXmyELVXOyQQDviL6lER6s6rrJ6BPlZeT/gcNk=','2022-11-17 02:55:04.153029',0,'66666666666','Fábio','Mendonça','fabio.mendonca@outlook.com',1,1,'2022-10-19 01:20:26.000000'),(18,'pbkdf2_sha256$390000$uafHy3Y5fxmEWfCxXDojma$ttCn85yoaTljSdjRhmhOjSmvppcPfnEqs5GppKVeo14=',NULL,0,'00000000000','Auto','Atendimento','',0,1,'2022-10-19 01:31:22.622795'),(19,'pbkdf2_sha256$390000$Clp1nDs9RJJBBCyRQR9BlG$W8EhTqRIlBQrw0BetNYXeEnQ7h7nK9UIuDpflRAOiI8=','2022-11-06 01:38:03.861248',0,'21212121212','Rafael','Ouverney','rafael_ouverney31@hotmail.com',1,1,'2022-10-22 00:03:35.220279'),(20,'pbkdf2_sha256$390000$egm0AItXnjXkgkyzRAPVZ0$pv/vWAAf5jBJkAmgYR/NVsVeZIoy9pvpGN3FrmT8PMY=','2022-11-09 16:09:18.523238',0,'99999999999','Thomas','da Silva','9@9gmail.com',0,1,'2022-11-05 18:12:24.993474'),(21,'pbkdf2_sha256$390000$6U3kXvbbJ2m7BOjlVM4U1G$USbpNGEPZ15AHLCUXiqYfnE8bHik6EF5YtB8ZzPkDQ4=','2022-11-08 22:39:39.302940',1,'98798798798','Julia','Callado','',1,1,'2022-11-08 22:26:11.119690');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-11-23 22:36:24
