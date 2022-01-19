# 第5章 各种运输模型

## 5.1 运输模型的定义

用边和节点定义：

```{graphviz}
digraph G {
    rankdir="LR"
    start_1 [label="1" shape=circle]
    start_2 [label="2" shape=circle]
    start_m [label="m" shape=circle]
    end_1 [label="1" shape=circle]
    end_2 [label="2" shape=circle]
    end_n [label="n" shape=circle]
    a1 [color="white"]
    a2 [color="white"]
    am [color="white"]
    b1 [color="white"]
    b2 [color="white"]
    bn [color="white"]
    a1 -> start_1
    a2 -> start_2
    am -> start_m
    start_1 -> end_1 
    start_1 -> end_2
    start_1 -> end_n
    start_2 -> end_1
    start_2 -> end_2
    start_2 -> end_n
    start_m -> end_1
    start_m -> end_2
    start_m -> end_n
    end_1 -> b1
    end_2 -> b2
    end_n -> bn
}
```

## 5.2 非传统运输模型

```{toctree}
---
maxdepth: 1
---

chapter.5.code
```