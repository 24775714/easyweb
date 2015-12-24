-- MySQL dump 10.13  Distrib 5.6.23, for Win32 (x86)
--
-- Host: localhost    Database: easydb
-- ------------------------------------------------------
-- Server version	5.6.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `car_maintenance`
--

DROP TABLE IF EXISTS `car_maintenance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `car_maintenance` (
  `recid` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(40) DEFAULT NULL,
  `mtl_name` varchar(45) DEFAULT NULL,
  `odometer` int(11) DEFAULT NULL,
  `remark` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`recid`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car_maintenance`
--

LOCK TABLES `car_maintenance` WRITE;
/*!40000 ALTER TABLE `car_maintenance` DISABLE KEYS */;
INSERT INTO `car_maintenance` VALUES (1,'13-04-2013','变速箱油',17000,'3次保养'),(2,'13-04-2013','刹车油',17000,'3次保养'),(3,'20-07-2013','空气滤芯',20000,'4次保养'),(4,'13-08-2013','机油机滤',21200,'4次保养'),(5,'20-02-2014','机油机滤',29000,'5次保养'),(6,'20-02-2014','防冻液',29000,'5次保养'),(7,'24-02-2014','空气滤芯',32000,'5次保养'),(8,'30-03-2014','机油机滤',33455,'6次保养'),(9,'30-03-2014','变速箱油',33455,'6次保养'),(10,'15-06-2014','空调加氟',37400,'7次保养'),(11,'06-07-2014',' 机滤机油、方向助力、四轮定位',39100,'8次保养'),(12,'10-10-2014','机油机滤',45600,'9次保养'),(13,'21-10-2014','火花塞',46000,'10次保养'),(14,'08-11-2014','水箱盖 灯泡 防冻液',47400,'11次保养'),(15,'25-01-2015','机油机滤、变速箱油、四轮定位',51300,'12次保养'),(16,'18-02-2015','方向助理油',53000,'13次保养'),(17,'03-05-2015','机油机滤',57400,'14次'),(18,'24-08-2015','机油、机滤、空滤',63000,'15次'),(19,'27-08-2015','换刹车片',63400,'16次'),(20,'24-11-2015','机油+变速箱',68400,'17次');
/*!40000 ALTER TABLE `car_maintenance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `consume_class`
--

DROP TABLE IF EXISTS `consume_class`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `consume_class` (
  `recid` int(11) NOT NULL AUTO_INCREMENT,
  `class_code` varchar(45) NOT NULL,
  `class_name` varchar(45) NOT NULL,
  `remark` varchar(200) DEFAULT NULL,
  `priority` int(11) DEFAULT NULL,
  PRIMARY KEY (`recid`),
  UNIQUE KEY `class_id_UNIQUE` (`recid`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `consume_class`
--

LOCK TABLES `consume_class` WRITE;
/*!40000 ALTER TABLE `consume_class` DISABLE KEYS */;
INSERT INTO `consume_class` VALUES (1,'C001','日常用品等','蔬菜,水果，日用品等',19),(2,'C002','汽车消费','学车烧油气等',18),(3,'C003','水电暖费','购电 购水  暖气费 等',19),(4,'C004','伙食费','',20),(5,'C005','其他','',NULL),(7,'C007','房贷','',16),(10,'C006','鞋衣服等','衣服鞋子等',10),(11,'C008','家电通信费','',12),(13,'C009','生日结婚等','生日送礼等',10),(14,'C010','装修与租房','房装修（板材，地板等）',15),(15,'C011','玩具学习等','',14),(16,'C012','看病等','',10),(17,'C013','零食','',13),(18,'consume_date','消费帐期','消费帐期',26),(19,'SUM','合计','',25);
/*!40000 ALTER TABLE `consume_class` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `consume_detail_list`
--

DROP TABLE IF EXISTS `consume_detail_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `consume_detail_list` (
  `recid` int(11) NOT NULL AUTO_INCREMENT,
  `consume_date` varchar(6) NOT NULL,
  `fee` float DEFAULT '0',
  `product_id` int(11) DEFAULT NULL,
  `insert_time` varchar(16) DEFAULT NULL,
  `remark` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`recid`)
) ENGINE=InnoDB AUTO_INCREMENT=992 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `consume_detail_list`
--


--
-- Table structure for table `consume_list`
--

DROP TABLE IF EXISTS `consume_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `consume_list` (
  `recid` int(11) NOT NULL AUTO_INCREMENT,
  `consume_date` varchar(45) NOT NULL,
  `class_id` int(11) DEFAULT NULL,
  `sum_fee` float DEFAULT NULL,
  `consume_state` varchar(2) NOT NULL DEFAULT 'N',
  `insert_time` varchar(45) DEFAULT NULL,
  `remark` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`recid`),
  KEY `FK_list_class_id_idx` (`class_id`),
  CONSTRAINT `FK_list_class_id` FOREIGN KEY (`class_id`) REFERENCES `consume_class` (`recid`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=407 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `consume_list`
--


--
-- Table structure for table `meum_sidebar`
--

DROP TABLE IF EXISTS `meum_sidebar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `meum_sidebar` (
  `recid` int(11) NOT NULL AUTO_INCREMENT,
  `sidebar_code` varchar(45) NOT NULL,
  `sidebar_text` varchar(45) NOT NULL,
  `sidebar_img` varchar(45) NOT NULL DEFAULT 'icon-folder',
  `expanded` varchar(45) DEFAULT '',
  `prant_code` varchar(45) DEFAULT '-1',
  `web_template` varchar(45) DEFAULT NULL,
  `tablename` varchar(20) DEFAULT NULL,
  `sort_number` int(11) DEFAULT '0',
  `sidebarstate` varchar(1) DEFAULT 'N',
  PRIMARY KEY (`recid`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `meum_sidebar`
--

LOCK TABLES `meum_sidebar` WRITE;
/*!40000 ALTER TABLE `meum_sidebar` DISABLE KEYS */;
INSERT INTO `meum_sidebar` VALUES (1,'CCM01','消费分类','icon-page','','JCM00','productclass_view','consume_class',2,'Y'),(2,'CDM01','消费详单明细','icon-page','','XFM00','comsume_detail','consume_detail_list',2,'Y'),(3,'CLM01','消费月结单','icon-page','','XFM00','comsume_view','consume_list',11,'Y'),(4,'CPM01','产品信息','icon-page','','JCM00','product_view','product_list',1,'Y'),(5,'JCM00','基础信息管理','icon-folder','true','-1',NULL,NULL,1,'Y'),(6,'XFM00','消费信息管理','icon-folder','true','-1',NULL,NULL,0,'Y'),(7,'SYS01','系统信息管理','icon-folder','true','-1',NULL,NULL,5,'Y'),(8,'SYS02','菜单管理','icon-page','','SYS01','sidebar_view','meum_sidebar',1,'Y'),(9,'REPORT01','报表信息管理','fa-home','true','-1','','',2,'Y'),(10,'WROKRE01','汽车保养记录','icon-page','','REPORT01','carrep_view','car',2,'N'),(11,'REPRO001','月度消费报表','icon-page','','REPORT01','monthreport_view','month_report',0,'Y'),(12,'REPYear01','年度消费报表','icon-page','true','REPORT01','yearreport_view','year_report',1,'N'),(13,'DES_REPORT','消费报表设计','icon-page','true','REPORT01','des_report_view','DES_REPORT',11,'N'),(14,'BF001','数据库备份','icon-page','true','SYS01','backup_view','',7,'N');
/*!40000 ALTER TABLE `meum_sidebar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_list`
--

DROP TABLE IF EXISTS `product_list`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product_list` (
  `recid` int(11) NOT NULL AUTO_INCREMENT,
  `product_code` varchar(45) NOT NULL,
  `product_name` varchar(45) NOT NULL,
  `class_id` int(11) DEFAULT NULL,
  `unit_price` float DEFAULT NULL,
  `unit_type` varchar(45) DEFAULT NULL,
  `remark` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`recid`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_list`
--

LOCK TABLES `product_list` WRITE;
/*!40000 ALTER TABLE `product_list` DISABLE KEYS */;
INSERT INTO `product_list` VALUES (1,'TRQ001','天然气',2,3.48,'方',''),(2,'TRQ002','天然气2',2,3.58,'方',''),(4,'GSDQ001','购水电气',3,2.1,'方',''),(14,'YSJ001','益生菌',1,16.8,'板',''),(15,'PG001','苹果',1,6,'斤',''),(20,'SZDD001','散装大豆',17,9,'斤',''),(27,'YF001','衣服',10,200,'件',''),(29,'XG001','西瓜',1,1.5,'斤',''),(30,'TZ001','桃子',1,13,'斤',''),(31,'QT001','其他',5,1,'',''),(32,'LF001','理发',5,15,'个',''),(34,'XHS001','西红柿',1,6,'斤',''),(35,'SJ001','烧鸡',4,20,'只',''),(36,'SL001','随礼',13,1,'元',''),(37,'LS001','零食',17,0.8,'个',''),(38,'DZDD001','袋装大豆',4,2.8,'袋',''),(39,'SC001','蔬菜',4,2,'斤',''),(40,'BZ001','饼子',4,1.5,'个',''),(41,'KCDLS001','烤肠等零食',17,1,'个',''),(42,'MMD001','米面等',4,80,'袋',''),(43,'SWJWD001','蛋蛋学费书玩具玩等',15,1,'本',''),(44,'CSGW001','超市购物',4,1,'个',''),(45,'ZD001','早点',4,2.5,'个',''),(46,'Y001','药',16,1,'1',''),(47,'QCYP001','汽车用品',2,1,'件',''),(48,'TCF001','停车费',2,2,'次',''),(49,'WCJC001','外出就餐',4,1,'1',''),(50,'QY001','93#汽油',2,6.54,'L',''),(51,'NFD001','奶粉等',15,32,'箱','蛋蛋牛奶'),(52,'JYD001','酱油等',4,1,'瓶',''),(53,'KDHF001','宽带-电话费用',11,1,'月',''),(54,'XF001','学费',15,1,'1','1');
/*!40000 ALTER TABLE `product_list` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `report_info`
--

DROP TABLE IF EXISTS `report_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `report_info` (
  `recid` int(11) NOT NULL AUTO_INCREMENT,
  `consume_date` varchar(45) NOT NULL,
  `report_year` varchar(2) NOT NULL DEFAULT 'N',
  `class_id` int(11) NOT NULL,
  `report_state` varchar(2) NOT NULL DEFAULT 'N',
  `fee` float DEFAULT '0',
  `increase` float DEFAULT '0',
  PRIMARY KEY (`recid`)
) ENGINE=InnoDB AUTO_INCREMENT=518 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `report_info`
--

--
-- Table structure for table `userinfo`
--

DROP TABLE IF EXISTS `userinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userinfo` (
  `recid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(40) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`recid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userinfo`
--

LOCK TABLES `userinfo` WRITE;
/*!40000 ALTER TABLE `userinfo` DISABLE KEYS */;
INSERT INTO `userinfo` VALUES (1,'admin','admin'),(2,'1','1');
/*!40000 ALTER TABLE `userinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'easydb'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-12-17 16:12:53
