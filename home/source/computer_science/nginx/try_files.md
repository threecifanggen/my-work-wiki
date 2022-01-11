# Try_files

::: {important}
`try_files`可以实现单页应用都导回到`index.html`中。
:::

在编写玩`ELM`实现的SPA应用时，点击`index.html`上的链接可以实现单页效果。而直接访问链接，就找不到任何地址，方法就是通过`try_files`都导回到`index.html`中。

```nginx
location / {
    try_files $uri $uri/ /index.html;
}
```
