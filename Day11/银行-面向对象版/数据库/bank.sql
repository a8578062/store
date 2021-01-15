/*
SQLyog Ultimate v12.08 (64 bit)
MySQL - 5.5.27 : Database - yjl
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`yjl` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `yjl`;

/*Table structure for table `t_user` */

DROP TABLE IF EXISTS `t_user`;

CREATE TABLE `t_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `account` int(11) NOT NULL DEFAULT '0',
  `username` varchar(20) DEFAULT NULL,
  `password` int(11) DEFAULT NULL,
  `country` varchar(20) DEFAULT NULL,
  `province` varchar(20) DEFAULT NULL,
  `street` varchar(20) DEFAULT NULL,
  `door` varchar(20) DEFAULT NULL,
  `money` decimal(9,2) DEFAULT NULL,
  `reg_date` datetime DEFAULT NULL,
  `bankname` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`account`),
  KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

/*Data for the table `t_user` */

insert  into `t_user`(`id`,`account`,`username`,`password`,`country`,`province`,`street`,`door`,`money`,`reg_date`,`bankname`) values (4,83862,'姚佳龙',123456,'中国','北京','幸福大道','308','1000.00','2021-01-14 19:31:30','中国工商银行北京市沙河支行'),(5,12519635,'qwer',123456,'123','123','123','123','1234.00','2021-01-14 21:47:57','中国工商银行北京市沙河支行'),(1,40925745,'yjl',123456,'china','beijing','street','308','122456.00','2021-01-14 15:16:51','中国工商银行北京市沙河支行'),(6,49317952,'cyh',990325,'china','beijing','tthxq','501','500.00','2021-01-15 10:49:56','中国工商银行北京市沙河支行'),(2,62668165,'123',123,'13','123','123','123','123.00','2021-01-14 16:02:28','中国工商银行北京市沙河支行');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
