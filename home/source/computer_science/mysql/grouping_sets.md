# MySQL的`group`技巧实现CUBE之类的OLAP概念

MySQL对OLAP的支持不是很好，要使用高低维度同时`group by`操作，则要使用关键词`ROLLUP`（`<5.8`版本也支持），但似乎没有找到可选维度，得所有维度都进行下钻之类的操作。

```mysql
SELECT
    a,
    b,
    count(*)
FROM
    example_table
FROM
    a, b ROLLUP
```