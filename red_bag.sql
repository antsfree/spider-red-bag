CREATE TABLE `red_bag` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `sign` varchar(50) NOT NULL DEFAULT '',
  `red_bag_id` varchar(50) NOT NULL DEFAULT '',
  `uid` varchar(50) NOT NULL DEFAULT '',
  `money` varchar(50) NOT NULL DEFAULT '',
  `stock_num` varchar(50) NOT NULL DEFAULT '',
  `type` varchar(5) NOT NULL DEFAULT '2',
  PRIMARY KEY (`id`),
  KEY `money` (`money`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=latin1;