# `pyAudioAnaysis`中的一些特征的作用分析

## Zero Crossing Rate

是判断信号变化率的，作用应该是判断音频的音量的起伏。可能可以用来判断说话的**戏剧性**。

## Energy

是信号值的平方和。这个可以直接表明音量大小。

## Entropy of Energy

归一化后的小frame内的熵。可以用来测量突然的变化。

## Spectral Centroid

```{seealso}
有相关的[维基](https://en.wikipedia.org/wiki/Spectral_centroid)介绍。
```

光谱的重力中心（？, the center of gravity of the spectrum）。判断谱的中心，WIKI上描述可以判断声音的亮度（Brightness）。

## Spectral Spread

频扩表示背离光谱中心的程度。

## Spread Entropy

## Spread Flux

## Spread Rolloff

## MFCC

MFCC(Mel Frequency Cepstral Coefficients)。

## Chroma Vector

## Chroma Deviation