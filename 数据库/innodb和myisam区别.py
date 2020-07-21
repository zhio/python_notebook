"""
MySQL的两种存储引擎 InnoDB 和 MyISAM 的区别？
	InnoDB支持事务，可以进行Commit和Rollback；
	MyISAM 只支持表级锁，而 InnoDB 还支持行级锁，提高了并发操作的性能；
	InnoDB 支持外键；
	MyISAM 崩溃后发生损坏的概率比 InnoDB 高很多，而且恢复的速度也更慢；
	MyISAM 支持压缩表和空间数据索引，InnoDB需要更多的内存和存储；
	InnoDB 支持在线热备份

"""