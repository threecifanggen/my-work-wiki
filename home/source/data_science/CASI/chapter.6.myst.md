# 第六章 经验贝叶斯

```{seealso}
相关内容参考[这个Jupyter Notebook](chapter.6.jupyter)。
```

## 6.1 Robbin公式

```{list-table} 索赔频率
---
header-rows: 1
---
* - 索赔次数($x$)
  - 0
  - 1
  - 2
  - 3
  - 4
  - 5
  - 6
  - 7
* - 人数($y_x$)
  - 7840
  - 1317
  - 239
  - 42
  - 14
  - 4
  - 4
  - 1
```

研究欧洲汽车保险一年内索赔数量，假设有$k$个人在一年索赔次数x为$\theta_k$的泊松分布，即：


$$
Pr(x_k = x) = p_{\theta_k} (x) = 
    \frac {e^{-\theta_k \theta_k^x}} {x!}
$$(6.1)

```{note}
这里用到了以下几个知识：

第一个是贝叶斯定理

$$
P(\theta | x) = \frac {P(x|\theta) P(\theta)} {P(x)} = 
    \frac {P(x|\theta) P(\theta)} {\sum P(x|\theta) P(\theta)}
$$(6.1.1)

第二个是期望的求法:

$$
E(f(x)) = \frac {\int f(x)P(x) dx} {\int P(x) dx}
$$(6.1.2)

最后，$P(x|\theta) = p_{\theta}(x)$，$P(\theta) = g(\theta)$

```

如果知道顾客的$\theta$值的先验分布$g(\theta)$，则可以写出索赔次数$x$的期望为

$$
E\{\theta|x\} = \frac 
    {\int^{\infty}_0 \theta p_{\theta}(x)g(\theta)d\theta}
    {\int^{\infty}_0 p_{\theta}(x)g(\theta)d\theta}
$$(6.2)

由 {eq}`6.1` 和 {eq}`6.2` 可以推出下面的结果：

$$
E\{\theta|x\} = \frac 
    {\int^{\infty}_0[\frac{e^{-\theta}\theta ^ {x + 1}}{(x+1)!}]g(\theta)d\theta}
    {\int^{\infty}_0[\frac{e^{-\theta}\theta ^ {x}}{(x)!}]g(\theta)d\theta}
$$(6.3)

我们可以把泊松分布的部分的积分定义为:

$$
f(x) = \int^{\infty}_0\frac {e^{-\theta_k \theta_k^x}} {x!} g(\theta)d\theta
$$(6.4)

```{note}
$f(x)$其实就是$P(x)$
```

将 {eq}`6.4` 带入到 {eq}`6.3` 可得

$$
E\{\theta|x\} = \frac {(x + 1) f(x+1)} {f(x)}
$$(6.5)

这样的好处就是，我们可以不对$g(\theta)$做任何假设，也可以推断出来，常用的推断方式就是

$$
\hat{f}(x) = y_x / N
$$(6.6)

即出现x次的次数占总人数的比例，比如上面的例子中，9461人中7840人没有索赔，1317人索赔1次，则我们可以计算$\hat{f}(0) = 7840/9461$，$\hat{f}(1) = 1317/7480$

而最终版本，是不需要$N$出现的：

$$
\hat{E} \{\theta | x\} = \frac {(x + 1) \hat{f}(x+1)} {\hat{f}(x)} =
    \frac {(x + 1) y_{x+1}} {y_x}
$$(6.7)

{eq}`6.7` 就是Rubbin公式，所以可以算出一年内提出0次索赔第二年索赔的次数的期望为0.168。

### 改进

这个方案不好在于，由于后面的观测量很小，数据波动很大。现在假设$g(\theta)$符合GAMMA形式：

$$
g(\theta) = \frac
    {\theta ^ {\nu - 1} e ^ {-\frac{\theta}{\sigma}}}
    {\sigma ^ {\nu}\Gamma(\nu)}, \;\; \theta \ge 0
$$(6.8)

可以通过拼数有关的$y_x$的最大似然法得到$\sigma$和$\nu$。

```{note}
带入$g(\theta)$到 {eq}`6.1` 中，可以化简

$$
f_{\nu, \sigma}(x) = \frac 
    {\gamma ^{\nu + x} \Gamma (\nu + x)}
    {\sigma ^{\nu} \Gamma (\nu ) x !}
$$(6.8.1)

然后，可以$P(x) = f(x)$，所以按照每个用户可以算出概率积。例如次数为0的人数为7840人，则这7840人的概率积为$(f_{\nu, \sigma}(0)) ^ {7840}$。所以最后优化$log$后的MLE函数为

$$
\underset{\nu, \sigma}{argmax}\{\sum^{x_{max}}_{x = 0}y_x log f_{\nu, \sigma}(x)\}
$$
```

然后可以得到：

$$
\hat{y} (x) = f_{\hat{\nu}, \hat{\sigma}}(x)
$$(6.9)

或等价形式$\hat{y}_x = N f_{\hat{\nu}, \hat{\sigma}}(x)$


## 参考`Notebook`

```{toctree}
---
maxdepth: 1
---

chapter.6.jupyter.ipynb
```