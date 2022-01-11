# Actor模型

## 基本介绍

Actor模型用来解决多线程的锁的问题，这个模型抽象：

1. 程序由一个个Actor组成；
2. Actor通过Message传递消息，并基于类型系统来判断要做的事，这里要求Actor需要有个Address的概念；
3. Actor在接受到Message时可以同时做以下事：
    * 发送Message给别的Actor
    * 创建新的Actor
    * 决定下次接收到Message时会如何处理数据

Address可以由以下方式实现：

1. 直接的物理设备
2. 内存或者硬盘地址
3. 网络地址
4. email地址

## 常见应用

1. Email系统是标准的Actor系统，邮件账户就是Actor而Email地址就是Actor Address；
2. 网络服务使用SOAP也可以被看做是Actor address；
3. 用锁的对象都可以以Actor建模。

## 本地性和安全性

本地性(Locality)和安全性(Security)要求Actor承诺止发送下面方式产生的信息：

1. 它接受到的消息；
2. 它在接受消息前已经有的消息；
3. 它在处理消息时创造的消息；




## 参考文献

1. Hewitt, C. (2010). Actor model of computation: scalable robust information systems. *arXiv preprint* arXiv:1008.1459. 	