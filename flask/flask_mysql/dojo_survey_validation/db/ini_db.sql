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
-- Table structure for table `laguage`
--

DROP TABLE IF EXISTS `laguage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `laguage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `laguage` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `laguage`
--

LOCK TABLES `laguage` WRITE;
/*!40000 ALTER TABLE `laguage` DISABLE KEYS */;
INSERT INTO `laguage` VALUES (1,'HTML','2019-02-13 10:43:24','2019-02-13 10:43:24'),(2,'CSS','2019-02-13 10:43:24','2019-02-13 10:43:24'),(3,'JavaScript','2019-02-13 10:43:24','2019-02-13 10:43:24'),(4,'Python','2019-02-13 10:43:24','2019-02-13 10:43:24'),(5,'Mean','2019-02-13 10:43:24','2019-02-13 10:43:24'),(6,'Rubby','2019-02-13 10:43:24','2019-02-13 10:43:24'),(7,'Jave','2019-02-13 10:43:24','2019-02-13 10:43:24'),(8,'C#.NET','2019-02-13 10:43:24','2019-02-13 10:43:24');
/*!40000 ALTER TABLE `laguage` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `location`
--

DROP TABLE IF EXISTS `location`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `location` (
  `location_id` int(11) NOT NULL AUTO_INCREMENT,
  `city` varchar(45) DEFAULT NULL,
  `state` varchar(45) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`location_id`)
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
  `source_id` int(11) NOT NULL AUTO_INCREMENT,
  `source` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`source_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
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
  `source_id` varchar(45) DEFAULT NULL,
  `comment` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `surveycol` varchar(45) DEFAULT 'NOW() ON UPDATE NOW()',
  `location_location_id` int(11) NOT NULL,
  `laguage_id` int(11) NOT NULL,
  PRIMARY KEY (`survey_id`),
  KEY `fk_survey_location_idx` (`location_location_id`),
  KEY `fk_survey_laguage1_idx` (`laguage_id`),
  CONSTRAINT `fk_survey_laguage1` FOREIGN KEY (`laguage_id`) REFERENCES `laguage` (`id`),
  CONSTRAINT `fk_survey_location` FOREIGN KEY (`location_location_id`) REFERENCES `location` (`location_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `survey`
--

LOCK TABLES `survey` WRITE;
/*!40000 ALTER TABLE `survey` DISABLE KEYS */;
/*!40000 ALTER TABLE `survey` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `survey_source`
--

DROP TABLE IF EXISTS `survey_source`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `survey_source` (
  `id` int(11) NOT NULL,
  `survey_id` int(11) DEFAULT NULL,
  `source_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `survey_source`
--

LOCK TABLES `survey_source` WRITE;
/*!40000 ALTER TABLE `survey_source` DISABLE KEYS */;
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

-- Dump completed on 2019-02-13 10:54:58
