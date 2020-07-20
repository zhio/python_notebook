"""
分为全量复制和部分复制

全量复制过程

Redis 内部会发出一个同步命令，刚开始是 Psync 命令，Psync  -1表示要求 master 主机同步数据
主机会向从机发送 runid 和 offset，因为 slave 并没有对应的 offset，所以是全量复制
从机 slave 会保存 主机master 的基本信息 save masterInfo
节点收到全量复制的命令后，执行bgsave（异步执行），在后台生成RDB文件（快照），并使用一个缓冲区（称为复制缓冲区）记录从现在开始执行的所有写命令
主机send RDB 发送 RDB 文件给从机
发送缓冲区数据
刷新旧的数据，从节点在载入主节点的数据之前要先将老数据清除
加载 RDB 文件将数据库状态更新至主节点执行bgsave时的数据库状态和缓冲区数据的加载。

部分复制过程

如果网络抖动（连接断开 connection lost）
主机master 还是会写 replbackbuffer（复制缓冲区
从机slave 会继续尝试连接主机
从机slave 会把自己当前 runid 和偏移量传输给主机 master，并且执行 pysnc 命令同步
如果 master 发现你的偏移量是在缓冲区的范围内，就会返回 continue 命令

"""