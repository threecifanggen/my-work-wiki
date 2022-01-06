# 如何复用GitHub Actions

## 一个完整的复用`workflows`

```yaml
on:
  workflow_call:
    inputs:
      username:
        required: true
        type: string
    secrets:
      envPAT:
        required: true
```

### 监听事件为`workflow_call`

监听事件不在为`pull_request`或者`push`之类的内容，而是`workflow_call`，即

```yaml
on:
    workflow_call:
```
### 参数使用`inputs`

```yaml
inputts:
    username:
        required: true # 是否是必填
        type: string # 属性
```

### 加密变量

加密变量调用声明需要使用`secrets`：

```yaml
scretes:
    envPAT: # 加密变量名
        required: true #是否必填
```

## 如何使用

通过`uses`关键字指定目录来使用，是`steps`中可选的一种（`steps`仅支持`uses/with`和`name/run`两种语句）。使用`with`来指定参数：

```yaml
jobs:
  reusable_workflow_job:
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: ./.github/actions/my-action@v1
        with:
          username: ${{ inputs.username }}
          token: ${{ secrets.envPAT }}
```

使用[加密变量](./secrets.md)的例子：

```yaml
jobs:
  call-workflow-passing-data:
    uses: octo-org/example-repo/.github/workflows/reusable-workflow.yml@main
    with:
      username: mona
    secrets:
      envPAT: ${{ secrets.envPAT }}
```