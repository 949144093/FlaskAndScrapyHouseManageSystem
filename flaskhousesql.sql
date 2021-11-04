/*
SQLyog 企业版 - MySQL GUI v8.14 
MySQL - 5.7.17-log : Database - flaskhouse
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`flaskhouse` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci */;

USE `flaskhouse`;

/*Table structure for table `housecount` */

DROP TABLE IF EXISTS `housecount`;

CREATE TABLE `housecount` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `country` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `countryhousecount` varchar(11) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/*Data for the table `housecount` */

insert  into `housecount`(`id`,`country`,`countryhousecount`) values (1,'天津','3'),(2,'上海','17'),(3,'重庆','28'),(4,'武汉','12'),(5,'北京','19');

/*Table structure for table `houseinfo` */

DROP TABLE IF EXISTS `houseinfo`;

CREATE TABLE `houseinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `country` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `communityName` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `houseInfo` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `price` float DEFAULT NULL,
  `name` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `telenumber` varchar(11) COLLATE utf8_unicode_ci DEFAULT NULL,
  `useraccount` varchar(11) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/*Data for the table `houseinfo` */

insert  into `houseinfo`(`id`,`country`,`communityName`,`houseInfo`,`price`,`name`,`telenumber`,`useraccount`) values (1,'武汉','天成美雅','天成美雅-2室2厅-87.59平米',218.5,'李先生','13555555555','user'),(2,'武汉','旭辉御府','旭辉御府-2室1厅-77.19平米',147,'李先生','13999999999','user'),(3,'武汉','天祥尚府','天祥尚府-2室1厅-89.95平米',175,'王先生','13899999999','user'),(4,'武汉','宜家龙臣','宜家龙臣-2室1厅-91.94平米',98.5,'王先生','138988899','user2'),(5,'北京','朝阳小区','朝阳小区-3室1厅-100.36平米',600,'牛先生','13569995993','user2'),(6,'北京','朝阳小区','朝阳小区-2室1厅-80.36平米',500,'牛先生','13569995993','user2');

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(10) COLLATE utf8_unicode_ci DEFAULT NULL,
  `password` varchar(16) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

/*Data for the table `user` */

insert  into `user`(`id`,`username`,`password`) values (1,'admin','666'),(2,'user','666'),(3,'user2','666'),(4,'user3','666');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
