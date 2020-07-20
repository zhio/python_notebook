## 简述下kafka架构

```text
kafkas是一个分布式，基于发布订阅模式的消息系统。一个典型的kafka集群包含若干个producer，若干个broker，若干个consumer group 和一个zookeeper集群，kafka通过zookeeper管理集群配置，选举leader，consumer group发生变化是时进行再均衡，producer通过push模式向broker推送消息，consumer通过pull模式从broke订阅并消费消息
```

## kafka高吞吐原理

```reStructuredText
1、顺序写磁盘，省去了磁盘寻址时间
2、零拷贝技术
3、分区可以横向扩展和高并发
4、数据压缩和批次方式发送，减少了IO次数
```

## kafka怎么保证消息不重复消费

```reStructuredText
保证消息队列消费幂等性
结合业务场景分析
1、比如消息写数据库，拿主键去查询一下，如果数据有了，抛弃
2.如果写redis set类型天然幂等性
```

## kafka怎么保证不丢消息

``````
1、消费者丢数据
问题：kafka会自动提交offset，让 Kafka 以为你已经消费好了这个消息，但其实你才刚准备处理这个消息，你还没处理，你自己就挂了，此时这条消息就丢了
解决：关闭自动提交，改为手动提交offset
2、kafka丢失数据
问题：
解决：
``````

