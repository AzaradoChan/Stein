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
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=77 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add Token',7,'add_token'),(26,'Can change Token',7,'change_token'),(27,'Can delete Token',7,'delete_token'),(28,'Can view Token',7,'view_token'),(29,'Can add token',8,'add_tokenproxy'),(30,'Can change token',8,'change_tokenproxy'),(31,'Can delete token',8,'delete_tokenproxy'),(32,'Can view token',8,'view_tokenproxy'),(33,'Can add cargo',9,'add_cargo'),(34,'Can change cargo',9,'change_cargo'),(35,'Can delete cargo',9,'delete_cargo'),(36,'Can view cargo',9,'view_cargo'),(37,'Can add setor',10,'add_setor'),(38,'Can change setor',10,'change_setor'),(39,'Can delete setor',10,'delete_setor'),(40,'Can view setor',10,'view_setor'),(41,'Can add funcionario',11,'add_funcionario'),(42,'Can change funcionario',11,'change_funcionario'),(43,'Can delete funcionario',11,'delete_funcionario'),(44,'Can view funcionario',11,'view_funcionario'),(45,'Can add tipo produto',12,'add_tipoproduto'),(46,'Can change tipo produto',12,'change_tipoproduto'),(47,'Can delete tipo produto',12,'delete_tipoproduto'),(48,'Can view tipo produto',12,'view_tipoproduto'),(49,'Can add produto',13,'add_produto'),(50,'Can change produto',13,'change_produto'),(51,'Can delete produto',13,'delete_produto'),(52,'Can view produto',13,'view_produto'),(53,'Can add comanda',14,'add_comanda'),(54,'Can change comanda',14,'change_comanda'),(55,'Can delete comanda',14,'delete_comanda'),(56,'Can view comanda',14,'view_comanda'),(57,'Can add mesa',15,'add_mesa'),(58,'Can change mesa',15,'change_mesa'),(59,'Can delete mesa',15,'delete_mesa'),(60,'Can view mesa',15,'view_mesa'),(61,'Can add comanda_ produto',16,'add_comanda_produto'),(62,'Can change comanda_ produto',16,'change_comanda_produto'),(63,'Can delete comanda_ produto',16,'delete_comanda_produto'),(64,'Can view comanda_ produto',16,'view_comanda_produto'),(65,'Can add usuario',17,'add_usuario'),(66,'Can change usuario',17,'change_usuario'),(67,'Can delete usuario',17,'delete_usuario'),(68,'Can view usuario',17,'view_usuario'),(69,'Can add perfil',18,'add_perfil'),(70,'Can change perfil',18,'change_perfil'),(71,'Can delete perfil',18,'delete_perfil'),(72,'Can view perfil',18,'view_perfil'),(73,'Can add email anonimo',19,'add_emailanonimo'),(74,'Can change email anonimo',19,'change_emailanonimo'),(75,'Can delete email anonimo',19,'delete_emailanonimo'),(76,'Can view email anonimo',19,'view_emailanonimo');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-05 20:32:51
