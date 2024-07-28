/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.1.32-community : Database - tribe
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`tribe` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `tribe`;

/*Table structure for table `notifications` */

DROP TABLE IF EXISTS `notifications`;

CREATE TABLE `notifications` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `notification` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `notifications` */

/*Table structure for table `packagestatus` */

DROP TABLE IF EXISTS `packagestatus`;

CREATE TABLE `packagestatus` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pkgid` int(11) DEFAULT NULL,
  `volid` int(11) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `packagestatus` */

insert  into `packagestatus`(`id`,`pkgid`,`volid`,`status`) values 
(1,2,27,'pending');

/*Table structure for table `tb_account` */

DROP TABLE IF EXISTS `tb_account`;

CREATE TABLE `tb_account` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `accno` varchar(50) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `tb_account` */

insert  into `tb_account`(`id`,`lid`,`accno`,`amount`) values 
(1,22,'123456789123','17240');

/*Table structure for table `tb_allotservice` */

DROP TABLE IF EXISTS `tb_allotservice`;

CREATE TABLE `tb_allotservice` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cid` int(11) DEFAULT NULL,
  `vid` int(11) DEFAULT NULL,
  `rid` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `tb_allotservice` */

/*Table structure for table `tb_awareness` */

DROP TABLE IF EXISTS `tb_awareness`;

CREATE TABLE `tb_awareness` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `exid` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `prgm_name` varchar(50) DEFAULT NULL,
  `details` varchar(50) DEFAULT NULL,
  `photo` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `tb_awareness` */

insert  into `tb_awareness`(`id`,`exid`,`date`,`prgm_name`,`details`,`photo`) values 
(1,10,'2019-11-06','prgm','fgcfg','3_Kurumbar_Nritham_Dance.jpg'),
(2,12,'2019-11-10','nnn','coun','aa.png'),
(3,27,'2019-11-28','pgmins','detttt','Screenshot_93.png');

/*Table structure for table `tb_bill` */

DROP TABLE IF EXISTS `tb_bill`;

