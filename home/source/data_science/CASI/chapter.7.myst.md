# 第七章 James-Stein估计和岭回归

## 7.1 James-Stein估计

```{admonition} James-Steain定理
假设

$$
x_i | \mu_i \sim \mathbb{N}(\mu_i, 1)
$$(7.1)

相互独立。其中$i = 1, 2, ..., N$且$N \ge 4$。那么

$$
E\{|| \hat{\boldsymbol{\mu}} ^ {JS} - \boldsymbol{\mu}||^2\} < N = E\{|| \hat{\boldsymbol{\mu}} ^ {MLE} - \boldsymbol{\mu}||^2\} 
$$(7.2)

对于$\boldsymbol{\mu} \in \mathbb{R}^N$的所有选择。
```

### James-Stein的后果

方程 {eq}`7.2` 中表面，不管$\boldsymbol{\mu}$取何值，只要维度超过3，$MLE$的风险都无法控制越来越多，而JS定理则很好地控制了风险。这个在1961年造成了巨大冲击，大家对MLE产生了巨大的失望。

## 7.3 岭回归

岭回归的目标是一种收缩算法，其表达式可以表示为

$$
\hat{\beta}(\lambda) = (\boldsymbol{S} + \lambda \boldsymbol{I}) ^{-1} \boldsymbol{X}'y 
    = (\boldsymbol{S} + \lambda \boldsymbol{I})^{-1}\boldsymbol{S}
\hat {\beta}$$(7.3)

早期对岭回归的研究是频率派的方法。而贝叶斯也有个理论版本，即假设：

$$
\hat{\beta} = \mathbb{N}_p(\beta, \sigma ^ 2 \boldsymbol{S})
$$(7.4)

之后则产生了一个称为Lasso回归的估计量。

JS定理可以给出一个新的估计量，表示为：

$$
\hat{\beta} ^ {JS} = [ 1 - \frac {(p - 2)\sigma ^2} {\hat{\beta}' \boldsymbol{S} \hat{\beta}}] \hat{\beta}
$$(7.5)

在$p\ge 3$时，可以保证

$$
E\{|| \hat{\boldsymbol{\mu}} ^ {JS} - \boldsymbol{\mu}||^2\} < p\sigma ^ 2
$$(7.6)

而岭回归没有这样的保证，也没有选择$\lambda$的万无一失的想法。