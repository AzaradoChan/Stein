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
-- Table structure for table `estoque_produto`
--

DROP TABLE IF EXISTS `estoque_produto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estoque_produto` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nome` varchar(60) NOT NULL,
  `preco` decimal(8,2) NOT NULL,
  `descricao` varchar(150) DEFAULT NULL,
  `dataAdicao` date NOT NULL,
  `vendendo` tinyint(1) NOT NULL,
  `tipoProduto_id` bigint NOT NULL,
  `imagem` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nome` (`nome`),
  KEY `estoque_produto_tipoProduto_id_42d96b45_fk_estoque_t` (`tipoProduto_id`),
  CONSTRAINT `estoque_produto_tipoProduto_id_42d96b45_fk_estoque_t` FOREIGN KEY (`tipoProduto_id`) REFERENCES `estoque_tipoproduto` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estoque_produto`
--

LOCK TABLES `estoque_produto` WRITE;
/*!40000 ALTER TABLE `estoque_produto` DISABLE KEYS */;
INSERT INTO `estoque_produto` VALUES (2,'Suco de Laranja Jarra 1L',12.90,'Suco feito na hora e adoçado.','2022-09-15',1,1,'images/produtos/jarra-de-suco-de-laranja-e-frutas-laranja-com-folhas-verdes_80510-1088.jpg'),(3,'Chiclete Tridente c/8 Menta',1.50,NULL,'2022-09-15',1,8,'images/produtos/Trident-Mentasuave-Web.webp'),(4,'Devassa 350mL',5.80,NULL,'2022-10-04',1,4,'images/produtos/87016-cerveja-devassa-puro-malte-269ml.jpg'),(5,'Porção de Tilápia',25.90,NULL,'2022-10-05',1,7,'images/produtos/porcao-de-tilapia_331161-62.png'),(6,'Coca-Cola 2L',12.50,NULL,'2022-10-05',1,3,'images/produtos/230365-800-auto.png'),(7,'Coca-Cola Lata 350mL',5.40,NULL,'2022-10-05',1,3,'images/produtos/1984-refrigerante-coca-cola-lata-350ml.jpg'),(8,'Suco de Morango Jarra 1L',12.50,NULL,'2022-10-06',1,9,'images/produtos/Limonada-de-Morango.jpg'),(9,'X-tudo',25.90,'Com 2 Hamburgueres, Alface, queijo, tomate, filé de frango, cheddar, cebola caramelizada e bacon.','2022-10-06',1,2,'images/produtos/receitas-de-x-tudo.webp'),(10,'X-Salada',12.60,NULL,'2022-10-06',1,2,'images/produtos/x-salada-classico.jpg'),(11,'Heineken 30mL Zero',8.90,NULL,'2022-10-06',1,5,'images/produtos/87462-cerveja-heineken-0-0-alcool-long-neck-330ml.jpg'),(12,'Guaraná Lata 350mL Zero',8.50,NULL,'2022-10-06',1,6,'images/produtos/995a9c005ff426b2498664abca6004f2.webp'),(13,'Sprite 350mL',4.00,NULL,'2022-10-16',1,3,'images/produtos/51II-Lbyy9L._AC_SX522_.jpg'),(14,'Guaraná 1L',7.98,NULL,'2022-11-08',1,3,'images/produtos/guaraná1L.jpg'),(15,'Guaraná 3L',18.90,NULL,'2022-11-08',1,3,'images/produtos/Guarana3L.jpg'),(16,'Guaraná 350mL',3.50,NULL,'2022-11-08',1,3,'images/produtos/Guarana350mL.png'),(17,'Batata Frita',25.00,NULL,'2022-11-08',1,7,'images/produtos/porcaoBatataFrita.jpg'),(18,'Mistos',67.00,NULL,'2022-11-08',1,7,'images/produtos/porcaoBoteco.jpg'),(19,'Frango a Parmegiana',34.00,NULL,'2022-11-08',1,7,'images/produtos/porcaofrangoparme.jpg'),(20,'Picanha',67.00,NULL,'2022-11-08',1,7,'images/produtos/porcaoPicanha.jpg'),(21,'Frios',27.00,NULL,'2022-11-08',1,7,'images/produtos/porcaoFrios.jpg'),(22,'Heineken 330mL',9.45,NULL,'2022-11-08',1,4,'images/produtos/heineken330mL.jpg'),(23,'Skol 269mL',4.58,NULL,'2022-11-08',1,4,'images/produtos/skol269mL.jpg'),(24,'Eisenbahn Pilsen 350mL',6.45,NULL,'2022-11-08',1,4,'images/produtos/eisenbahn350mL.webp'),(25,'Brahma 350mL Zero',4.58,NULL,'2022-11-08',1,5,'images/produtos/brahma350mL.jpg'),(26,'Itaipava 350mL Zero',5.98,NULL,'2022-11-08',1,5,'images/produtos/itaipava350mL.jpg'),(27,'Estrela Galicia 250mL Zero',5.80,NULL,'2022-11-08',1,5,'images/produtos/estrelaGalicia250mL.png'),(28,'Copo de Abacaxi c/ Menta',3.58,NULL,'2022-11-08',1,1,'images/produtos/abacaxiMentaCopo.jpg'),(29,'Jarra 1L Caju',9.58,NULL,'2022-11-08',1,1,'images/produtos/sucoCaju1L.jpg'),(30,'Halls Vários Sabores',1.50,NULL,'2022-11-08',1,8,'images/produtos/hallsSortidos.jpeg'),(31,'Mentos',4.50,NULL,'2022-11-08',1,8,'images/produtos/mentos.webp'),(32,'Chocolate Alpino',2.50,NULL,'2022-11-08',1,8,'images/produtos/alpino.webp'),(33,'Chocolate Smash',2.50,NULL,'2022-11-08',1,8,'images/produtos/smash.webp');
/*!40000 ALTER TABLE `estoque_produto` ENABLE KEYS */;
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
