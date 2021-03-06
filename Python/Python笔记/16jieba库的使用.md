jieba库是一款优秀的 Python 第三方中文分词库，jieba 支持三种分词模式：精确模式、全模式和搜索引擎模式，下面是三种模式的特点。

==精确模式：==试图将语句最精确的切分，不存在冗余数据，适合做文本分析

==全模式：==将语句中所有可能是词的词语都切分出来，速度很快，但是存在冗余数据

==搜索引擎模式：==在精确模式的基础上，对长词再次进行切分

# **jieba库函数的使用**

| 函数                       | 描述                                                         |
| -------------------------- | ------------------------------------------------------------ |
| jieba.lcut(s)              | **精确模式，返回一个列表类型的分词结果**<br/>\>>>jieba.lcut(“中国是一个伟大的国家”)<br/>[‘中国’，‘是’，‘一个’，’伟大‘，’的‘，’国家‘] |
| jieba.lcut(s,cut_all=True) | **全模式，返回一个列表类型的分词结果，存在冗余。**                                         >>>jieba.lcut(“中国是一个伟大的国家”)                                                                                [‘中国’，‘国是’，‘一个’，’伟大‘，’的‘，’国家‘] |
| jieba.lcut_for_search(s)   | **搜索引擎模式，返回一个列表类型的分词结果，存在冗余。** >>>jieba.lcut_for_search(“中华人民共和国是伟大的”)                                                          [‘中华’，‘华人’，’人民‘，’共和‘，’共和国‘，’中华人民共和国‘，’是‘，’伟大‘，’的‘] |
| jieba.add_word(w)          | **向分词词典增加新词w**                                         >>>jieba.add_word(“蟒蛇语言”) |

