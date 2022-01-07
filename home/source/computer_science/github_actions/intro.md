# GitHub Actions学习笔记

通过GitHub Actions，希望接触一些`CI/CD`相关的内容，并且加速我的开源程序`fppy-learn`的开发部署。

## 基本用法

基本用法如下，steps中只能有`name/run`语句或`uses/with`语句：

```yaml
jobs:
  example-job: # 任务名
      steps: ## 步骤
        - name: Upload output file # 名字会在Actions里面显示
            uses: actions/upload-artifact@v2
            with:
            name: output-log-file
            path: output.log
        - name: Connect to PostgreSQL
          run: node client.js
          env: #环境变量
            POSTGRES_HOST: postgres
            POSTGRES_PORT: 5432
```

## 使用多个job

```yaml
jobs:
  setup:
    runs-on: ubuntu-latest
    steps:
      - run: ./setup_server.sh
  build:
    needs: setup
    runs-on: ubuntu-latest
    steps:
      - run: ./build_server.sh
  test:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - run: ./test_server.sh
```

## 多种状态测试

可以测试不同的版本、系统之类

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node: [6, 8, 10]
    steps:
      - uses: actions/setup-node@v2
        with:
          node-version: ${{ matrix.node }}
```

## 使用社区贡献的可复用的例子

可以在专门的[GitHub Actions](https://github.com/marketplace?type=actions)市场找到一些社区贡献的Actions代码，使用`uses/with`语句即可。

:::{toctree}
:maxdepth: 1

reuses
secrets
cache
:::