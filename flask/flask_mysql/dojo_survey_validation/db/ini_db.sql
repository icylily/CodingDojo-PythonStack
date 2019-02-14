CREATE DATABASE  IF NOT EXISTS `user_survey` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `user_survey`;
-- MySQL dump 10.13  Distrib 8.0.14, for Win64 (x86_64)
--
-- Host: localhost    Database: user_survey
-- ------------------------------------------------------
-- Server version	8.0.14

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `backgroud`
--

DROP TABLE IF EXISTS `backgroud`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `backgroud` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `backgroud` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backgroud`
--

LOCK TABLES `backgroud` WRITE;
/*!40000 ALTER TABLE `backgroud` DISABLE KEYS */;
INSERT INTO `backgroud` VALUES (1,'Absolutely Raw','2019-02-13 10:41:10','2019-02-13 10:42:01'),(2,'A little relevant experience, less than a year','2019-02-13 10:41:10','2019-02-13 10:41:10'),(3,'More than one year relevant experience. ','2019-02-13 10:41:10','2019-02-13 10:41:10');
/*!40000 ALTER TABLE `backgroud` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `language`
--

DROP TABLE IF EXISTS `language`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `language` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `language` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `language`
--

LOCK TABLES `language` WRITE;
/*!40000 ALTER TABLE `language` DISABLE KEYS */;
INSERT INTO `language` VALUES (1,'HTML','2019-02-13 10:43:24','2019-02-13 10:43:24'),(2,'CSS','2019-02-13 10:43:24','2019-02-13 10:43:24'),(3,'JavaScript','2019-02-13 10:43:24','2019-02-13 10:43:24'),(4,'Python','2019-02-13 10:43:24','2019-02-13 10:43:24'),(5,'Mean','2019-02-13 10:43:24','2019-02-13 10:43:24'),(6,'Rubby','2019-02-13 10:43:24','2019-02-13 10:43:24'),(7,'Jave','2019-02-13 10:43:24','2019-02-13 10:43:24'),(8,'C#.NET','2019-02-13 10:43:24','2019-02-13 10:43:24');
/*!40000 ALTER TABLE `language` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `location`
--

DROP TABLE IF EXISTS `location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `location` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `city` varchar(45) DEFAULT NULL,
  `state` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `location`
--

