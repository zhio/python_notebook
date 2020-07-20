"""
Redis中的哨兵服务器是一个运行在哨兵模式下的Redis服务器，核心功能是监测主节点和从节点的运行情况，在主节点出现故障后， 
完成自动故障转移，让某个从节点升级为主节点。

自动故障转移流程
认定主节点主观下线（因为每隔2s，哨兵节点会给主节点发送PING命令，如果在一定时间间隔内，都没有收到回复，那么哨兵节点就认为主节点主观下线。
）
认定主节点客观下线
哨兵节点认定主节点主观下线后，会向其他哨兵节点发送sentinel is-master-down-by-addr命令，获取其他哨兵节点对该主节点的状态，当认定主节点下线的哨兵数量达到一定数值时，就认定主节点客观下线。

领导者选举
所有哨兵节点A会先其他哨兵节点，发送命令，申请成为该哨兵节点B的领导者，如果B还没有同意过其他哨兵节点，那么就同意A成为领导者，最终得票超过半数以上的哨兵节点会赢得选举，如果本次投票，没有选举出领导者哨兵，那么就开始新一轮的选举，直到选举出哨兵节点（实际开发中，最先判定主节点客观下线的哨兵节点，一般就能成为领导者。）
领导者哨兵节点首先会从从节点中选出一个节点作为新的主节点。选择的规则是：

领导者进行故障转移
1.首先排除一些不健康的节点。（下线的，断线的，最近5s没有回复哨兵节点的INFO命令的，与旧的主服务器断开连接时间较长的）

2.然后根据优先级，复制偏移量，runid最小，来选出一个从节点作为主节点。

向这个从节点发送slaveof no one命令，让其成为主节点，通过slaveof 命令让其他从节点成为它的从节点，将已下线的主节点更新为新的主节点的从节点。

"""

import copy


dic = {"a": [1, 3, 5]}

b = copy.copy(dic)
c = copy.deepcopy(dic)
b['a'].append(7)
c['a'].append(9)
print(dic)
print(b)
print(c)


