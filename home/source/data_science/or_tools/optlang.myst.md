---
html_meta:
    "description": "Python线性规划工具optlang"
    "author": "黄宝臣, 3gee, threecifanggen"
    "keywords": "optlang, Python, 线性规划, 3gee, threecifanggen, 工作百科, 数据科学, 计算机科学, 黄宝臣"
    "property=og:locale": "zh_CN"
---
# Python线性规划工具`optlang`

`optlang`类似`sympy`的一种线性规划的DSL的语言，主要是分为`Model`, `Variable`, `Constraint`, `Objective`这五部分。

## `Variable`

`Variable`是指定线性规划变量的对象，类似`sympy`中的`Symbol`。我们可以对其指定上下限(`lb`/`ub`)，例如下面就是指定一个名为`x`的变量，下限为`0`上限无穷的变量：

```python
x = Variable("x", lb=0)
```

## `Constraint`

`Constraint`则是指定约束，即线性规划中的($s.t.$)部分，此部分可以利用`Variable`的变量实现`sympy`中的符号运算式子，下面表示约束$1 \le 2x + 1\le 5$。

```python
c = Constraint(2 * x + 1, lb=1, ub=5)
```

## `Objective`

`Objective`则表示优化函数，`direction`表示是向最大值优化还是最小值优化：

```python
obj = Objective(5 - 4 * x, direction="max")
```

## `Model`

最后`Model`就是用以优化的所有函数，下面是优化即输出结果的方式。

```python
model = Model(name='Test Model') # 创建模型及命名
model.objective = obj # 增加目标函数
model.add([c]) # 增加约束

status = model.optimize()
print("status:", model.status)
print("objective value:", model.objective.value)
print("----------")
for var_name, var in model.variables.iteritems():
    print(var_name, "=", var.primal)
```
