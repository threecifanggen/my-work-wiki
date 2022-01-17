# 语音/Podcast相关数据分析

## 简介

语音/Podcast的分析，主要包含的内容包括：

1. 基于音频属性，例如音质；
2. 基于说话方式，诸如真空时间，语调（音高）等；
3. 基于说话内容，这个术语NLP范畴，包括语助词（是否赘词过多），积极与否等。

## 细类

* Transcription(转义为文字)，常用工具有：

    1. [Azure Cognitive Services](https://azure.microsoft.com/en-us/services/cognitive-services/#overview)
    2. [pocketsphinx](https://pypi.org/project/pocketsphinx/)

* 音频分析，常用的工具

    1. [Dolby IO](https://docs.dolby.io/media-apis/docs/analyze-api-guide)

* 通用工具：
    1. [pyAudioAnalysis](https://github.com/tyiannak/pyAudioAnalysis)

## 参考内容

1. [Unlocking More From Your Audio Data - Braden Riggs | PyData Global 2021](https://www.youtube.com/watch?v=n47Cphwo0U4&list=PL5zN-u5VImeBzsvpT3knoA3RYOJkrhtQ9&index=4&t=3938s)
2. [GitHub - Briggs599 / Awesome-audio](https://github.com/Briggs599/awesome-audio)
3. [pyAudioAnalysis](https://github.com/tyiannak/pyAudioAnalysis)

```{toctree}
---
maxdepth: 1
---

pyaudioanalysis_feature
```