# get_chinese_from_file
程序功能：从GB2312编码的文件里面提取出中文，方便做嵌入式字体
设计初衷: 解决手工处理老项目里面的中文工作量大且容易出错问题
程序依赖：需安装python, 实测python2.7
使用方法：python getzh.py a.c b.c

值得说明的是，后面跟的文件可以是无数多个, 程序执行后会输出为gb2312.txt
和utf8.txt,分别对应两种不同编码的文件。

程序提取中文后并没有去重复，配合如下网友的工具可以完美去重并生成字体：
	http://www.armbbs.cn/forum.php?mod=viewthread&tid=87428

如果觉得工具好用，请start, 如果有更好的实现，帮忙comments， 谢谢！

BRs
Wufeng
