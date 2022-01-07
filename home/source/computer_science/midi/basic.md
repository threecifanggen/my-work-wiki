# MIDI基础

:::{note}
内容来自[CMU的一个在线教程](https://www.cs.cmu.edu/~music/cmsip/readings/MIDI%20tutorial%20for%20programmers.html)
:::

## MIDI Message

MIDI语言没有定义声音，而是定义了如何用合成器创建声音的指令。

MIMI Message一般是一个或多个字节（8位），第一个字节是STATUS byte，后面一般会跟上一些新增的参数。STATUS byte第7位设定为1，DATA byte第七位设定为0。

|  -   |    STATUS byte    |  DATA byte   |
|:----:|:-----------------:|:------------:|
| 位置 |       开始        | 在STATUS之后 |
| 特征 |     第七位是1     |  第七位是0   |
| 作用 | 决定Message的类型 |              |

### STATUS byte

STATUS byte可能包含MIDI通道(channel)数，可以有16个MIDI通道（从0~15，使用十六进制数）。实践中，音乐家和软件一般是从1开始计数，所以在使用相关软件和程序时要判断是不是从0计数。一个chennel可以控制一个乐器演奏，所以最多可以16个乐器独立演奏。

## NOTE Message

最主要要的message是NOTE ON和NOTE OFF信息。

设定NOTE ON时就是研究者敲击乐器的时候：它包括了参数表示**音高**和**速度**。NOTE OFF则是切换合成器。

NOTE ON结构实例如下：

* STATUS byte: 1001 CCCC (CCCC是MIDI的channel， 从0到15)
* DATA byte 1: 0PPP PPPP (PPP PPP音高， 从0到127，middle C是60)
* DATA byte 2: 0VVV VVVV (VVV VVVV是速度值 从0到127)

    ![](assets/img/2022-01-07-10-43-20.png)

一些精密的合成器里，值也可能带有音质的信息。

NOTE OFF结构如下：

* STATUS byte: 1000 CCCC 
* DATA byte 1: 0PPP PPPP
* DATA byte 2: 0VVV VVVV

## 演奏音符和和弦

![](assets/img/2022-01-07-10-58-18.png)

* t=0 : `0x90` - `0x40` - `0x40` (Start of E3 note, pitch = 64)
* t=0 : `0x90` - `0x43` - `0x40` (Start of G3 note, pitch= 67)
* t=1 : `0x80` - `0x43` - `0x00` (End of G3 note, pitch=67)
* t=1 : `0x90` - `0x45` - `0x40` (Start of A3 note, pitch=69)
* t=2 : `0x80` - `0x45` - `0x00` (End of A3 note, pitch=69)
* t=2 : `0x80` - `0x40` - `0x00` (End of E3 note, pitch=64)
* t=2 : `0x90` - `0x3C` - `0x40` (Start of C3 note, pitch = 60)
* t=2 : `0x90` - `0x47` - `0x40` (Start of B3 note, pitch= 71)
* t=3 : `0x80` - `0x47` - `0x00` (End of B3 note, pitch= 71)
* t=3 : `0x90` - `0x48` - `0x40` (Start of C4 note, pitch= 72)
* t=4 : `0x80` - `0x48` - `0x00` (End of C4 note, pitch= 72)
* t=4 : `0x80` - `0x3C` - `0x40` (End of C3 note, pitch = 60)

## 选择乐器

（待续）