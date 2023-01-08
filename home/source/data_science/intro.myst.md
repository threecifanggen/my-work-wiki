---
html_meta:
    "description": "数据科学相关汇总"
    "author": "黄宝臣, 3gee, threecifanggen"
    "keywords": "3gee, threecifanggen, 工作百科, 数据科学, 计算机科学, 黄宝臣"
    "property=og:locale": "zh_CN"
---
# 数据科学相关汇总

在工作中，除了会遇到我们常见的大数据问题（更多是工程层面的问题），大部分需要
动脑筋的反而是数据量不大的情况。这感觉也是我工作的价值，套用解决方案，其实对
于一个数据科学家而言仅仅是基本要求，大部分的实际问题都是不可直接找到解决方案
的，或者在直接方案下有缺憾的（即没有理论支持）的工作。这是我在各种层面做努力
的地方，如何用数据科学/数学思维解决一个传统上没法套用的领域或问题；或者，在
一个缺乏理论支持的解决方案中找到可以让流程/工作/解决方案更具科学性的方法。


:::{graphviz}
digraph G {
    rankdir="LR"
    node [shape=box]
    数据量 -> 微数据
    数据量 -> 小数据
    数据量 -> 大数据

    微数据 -> "假设/仿真/模拟"

    小数据 -> "描述性统计/统计推断/机器学习"

    大数据 -> "数据工程/描述性统计/深度学习"
}
:::
## 进一步阅读

```{toctree}
---
maxdepth: 1
---
wideviews_of_ds
recommender/intro
deep_learning/intro
numerical_planning/intro
ab_test/intro
simulation/intro
CASI/intro
audio_analysis/intro
or_tools/intro
medicine_stat/intro
```