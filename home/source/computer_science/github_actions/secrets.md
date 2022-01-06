# 加密变量

## 缘起

部分`workflow`可能涉及数据库、一些发布平台账号/token等值，直接写在项目中会非常不安全。我自己使用到的情况就是发布到`PYPI`，这个就需要一个用户TOKEN不可能暴露在项目中；此外，我也希望在合并分支时，也会同时`git push`一份到`Gitee`。这也会用到`Gitee`的token的概念。

## 如何设定

方法就是在项目页的`Settings`的`Secrets`中的`New Repository Secret`添加：

![](assets/img/2022-01-06-11-48-25.png)

调用方式是使用下面语句

```yaml
echo ${{ secrets.VAR }}
```