CREATE TABLE `tb_bill` (
  `bid` int(11) NOT NULL AUTO_INCREMENT,
  `cuid` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `total` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`bid`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=latin1;

/*Data for the table `tb_bill` */

insert  into `tb_bill`(`bid`,`cuid`,`date`,`total`,`status`) values 
(1,13,'2019-10-29','100','pending'),
(2,22,'2019-11-07','460','pending'),
(3,22,'2019-11-07','140','pending'),
(4,22,'2019-11-07','40','pending'),
(5,22,'2019-11-07','60','payed'),
(6,22,'2019-11-08','200','payed'),
(7,22,'2019-11-08','100','payed'),
(8,22,'2019-11-08','600','payed'),
(9,22,'2019-11-08','100','payed'),
(10,22,'2019-11-08','20','payed'),
(11,22,'2019-11-08','20','payed'),
(12,42,'2019-11-12','100','pending'),
(13,42,'2019-11-12','440','payed'),
(14,22,'2019-11-14','300','pending'),
(15,22,'2019-11-14','100','pending'),
(16,22,'2019-11-14','100','payed'),
(17,22,'2019-11-14','100','payed'),
(18,22,'2019-11-14','300','payed'),
(19,22,'2019-11-14','100','pending'),
(20,22,'2019-11-14','20','payed'),
(21,22,'2019-11-14','40','payed'),
(22,22,'2019-11-14','400','payed'),
(23,43,'2019-11-28','0','pending'),
(24,43,'2019-11-28','220','pending'),
(25,43,'2019-11-28','900','pending'),
(26,43,'2019-11-28','0','pending'),
(27,43,'2019-11-28','0','pending'),
(28,43,'2019-11-28','0','pending'),
(29,43,'2019-11-28','0','pending'),
(30,43,'2019-11-28','40','pending'),
(31,43,'2019-11-28','100','pending');

/*Table structure for table `tb_billproduct` */

DROP TABLE IF EXISTS `tb_billproduct`;

CREATE TABLE `tb_billproduct` (
  `bpid` int(11) NOT NULL AUTO_INCREMENT,
  `bid` int(11) DEFAULT NULL,
  `product` varchar(50) DEFAULT NULL,
  `price` varchar(50) DEFAULT NULL,
  `quantity` varchar(50) DEFAULT NULL,
  `lid` int(11) DEFAULT NULL,
  PRIMARY KEY (`bpid`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=latin1;

/*Data for the table `tb_billproduct` */

insert  into `tb_billproduct`(`bpid`,`bid`,`product`,`price`,`quantity`,`lid`) values 
(1,2,'2','40','2',22),
(2,2,'2','60','3',22),
(3,2,'2','80','4',22),
(4,2,'2','100','5',22),
(5,2,'2','60','3',22),
(6,2,'2','60','3',22),
(7,2,'2','60','3',22),
(8,3,'2','60','3',22),
(9,3,'2','40','2',22),
(10,3,'2','40','2',22),
(11,4,'2','40','2',22),
(12,5,'2','60','3',22),
(13,6,'3','200','2',22),
(14,7,'3','100','1',22),
(15,8,'3','300','3',22),
(16,8,'3','300','3',22),
(17,9,'3','100','1',22),
(18,10,'2','20','1',22),
(19,11,'2','20','1',22),
(20,12,'2','100','5',42),
(21,13,'3','400','4',42),
(22,13,'2','40','2',42),
(23,14,'3','100','1',22),
(24,14,'3','200','2',22),
(25,15,'3','100','1',22),
(26,16,'3','100','1',22),
(27,17,'3','100','1',22),
(28,18,'3','300','3',22),
(29,19,'3','100','1',22),
(30,20,'2','20','1',22),
(31,21,'2','40','2',22),
(32,22,'3','200','2',22),
(33,22,'3','200','2',22),
(34,24,'2','20','1',43),
(35,24,'3','200','2',43),
(36,25,'4','900','1',43),
(37,30,'2','40','2',43),
(38,31,'3','100','1',43);

/*Table structure for table `tb_cloth` */

DROP TABLE IF EXISTS `tb_cloth`;

CREATE TABLE `tb_cloth` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `gender` varchar(50) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `cloth_type` varchar(50) DEFAULT NULL,
  `count` varchar(50) DEFAULT NULL,
  `donor_name` varchar(50) DEFAULT NULL,
  `phoneno` bigint(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `tb_cloth` */

insert  into `tb_cloth`(`id`,`gender`,`age`,`cloth_type`,`count`,`donor_name`,`phoneno`,`email`) values 
(1,'female',23,'def','5','john',1111111111,'john@gmail.com');

/*Table structure for table `tb_complaint` */

DROP TABLE IF EXISTS `tb_complaint`;

CREATE TABLE `tb_complaint` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `complaint` varchar(50) DEFAULT NULL,
  `reply` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=latin1;

/*Data for the table `tb_complaint` */

insert  into `tb_complaint`(`id`,`lid`,`date`,`complaint`,`reply`) values 
(2,2,'2019-10-03','complaint2','reply1'),
(4,9,'2019-11-11','complaint6','pending'),
(5,10,'2019-10-21','complaint5','reply5'),
(6,10,'2019-10-28','complaint6','pending'),
(7,1,'2019-10-29','complaint7','sdds'),
(8,22,'2019-11-06','cjk','kkk'),
(9,22,'2019-11-08','uhhsgsghjjjnbvg','hiooo'),
(10,12,'2019-11-10','nnnnnnnnnnnnnn','pending'),
(12,6,'2019-11-11','ssaaaaass','pending'),
(15,22,'2019-11-14','bdf','kkk'),
(16,22,'2019-11-14','ahhdhjjx','pending'),
(17,22,'2019-11-14','aaaaaaa','pending'),
(18,22,'2019-11-14','hahaha','nnnmm'),
(19,2,'2019-11-22','coooomplntssss','okkk'),
(20,25,'2019-11-25','commmppp','okk');

/*Table structure for table `tb_education` */

DROP TABLE IF EXISTS `tb_education`;

CREATE TABLE `tb_education` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `material_name` varchar(50) DEFAULT NULL,
  `count` varchar(50) DEFAULT NULL,
  `donor_name` varchar(50) DEFAULT NULL,
  `phoneno` bigint(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `tb_education` */

insert  into `tb_education`(`id`,`material_name`,`count`,`donor_name`,`phoneno`,`email`) values 
(1,'book','4','arya',9999999999,'arya123@gmail.com');

/*Table structure for table `tb_event` */

DROP TABLE IF EXISTS `tb_event`;

CREATE TABLE `tb_event` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `crid` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `prgm_name` varchar(50) DEFAULT NULL,
  `details` varchar(50) DEFAULT NULL,
  `photo` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `tb_event` */

insert  into `tb_event`(`id`,`crid`,`date`,`prgm_name`,`details`,`photo`) values 
(1,9,'2019-11-06','prgm1','dt','3_Kurumbar_Nritham_Dance.jpg'),
(2,9,'2019-11-08','dance','xcv','2_Thavala_Kali_Dance.jpg'),
(3,9,'2019-11-08','mnb ','mm ','1_Gadhika_Dance.jpg'),
(4,9,'2019-11-11','dfggghg','uuhhh','aa.png'),
(5,25,'2019-11-28','pgmm','pppphhh','k.png');

/*Table structure for table `tb_familydt` */

DROP TABLE IF EXISTS `tb_familydt`;

CREATE TABLE `tb_familydt` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tid` int(11) DEFAULT NULL,
  `member_name` varchar(50) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `age` varchar(50) DEFAULT NULL,
  `relation_with_head` varchar(50) DEFAULT NULL,
  `position` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `tb_familydt` */

insert  into `tb_familydt`(`id`,`tid`,`member_name`,`gender`,`age`,`relation_with_head`,`position`) values 
(5,11,'memnm1','female','45','rr1','p1'),
(6,11,'memnm2','male','12','son','student');

/*Table structure for table `tb_food` */

DROP TABLE IF EXISTS `tb_food`;

CREATE TABLE `tb_food` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `item_name` varchar(50) DEFAULT NULL,
  `quantity` varchar(50) DEFAULT NULL,
  `donor_name` varchar(50) DEFAULT NULL,
  `phoneno` bigint(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `tb_food` */

insert  into `tb_food`(`id`,`item_name`,`quantity`,`donor_name`,`phoneno`,`email`) values 
(1,'vegetables','100','john',9999999999,'john@gmail.com'),
(2,'bread','50','dfgg',7356786590,'aasa@gmail.com');

/*Table structure for table `tb_login_master` */

DROP TABLE IF EXISTS `tb_login_master`;

CREATE TABLE `tb_login_master` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=latin1;

/*Data for the table `tb_login_master` */

insert  into `tb_login_master`(`lid`,`username`,`password`,`type`) values 
(1,'admin','admin1','admin'),
(2,'neenu','neenu','councillor'),
(3,'swathi','swathi','councillor'),
(4,'shop1','shop1','pending'),
(6,'nn','nn','councillor'),
(7,'nn','nn','councillor'),
(9,'aswin','aswin','coordinator'),
(10,'divya','divya','expertise'),
(12,'teena','teena','volunteer'),
(15,'drishya','drishya','volunteer'),
(22,'anu','anu','public'),
(23,'d@g.com','dd','district'),
(24,'council@g.com','council','councillor'),
(25,'cordin','cordin','coordinator'),
(27,'vvv','vvv','volunteer'),
(29,'xxx','x22','shop'),
(34,'aa','','pending'),
(35,NULL,NULL,NULL),
(37,'aa','aa','pending'),
(38,'aa','aaa','pending'),
(39,'sagar','qwwertyyu','coordinator'),
(42,'b@g.com','1111','public'),
(43,'sumi@gmail.com','aaa','public'),
(44,'','','public'),
(45,'vishal','123','coordinator'),
(46,'amal','12','coordinator');

/*Table structure for table `tb_medicine` */

DROP TABLE IF EXISTS `tb_medicine`;

CREATE TABLE `tb_medicine` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(50) DEFAULT NULL,
  `medicine_name` varchar(50) DEFAULT NULL,
  `dosage` varchar(50) DEFAULT NULL,
  `quantity` varchar(50) DEFAULT NULL,
  `expiry_date` date DEFAULT NULL,
  `donor_name` varchar(50) DEFAULT NULL,
  `phoneno` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `tb_medicine` */

insert  into `tb_medicine`(`id`,`type`,`medicine_name`,`dosage`,`quantity`,`expiry_date`,`donor_name`,`phoneno`,`email`) values 
(1,'Tablet','paracetamol','50','100','2019-09-18','arya','11111111111','arya123@gmail.com'),
(2,'Tablet','paracetamol','25','4','2019-12-27','asdd','9656823298','aaa@gmail.com'),
(3,'Tablet','asdd','52','32','2020-03-06','ghhj','9656884442','qqq@gmail.com');

/*Table structure for table `tb_notification` */

DROP TABLE IF EXISTS `tb_notification`;

CREATE TABLE `tb_notification` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(50) DEFAULT NULL,
  `notification` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `tb_notification` */

insert  into `tb_notification`(`id`,`date`,`notification`) values 
(1,'2019-09-19','notification1'),
(2,'2019-09-27','notifications2'),
(3,'2019-11-11','sdfhj');

/*Table structure for table `tb_package` */

DROP TABLE IF EXISTS `tb_package`;

CREATE TABLE `tb_package` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `package_name` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `tb_package` */

insert  into `tb_package`(`id`,`package_name`,`description`) values 
(2,'package1','hbxhzvcbhjxzbch'),
(3,'packages2','fvbgb');

/*Table structure for table `tb_product` */

DROP TABLE IF EXISTS `tb_product`;

CREATE TABLE `tb_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sid` int(11) DEFAULT NULL,
  `poduct_name` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `quantity` varchar(50) DEFAULT NULL,
  `price` varchar(50) DEFAULT NULL,
  `photos` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `tb_product` */

insert  into `tb_product`(`id`,`sid`,`poduct_name`,`description`,`quantity`,`price`,`photos`) values 
(2,4,'product1','bbxcn','18','20','aYaYi17_nRE1pcz.jpg'),
(3,4,'honey','hbhjb','1','100','last-forest-f-2-1152x603.jpg'),
(4,29,'nnn','kkk','99','900','1.jpeg');

/*Table structure for table `tb_productreq` */

DROP TABLE IF EXISTS `tb_productreq`;

CREATE TABLE `tb_productreq` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cid` int(11) DEFAULT NULL,
  `pid` int(11) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `tb_productreq` */

/*Table structure for table `tb_publicreg` */

DROP TABLE IF EXISTS `tb_publicreg`;

CREATE TABLE `tb_publicreg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fname` varchar(50) DEFAULT NULL,
  `lname` varchar(50) DEFAULT NULL,
  `dob` varchar(25) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `postoffice` varchar(50) DEFAULT NULL,
  `pin` varchar(50) DEFAULT NULL,
  `phoneno` bigint(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=latin1;

/*Data for the table `tb_publicreg` */

insert  into `tb_publicreg`(`id`,`fname`,`lname`,`dob`,`gender`,`place`,`postoffice`,`pin`,`phoneno`,`email`) values 
(1,'arya','kk','2019-10-29','female','vatakara','vatakara','673308',333333,'cxcc'),
(22,'anu','kk','2000-05-07','Female','vtk','vtk','22',6666,'anu@gmail.com'),
(42,'Nam','Last','19111995','Male','Place','Post','7896',8888888,'b@g.com'),
(43,'sumi','sundar','10','Female','calicul','calicut','67654',9656887332,'sumi@gmail.com'),
(44,'','','','Female','','','',0,'');

/*Table structure for table `tb_registration` */

DROP TABLE IF EXISTS `tb_registration`;

CREATE TABLE `tb_registration` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `fname` varchar(50) DEFAULT NULL,
  `lname` varchar(50) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `pin` varchar(50) DEFAULT NULL,
  `contactno` bigint(20) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `qualification` varchar(50) DEFAULT NULL,
  `type` varchar(50) DEFAULT NULL,
  `officer_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;

/*Data for the table `tb_registration` */

insert  into `tb_registration`(`id`,`lid`,`fname`,`lname`,`dob`,`gender`,`place`,`post`,`pin`,`contactno`,`email`,`qualification`,`type`,`officer_id`) values 
(1,2,'neenu','chandran','1996-04-05','female','vatakara','chombala','673308',8606628534,'neenuc5496@gmail.com','SSLC,PLUSTWO,UG','councillor',NULL),
(3,9,'aswin','pk','2019-10-11','male','kunnummakkara','chombala','673308',6666666666,'aswin@gmail.com','SSLC,PLUSTWO,UG','coordinator',NULL),
(4,10,'Divya','k k','1990-07-19','female','kannur','kannursouth','22222',86066256787,'divya@gmail.com','SSLC,PLUSTWO,UG,PG','expertise',NULL),
(6,12,'teena','p s','1999-03-02','female','kannur','kannur','66',888888,'teena@gmail.com','SSLC,PLUSTWO,UG','volunteer',NULL),
(9,15,'drishya','m','2019-10-31','female','koyilandi','koyilandi','999',7777,'dri@gmail.com','SSLC,PLUSTWO,UG','volunteer',NULL),
(10,23,'first','last','2019-11-21','female','kozhikode','post','555555',9999999999,'d@g.com','UG,PG','district',NULL),
(11,24,'council','coun','2019-11-29','female','place','office','777777',9999999999,'council@g.com','UG,PG','councillor',23),
(12,25,'cordiantr','cordin','2019-11-20','male','pace','posr','888888',9999999999,'co@g.com','PG','coordinator',6),
(13,27,'fname','lnmae','2019-11-21','Female','place','post','888888',9999999999,'voll@g.com','PLUSTWO,UG','volunteer',0),
(15,29,'admin','coun','2019-11-19','Male','place','office','888888',9999999999,'vol2l@g.com','SSLC','volunteer',0),
(16,39,'vidhya','sagar','1990-10-06','male','calicut','sdfghgh','456872',9656882211,'gfsg@gmail.com','SSLC,PLUSTWO,UG','coordinator',6),
(17,45,'vishal','k','2019-11-22','male','calicut','calicut','785864',9988770055,'vishal@gmail.com','PG','coordinator',2),
(18,46,'amal','jith','2019-11-06','male','calicut','calicut','678898',9988770055,'amal@gmail.com','PG','coordinator',3);

/*Table structure for table `tb_report` */

DROP TABLE IF EXISTS `tb_report`;

CREATE TABLE `tb_report` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `tribe_area` varchar(50) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  `report` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `tb_report` */

insert  into `tb_report`(`id`,`lid`,`date`,`tribe_area`,`title`,`report`) values 
(2,2,'2019-10-03','tribearea2','title2','Diagram1.png'),
(3,9,'2019-10-20','tribeareas3','title3','er1.jpeg'),
(4,24,'2019-10-22','tribearea4','titless4','Diagram1.png'),
(5,25,'2019-11-10','nnn','sas','cv2-red-channel.png'),
(6,2,'2019-11-22','moodadi','sdfsdsdf','add_sub.html'),
(7,3,'2019-11-25','calicut','hkgk','k.png'),
(8,25,'2019-11-25','calicut','ghfg','cldd.png'),
(9,46,'2019-11-25','thiroor','dfsgf','ERmentor.png');

/*Table structure for table `tb_servicereq` */

DROP TABLE IF EXISTS `tb_servicereq`;

CREATE TABLE `tb_servicereq` (
  `rid` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `tribearea` varchar(50) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  `request` varchar(1000) DEFAULT NULL,
  `service` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`rid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `tb_servicereq` */

insert  into `tb_servicereq`(`rid`,`lid`,`date`,`tribearea`,`title`,`request`,`service`) values 
(1,9,'2019-10-09','calicut','title1','naturewallpaper.jpeg','Diagram1.png'),
(2,9,'2019-10-20','tribeareas2','titlee2','aYaYi17_nRE1pcz.jpg','pending'),
(3,25,'2019-11-10','newser','new','health.pdf','1.jpg'),
(4,25,'2019-11-10','ddddd','yyy','cv2-red-channel.png','pending');

/*Table structure for table `tb_shopreg` */

DROP TABLE IF EXISTS `tb_shopreg`;

CREATE TABLE `tb_shopreg` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `shopname` varchar(50) DEFAULT NULL,
  `place` varchar(50) DEFAULT NULL,
  `post` varchar(50) DEFAULT NULL,
  `pin` varchar(50) DEFAULT NULL,
  `contactno` bigint(20) DEFAULT NULL,
  `lid` int(11) DEFAULT NULL,
  `licenceno` varchar(30) DEFAULT NULL,
  `ownername` varchar(50) DEFAULT NULL,
  `username` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `tb_shopreg` */

insert  into `tb_shopreg`(`id`,`shopname`,`place`,`post`,`pin`,`contactno`,`lid`,`licenceno`,`ownername`,`username`) values 
(1,'Midunam','vatakara','vatakara','673308',333333,4,NULL,NULL,NULL),
(2,'\"+shophome+\"','\"+place+\"','\"+post+\"','\"+pin+\"',0,0,'\"+str(lid)+\"','\"+ownername+\"','\"+Username+\"'),
(3,'admin','coun','post','888888',9999999999,0,'34','xxx','aa'),
(4,'nnn','nn','post','888888',9999999999,37,'d@g.com','cordin','aa'),
(5,'council@gmail.com','coun','post','888888',22222222,38,'1111','vvv','aa');

/*Table structure for table `tb_tribeinfo` */

DROP TABLE IF EXISTS `tb_tribeinfo`;

CREATE TABLE `tb_tribeinfo` (
  `tid` int(11) NOT NULL AUTO_INCREMENT,
  `crid` int(11) DEFAULT NULL,
  `tribe_area` varchar(50) DEFAULT NULL,
  `name` varchar(50) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `gender` varchar(50) DEFAULT NULL,
  `position` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`tid`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `tb_tribeinfo` */

insert  into `tb_tribeinfo`(`tid`,`crid`,`tribe_area`,`name`,`age`,`gender`,`position`) values 
(11,9,'tribearea2','name2',78,'male','position2'),
(12,9,'scdc','xvvcxvk',22,'female','xvc '),
(13,9,'asffgggh','ssaa',0,'male','hhj'),
(14,25,'ggg','jhjhjj',45,'male','hkkj');

/*Table structure for table `tb_tribeproblem` */

DROP TABLE IF EXISTS `tb_tribeproblem`;

CREATE TABLE `tb_tribeproblem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) DEFAULT NULL,
  `tribe_area` varchar(50) DEFAULT NULL,
  `problem_name` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;

/*Data for the table `tb_tribeproblem` */

insert  into `tb_tribeproblem`(`id`,`lid`,`tribe_area`,`problem_name`,`description`) values 
(1,22,'ghjb','cffhh','GGFCC'),
(2,22,'calicut','nnmm','ggafscsh'),
(3,12,'admin','coun','kjkhk'),
(4,12,'dfghhjk','assd','tuhhhlkuio'),
(6,22,'','',''),
(7,22,'26727','gsghsusu','267e81829'),
(8,22,'aa','fghjj','sfgjk'),
(9,22,'','',''),
(11,27,'thiroor','no water','big crisis\r\n');

/*Table structure for table `tb_updonation` */

DROP TABLE IF EXISTS `tb_updonation`;

CREATE TABLE `tb_updonation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(50) DEFAULT NULL,
  `tribe_area` varchar(50) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  `description` varchar(50) DEFAULT NULL,
  `report` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `tb_updonation` */

insert  into `tb_updonation`(`id`,`type`,`tribe_area`,`date`,`description`,`report`) values 
(1,'education material','calicut','2019-10-11','gvtftgfy','er1.jpeg'),
(2,'cloth','kannur','2019-10-03','dcfc','1.jpeg');

/*Table structure for table `tb_work` */

DROP TABLE IF EXISTS `tb_work`;

CREATE TABLE `tb_work` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vid` int(11) DEFAULT NULL,
  `crid` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `tribearea` varchar(50) DEFAULT NULL,
  `work_details` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `tb_work` */

insert  into `tb_work`(`id`,`vid`,`crid`,`date`,`tribearea`,`work_details`) values 
(1,12,9,'2019-10-30','kannur','workdt1'),
(2,15,9,'2019-10-30','kuttyadi','dsvcfv');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
