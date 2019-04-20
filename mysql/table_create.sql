/* 表创建脚本 */

#创建database
create database inventory_management;
use inventory_management;

/* 创建表 */
#错误信息表
create table `error_code_info` (
	`error_kind` int unsigned not null auto_increment primary key,
	`error_des` varchar(50)
)engine=InnoDB default charset=utf8;
alter table `error_code_info` add unique (`error_kind`);
alter table `error_code_info` add index (`error_kind`);

#注册码
create table `reg_code` (
	`code_id` int unsigned not null auto_increment primary key,
	`code` varchar(8)
)engine=InnoDB default charset=utf8;
alter table `reg_code` add unique (`code_id`);
alter table `reg_code` add index (`code_id`);

#扭蛋类型表
create table `egge_data` (
	`egge_kind` int unsigned not null auto_increment primary key,
	`egge_des` varchar(50)
)engine=InnoDB default charset=utf8;
alter table `egge_data` add unique (`egge_kind`);
alter table `egge_data` add index (`egge_kind`);

#商场表
create table `shop` (
	`shop_id` int unsigned not null auto_increment primary key,
	`shop_province` varchar(30),
	`shop_city` varchar(30),
	`shop_name` varchar(30),
	`shop_des` varchar(300)
)engine=InnoDB default charset=utf8;
alter table `shop` add unique (`shop_id`);
alter table `shop` add index (`shop_id`);

#兑币机表
create table `coin_machine` (
	`machine_id` int unsigned not null auto_increment primary key,
	`shop_id` int unsigned not null,
	`accurate_position` varchar(50),
	`coin_num` int unsigned not NULL,
	`key_state` int,
	foreign key(shop_id) references shop(shop_id)
)engine=InnoDB default charset=utf8;
alter table `coin_machine` add unique (`machine_id`);
alter table `coin_machine` add index (`machine_id`);

#扭蛋机表
create table `egg_machine` (
	`egg_machine_id` int unsigned not null auto_increment primary key,
	`machine_id` int unsigned not null,
	`egges_num` int unsigned,
	`egge_kind` int unsigned,
	`error_kind` int unsigned,
	`err_time` date,
	foreign key(machine_id) references coin_machine(machine_id),
	foreign key(error_kind) references error_code_info(error_kind),
	foreign key(egge_kind) references egge_data(egge_kind)
)engine=InnoDB default charset=utf8;
alter table `egg_machine` add unique (`egg_machine_id`);
alter table `egg_machine` add index (`egg_machine_id`);

#用户和密码
create table `users` (
	`user_id` int unsigned not null auto_increment primary key,
	`user_name` varchar(30),
	`passwd` varchar(30),
)engine=InnoDB default charset=utf8;