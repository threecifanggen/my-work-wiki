# 使用缓存提速

一些可以提高速度的cache可以帮助快速进行测试搭建，`Python`可以通过[这个项目](https://github.com/actions/setup-python)得到。

下面是一个demo例子：

```yaml
name: Caching with npm

on: push

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2

      - name: Cache node modules
        uses: actions/cache@v2
        env:
          cache-name: cache-node-modules
        with:
          # npm cache files are stored in `~/.npm` on Linux/macOS
          path: ~/.npm
          key: ${{ runner.os }}-build-${{ env.cache-name }}-${{ hashFiles('**/package-lock.json') }}
          restore-keys: |
            ${{ runner.os }}-build-${{ env.cache-name }}-
            ${{ runner.os }}-build-
            ${{ runner.os }}-

      - name: Install Dependencies
        run: npm install

      - name: Build
        run: npm build

      - name: Test
        run: npm test
```

下面是一个`Python`多版本测试的例子：

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        # in this example, there is a newer version already installed, 3.7.7, so the older version will be downloaded
        python-version: ['3.7.4', '3.8', '3.9', '3.10']
    steps:
    - uses: actions/checkout@v2
    - uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}
    - run: python my_script.py
```