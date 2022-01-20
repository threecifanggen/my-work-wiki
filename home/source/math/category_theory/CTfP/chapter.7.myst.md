# 第7章 函子

## 7.0 简介

函子是一个非常简单却强大的概念，它表达的是「范畴」之间的映射。例如我们有个变形(morphism)在$C$中，将对象$a$和对象$b$之间联通：

$$
f:: a \rightarrow b
$$(7.1)

则我们可以做一个$f$在$D$中的镜像$Ff$，可以把$a$、$b$的镜像沟通起来：

$$
Ff:: Fa \rightarrow Fb
$$(7.2)

```{figure} assets/img/2022-01-20-16-48-09.png
---
name: Functor图示
align: center
---

Functor图示
```

函子也符合组合原则，即如果，

$$
h = g.f
$$

则：

$$
Fh = Fg.Ff
$$

```{figure} assets/img/2022-01-20-16-59-15.png
---
name: 函子组合
align: center
---

函子组合
```

## 7.1 编程中的函子

### 7.1.1 `Maybe`函子

```haskell
data Maybe a = Nothing | Just a
```

```scala
sealed trait Option[+A]
case object None extends Option[Nothing]
case class Some[A](a: A) extends Option[A]
```

```python
class Maybe(Generic[S]):
    pass

@dataclass
class Nothing(Maybe):
    pass

@dataclass
class Some(Maybe, Generic[S]):
    s: S
```


如此我们可以实现一个函数的映射：

```haskell
f' :: Maybe a -> Maybe b
f' Nothing = Nothing
f' (Just x) = Just (f x)
```

```scala
def f1[A, B]: Option[A] => Option[B] = {
case None => None
case Some(x) => Some(f(x))
}
```

```python
def f1(f: Callable[[Maybe[S]], Maybe[T]], x: Maybe[S]) -> Maybe[T]:
    if isinstance(x, Nothing):
        return Nothing()
    else:
        return Some(f(x.s))
```

```{figure} assets/img/2022-01-20-17-18-10.png
---
name: haskell中非fmap 
align: center
---

haskell中非fmap
```

```python
def fmap(f: Callable[[S], T]) -> Callable[[Maybe[S]], Maybe[T]]:
    def helper(x: Maybe[S]):
        if isinstance(x, Nothing):
            return Nothing()
        else:
            return Some(f(x.s))
    return helper
```

### 7.1.2 公式推理

主要可以形式化验证单位元特性以及组合特性。

### 7.1.3 Typeclasses



## 代码实现与习题



```{toctree}
---
maxdepth: 1
---

chapter.7.code
chapter.7.asignment
```