LOCK TABLES `location` WRITE;
/*!40000 ALTER TABLE `location` DISABLE KEYS */;
INSERT INTO `location` VALUES (1,'Berkeley','CA','2019-02-13 10:47:13','2019-02-13 10:47:13'),(2,'Boise','ID','2019-02-13 10:47:13','2019-02-13 10:47:13'),(3,'Chicago','IL','2019-02-13 10:47:13','2019-02-13 10:47:13'),(4,'Dallas','TX','2019-02-13 10:47:13','2019-02-13 10:47:13'),(5,'Los Angeles','CA','2019-02-13 10:47:13','2019-02-13 10:47:13'),(6,'Orange County','CA','2019-02-13 10:47:13','2019-02-13 10:47:13'),(7,'Seattle','WA','2019-02-13 10:47:13','2019-02-13 10:47:13'),(8,'Silicon Valley','CA','2019-02-13 10:47:13','2019-02-13 10:47:13'),(9,'Tulsa','OK','2019-02-13 10:47:13','2019-02-13 10:47:13'),(10,'Tysons Corner','VA','2019-02-13 10:47:13','2019-02-13 10:47:13'),(11,'ONLINE',NULL,'2019-02-13 10:47:13','2019-02-13 10:47:13');
/*!40000 ALTER TABLE `location` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `source`
--

DROP TABLE IF EXISTS `source`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `source` (
  `id` int(11) NOT NULL,
  `source` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `source`
--

LOCK TABLES `source` WRITE;
/*!40000 ALTER TABLE `source` DISABLE KEYS */;
INSERT INTO `source` VALUES (1,'Facebook'),(2,'Twitter'),(3,'Job hunting site'),(4,'Via a friend'),(5,'Other');
/*!40000 ALTER TABLE `source` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `survey`
--

DROP TABLE IF EXISTS `survey`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `survey` (
  `survey_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(45) DEFAULT NULL,
  `location_id` int(11) DEFAULT NULL,
  `language_id` varchar(45) DEFAULT NULL,
  `background_id` varchar(45) DEFAULT NULL,
  `comment` text,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`survey_id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `survey`
--

LOCK TABLES `survey` WRITE;
/*!40000 ALTER TABLE `survey` DISABLE KEYS */;
INSERT INTO `survey` VALUES (2,'Ann',3,'4','2','good','2019-02-13 13:05:53','2019-02-13 13:05:53'),(3,'lily',1,'1','3','\r\n      pretty good         ','2019-02-13 13:11:45','2019-02-13 13:11:45'),(4,'lily',1,'1','3','\r\n      pretty good         ','2019-02-13 13:12:16','2019-02-13 13:12:16'),(5,'d',1,'1','3','\r\n                ','2019-02-13 13:13:16','2019-02-13 13:13:16'),(6,'cc',1,'1','3','\r\n          dd      ','2019-02-13 14:47:11','2019-02-13 14:47:11'),(7,'ccd',1,'1','3','not bad    ','2019-02-13 14:48:52','2019-02-13 14:48:52'),(8,'ccd',1,'1','3','not bad    ','2019-02-13 14:48:52','2019-02-13 14:48:52'),(9,'ccd',1,'1','3','not bad    ','2019-02-13 14:48:52','2019-02-13 14:48:52'),(10,'ccd',1,'1','3','not bad    ','2019-02-13 14:49:22','2019-02-13 14:49:22'),(11,'ccd',1,'1','3','dd','2019-02-13 15:04:11','2019-02-13 15:04:11'),(12,'ccdd',1,'1','3','dd','2019-02-13 15:05:35','2019-02-13 15:05:35'),(13,'ccddddd',1,'1','3','dddd','2019-02-13 15:09:11','2019-02-13 15:09:11'),(14,'lili',1,'1','3','dddd','2019-02-13 15:12:11','2019-02-13 15:12:11'),(15,'liliy',1,'1','3','dddd','2019-02-13 15:13:29','2019-02-13 15:13:29'),(16,'liliyee',1,'1','3','dddd','2019-02-13 15:14:12','2019-02-13 15:14:12'),(17,'liliyeedd',1,'1','3','dddd','2019-02-13 15:46:38','2019-02-13 15:46:38'),(18,'liliyeeddddd',1,'1','3','dddd','2019-02-13 15:47:34','2019-02-13 15:47:34'),(19,'aadd',1,'1','3','ddd','2019-02-13 15:49:03','2019-02-13 15:49:03'),(20,'tatiana',1,'1','3','ddd','2019-02-13 15:50:04','2019-02-13 15:50:04'),(21,'lanford',1,'1','3','ddd','2019-02-13 15:54:46','2019-02-13 15:54:46'),(22,'lanford1',1,'1','3','ddd','2019-02-13 15:55:15','2019-02-13 15:55:15'),(23,'lanford13',1,'1','3','ddd','2019-02-13 16:04:43','2019-02-13 16:04:43'),(24,'lanford13d',1,'1','3','ddd','2019-02-13 16:11:30','2019-02-13 16:11:30'),(25,'aa',1,'1','3','\r\n                ','2019-02-13 16:24:24','2019-02-13 16:24:24');
/*!40000 ALTER TABLE `survey` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `survey_source`
--

DROP TABLE IF EXISTS `survey_source`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `survey_source` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `survey_id` int(11) DEFAULT NULL,
  `source_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `survey_source`
--

LOCK TABLES `survey_source` WRITE;
/*!40000 ALTER TABLE `survey_source` DISABLE KEYS */;
INSERT INTO `survey_source` VALUES (1,6,1,'2019-02-13 14:55:30','2019-02-13 14:55:30'),(2,6,2,'2019-02-13 14:55:30','2019-02-13 14:55:30'),(3,16,2,'2019-02-13 15:14:12','2019-02-13 15:14:12'),(4,16,3,'2019-02-13 15:14:12','2019-02-13 15:14:12'),(5,16,4,'2019-02-13 15:14:13','2019-02-13 15:14:13'),(6,17,2,'2019-02-13 15:46:38','2019-02-13 15:46:38'),(7,17,3,'2019-02-13 15:46:38','2019-02-13 15:46:38'),(8,17,4,'2019-02-13 15:46:38','2019-02-13 15:46:38'),(9,18,2,'2019-02-13 15:47:34','2019-02-13 15:47:34'),(10,18,3,'2019-02-13 15:47:34','2019-02-13 15:47:34'),(11,18,4,'2019-02-13 15:47:34','2019-02-13 15:47:34'),(12,19,2,'2019-02-13 15:49:03','2019-02-13 15:49:03'),(13,19,3,'2019-02-13 15:49:03','2019-02-13 15:49:03'),(14,19,4,'2019-02-13 15:49:03','2019-02-13 15:49:03'),(15,20,2,'2019-02-13 15:50:04','2019-02-13 15:50:04'),(16,20,3,'2019-02-13 15:50:04','2019-02-13 15:50:04'),(17,20,4,'2019-02-13 15:50:04','2019-02-13 15:50:04'),(18,21,2,'2019-02-13 15:54:46','2019-02-13 15:54:46'),(19,21,3,'2019-02-13 15:54:46','2019-02-13 15:54:46'),(20,21,4,'2019-02-13 15:54:46','2019-02-13 15:54:46'),(21,21,5,'2019-02-13 15:54:46','2019-02-13 15:54:46'),(22,22,2,'2019-02-13 15:55:15','2019-02-13 15:55:15'),(23,22,3,'2019-02-13 15:55:15','2019-02-13 15:55:15'),(24,22,4,'2019-02-13 15:55:15','2019-02-13 15:55:15'),(25,22,5,'2019-02-13 15:55:16','2019-02-13 15:55:16'),(26,23,2,'2019-02-13 16:04:44','2019-02-13 16:04:44'),(27,23,3,'2019-02-13 16:04:44','2019-02-13 16:04:44'),(28,23,4,'2019-02-13 16:04:44','2019-02-13 16:04:44'),(29,23,5,'2019-02-13 16:04:44','2019-02-13 16:04:44'),(30,24,2,'2019-02-13 16:11:30','2019-02-13 16:11:30'),(31,24,3,'2019-02-13 16:11:30','2019-02-13 16:11:30'),(32,24,4,'2019-02-13 16:11:30','2019-02-13 16:11:30'),(33,24,5,'2019-02-13 16:11:30','2019-02-13 16:11:30'),(34,25,3,'2019-02-13 16:24:24','2019-02-13 16:24:24');
/*!40000 ALTER TABLE `survey_source` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'user_survey'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-02-13 19:43:20
