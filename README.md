# 3119009472
基于python jieba的论文查重程序
***
| 这个作业属于哪个课程 | [计科国际班软工](https://edu.cnblogs.com/campus/gdgy/Internationalcourseincomputationalscienceandtechnology) </center>|
| ----------------- |--------------- |
| 这个作业要求在哪里| <center>[作业要求](https://edu.cnblogs.com/campus/gdgy/Internationalcourseincomputationalscienceandtechnology/homework/12187)</center>|
| 这个作业的目标 | 编写论文查重程序 </center>|
***
**1.github仓库：https://github.com/yyya77/3119009472**
***
**2.PSP表格：**
|PSP2.1  |Personal Software Process Stages |预估耗时（分钟）|实际耗时（分钟）|
| ----------------- |--------------- |----------------- |--------------- |
| Planning|计划 |10|10|
|· Estimate |· 估计这个任务需要多少时间  |10|10|
|Development |开发 |540|680|
| · Analysis| · 需求分析 (包括学习新技术) |60|90|
| · Design Spec| · 生成设计文档|30|60|
|· Design Review | · 设计复审 |30|40|
|· Coding Standard | · 代码规范 (为目前的开发制定合适的规范)|10|10|
|· Design | · 具体设计 |60|80|
| · Coding|· 具体编码 |300|360|
|· Code Review | · 代码复审 |30|40|
| · Test|· 测试（自我测试，修改代码，提交修改） |20|60|
| Reporting|报告  |50|75|
|· Test Repor |· 测试报告  |20|30|
| · Size Measurement| · 计算工作量 |10|15|
|· Postmortem & Process Improvement Plan | · 事后总结, 并提出过程改进计划 |20|30|
|Sum up | 合计 |600|765|
***
**3.计算模块接口的设计与实现过程:**
算法分析：
基于Python jieba分词的汉明距离进行文本相似度分析
整体思想如下：

<img src="https://img2020.cnblogs.com/blog/2526458/202109/2526458-20210916131526933-953950760.png" width="40%" alt=""/>

关于simhash可参照：
[浅谈simhash及其python实现](https://blog.csdn.net/madujin/article/details/53152619?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-5.no_search_link&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-5.no_search_link)

原理：
simhash是一种局部敏感hash。我们都知道什么是hash。那什么叫局部敏感呢，假定A、B具有一定的相似性，在hash之后，仍然能保持这种相似性，就称之为局部敏感hash。
在上文中，我们得到一个文档的关键词，取得一篇文章关键词集合，又会降低对比效率，我们可以通过hash的方法，把上述得到的关键词集合hash成一串二进制，这样我们直接对比二进制数，看其相似性就可以得到两篇文档的相似性，在查看相似性的时候我们采用海明距离，即在对比二进制的时候，我们看其有多少位不同，就称海明距离为多少。在这里，我是将文章simhash得到一串64位的二进制，一般取海明距离为3作为阈值，即在64位二进制中，只有三位不同，我们就认为两个文档是相似的。当然了，这里可以根据自己的需求来设置阈值。
就这样，我们把一篇文档用一个二进制代表了，也就是把一个文档hash之后得到一串二进制数的算法，称这个hash为simhash。

<img src="https://img2020.cnblogs.com/blog/2526458/202109/2526458-20210916132559588-938449437.png" width="60%" alt=""/>

由此取权重最高的多个值求出两篇文章的simhash值再进行比较得到汉明距离，最后通过汉明距离求得两文件的相似度。

