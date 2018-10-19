CREATE TABLE `red_bag` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `sign` varchar(50) CHARACTER SET utf8mb4 NOT NULL DEFAULT '',
  `red_bag_id` varchar(50) CHARACTER SET utf8mb4 NOT NULL DEFAULT '',
  `uid` varchar(50) CHARACTER SET utf8mb4 NOT NULL DEFAULT '',
  `money` varchar(50) CHARACTER SET utf8mb4 NOT NULL DEFAULT '',
  `stock_num` varchar(50) CHARACTER SET utf8mb4 NOT NULL DEFAULT '',
  `type` varchar(5) CHARACTER SET utf8mb4 NOT NULL DEFAULT '2',
  PRIMARY KEY (`id`),
  KEY `money` (`money`)
) ENGINE=InnoDB AUTO_INCREMENT=7173 DEFAULT CHARSET=latin1;

CREATE TABLE `user_info` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `uid` varchar(100) CHARACTER SET utf8mb4 NOT NULL DEFAULT '' COMMENT '用户ID',
  `user_name` varchar(100) CHARACTER SET utf8mb4 DEFAULT '' COMMENT '用户名',
  `authorization` varchar(255) CHARACTER SET utf8mb4 NOT NULL DEFAULT '',
  `cookie` text CHARACTER SET utf8mb4 NOT NULL,
  `longitude` varchar(255) CHARACTER SET utf8mb4 NOT NULL DEFAULT '',
  `latitude` varchar(255) CHARACTER SET utf8mb4 NOT NULL DEFAULT '',
  `is_delete` varchar(1) CHARACTER SET utf8mb4 NOT NULL DEFAULT '0' COMMENT '删除状态',
  PRIMARY KEY (`id`),
  KEY `uid` (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;