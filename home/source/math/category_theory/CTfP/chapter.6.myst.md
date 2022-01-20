# 第6章 简单的代数数据类型

## 6.1 Product Types

Pairs是最基本的组合类型。而Nesting Pair是同构的，因为可以找到一个方法可以回到组合。

```python
from typing import TypeVar
S = TypeVar("S")
T = TypeVar("T")
U = TypeVar("U")

def convert_pair(x: Tuple[Tuple[S, T], U]) -> Tuple[S, Tuple[T, U]]:
    return (x[0][0], (x[0][1], x[1]))
```

同样我们也可以知道`(a, ())`和`a`也是同构的，因为我们可以写出一个取出首个元素的函数：

```python
def first(x: Tuple[S, Tuple[]]) -> S:
    return x[0]
```

从头定义`Pair`:

```python
from abc import ABC
from dataclasses import dataclass
from typing import Generic


class Pair(ABC, Generic[S, T]):
    pass

@dataclass
class P(Pair, Generic[S, T]):
    a: S
    b: T
```

定义`stmt`:

```python
stmt: Pair[str, bool] = P("This statement is", False)
```

## 6.2 Records

即`Python`中的`dataclass`

## 6.3 Sum Types

```python
class Either(Generic[S, T]):
    pass

@dataclass
class Left(Either, Generic[S, T]):
    v: S

@dataclass
class Right(Either, Generic[S, T]):
    v: T
```

此外，还可以实现三元组的类型。另外枚举也可以作为Sum类型中的一个。

## 6.4 类型的代数

Sum和Product类型和数学上的sum和product一样，符合分配率的同构性：

```python
## type left
P[S, Either[T, U]]

## type right
Either[P(S, T), P(S, U)]
```

我们可以写转换函数
```python
def prod_to_sum(x: P[S, Either[T, U]]) -> Either[P[S, T], P[S, U]]:
    if isinstance(x.b, Left):
        return Left(P(x.a, x.b.v))
    else:
        return Right(P(x.a, x.b.v))
```

如何可以用类型类比数字：

|    数字     |                 类型                  |
| :---------- | :------------------------------------ |
| $0$         | `Void`                                |
| $1$         | `()`                                  |
| $a + b$     | `Either[A, B]` / `Left A` / `Right B` |
| $a\times b$ | `Pair[A, B]`                          |
| $2 = 1 + 1$ | `bool` / `True` / `False`             |
| $1 + a$     | `Option[A]` / `Some[A]` / `Nothing`   |

而`List`可以看成$x = 1 + a * x$的类型，当我们替换`List[A]`成`x`(`List a = Nil | Cons A (List a)`)：

```python
class CustomList(Generic[S]):
    pass

@dataclass
class Nil(CustomList):
    pass

@dataclass
class Cons(CustomList, Generic[S]):
    head: S
    tail: CustomList[S]
```

逻辑运算也可以转化为类型术语

|    逻辑     |         类型                   |
| :---------- | :---------------------------- |
| $false$     | `Void`                        |
| $true$      | `()`                          |
| $a \lor b$  | `Either a b = Left a \| Right b` |
| $a \land b$ | `(a, b)`                      |


## 6.5 习题

```{toctree}
---
maxdepth: 1
---

chapter.6.code
```