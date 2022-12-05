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
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=106 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2022-11-17 02:51:16.970802','5','Administração',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,7),(2,'2022-11-17 02:51:59.997743','9','auto-pedido',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,7),(3,'2022-11-17 02:52:45.916951','7','Gerência',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,7),(4,'2022-11-17 02:53:26.363525','6','Linha de Frente',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,7),(5,'2022-11-17 02:53:47.841291','8','Retaguarda',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,7),(83,'2022-11-18 23:30:43.150877','16','12',1,'[{\"added\": {}}]',15,7),(84,'2022-11-18 23:30:46.047176','17','13',1,'[{\"added\": {}}]',15,7),(85,'2022-11-18 23:30:48.507421','18','14',1,'[{\"added\": {}}]',15,7),(86,'2022-11-18 23:30:50.831565','19','15',1,'[{\"added\": {}}]',15,7),(87,'2022-11-18 23:30:53.271487','20','16',1,'[{\"added\": {}}]',15,7),(88,'2022-11-18 23:30:55.677607','21','17',1,'[{\"added\": {}}]',15,7),(89,'2022-11-18 23:30:58.184198','22','18',1,'[{\"added\": {}}]',15,7),(90,'2022-11-18 23:31:00.589921','23','19',1,'[{\"added\": {}}]',15,7),(91,'2022-11-18 23:31:04.383122','24','20',1,'[{\"added\": {}}]',15,7),(92,'2022-11-18 23:31:06.445466','25','21',1,'[{\"added\": {}}]',15,7),(93,'2022-11-18 23:31:08.743119','26','22',1,'[{\"added\": {}}]',15,7),(94,'2022-11-18 23:31:10.790480','27','23',1,'[{\"added\": {}}]',15,7),(95,'2022-11-18 23:31:14.325370','28','24',1,'[{\"added\": {}}]',15,7),(96,'2022-11-18 23:31:16.863253','29','25',1,'[{\"added\": {}}]',15,7),(97,'2022-11-18 23:31:18.908035','30','26',1,'[{\"added\": {}}]',15,7),(98,'2022-11-18 23:31:21.429814','31','27',1,'[{\"added\": {}}]',15,7),(99,'2022-11-18 23:31:23.706196','32','28',1,'[{\"added\": {}}]',15,7),(100,'2022-11-18 23:31:26.388587','33','29',1,'[{\"added\": {}}]',15,7),(101,'2022-11-18 23:31:29.024096','34','30',1,'[{\"added\": {}}]',15,7),(102,'2022-11-26 14:27:46.292804','7','admin',2,'[{\"changed\": {\"fields\": [\"Groups\"]}}]',4,7),(103,'2022-12-03 00:30:58.758065','5','Administração',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,7),(104,'2022-12-03 00:31:37.439093','5','Administração',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,7),(105,'2022-12-03 00:55:33.710473','5','Administração',2,'[{\"changed\": {\"fields\": [\"Permissions\"]}}]',3,7);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-05 20:32:54
