# MessageQueue

基于Redis实现简易MessageQueue
- 基于 List 实现队列功能
- 基于 pub/sub 实现消息通知
- 基于 Set 实现 ack
- threading

Usage:
```Python
	python run.py
```

client/client.py 用于模拟生产者产生数据
