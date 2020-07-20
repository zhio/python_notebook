"""
多版本并发控制，主要解决提交读，可重复读，可以解决幻读的问题。
innodb MVCC实现
每行都有DATA_TRX_ID（记录最近更新的事务ID）和DATA_ROLL_PTR（回滚指针）两个隐藏的列
"""