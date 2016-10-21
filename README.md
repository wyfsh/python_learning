# Python Learning

## 安装

* 比较简单的方法是直接装上Vizard软件（它应该会默认帮你一起装Python，但由于我当时是先装的Python，所以不是特别肯定）
* 另一种保险的方法是先单独装一遍Python，再装一遍Vizard

>     注意：新版的Mac系统都自带Python

### Vizard

Vizard的官网下载地址：http://www.worldviz.com/virtual-reality-software-downloads/

需要在上面选择对应自己的机型（好像没有mac客户端，mac的同学可以尝试一下能不能装windows版的。不能的话，实验室面谈时再想办法...）

实验室用的是Vizard4，最新版是Vizard5，根据我的使用经验，两个兼容性还是比较好的，推荐你们在自己的机子上装5，到正式实验前在实验室的机子上调试就行

目前官网下载的话，需要填一个信息收集，然后会收到含有下载链接的邮件。Vizard 5 (64-bit) (5.5) For 64-bit versions of Windows版本的偷懒链接：http://www.worldviz.com/download/vizard.php?p=64

### Python

单独下载Python的官网地址：https://www.python.org/

确保安装的是2.7版本，因为python2和python3差别很大，很多地方不兼容（目前的趋势是开发者都在努力转向python3的兼容，一般使用者都还在用2.7）

<br/>

## 测试

以上步骤搞定之后，可以测试一下Python是否已经成功安装

* 【Windows】打开cmd，输入python，回车，看是否能够成功执行
* 【Mac】（新版的Mac都自带Python）打开terminal终端（这个请自行百度一下，因为我没用过Mac），输入python，回车，看是否能够成功执行

<br/>

## 自学材料

### 教程

这里是网上的几个简单教程，有精力者可以自学一下：（以下按照文章篇幅长度排序）

* [分分钟学会一门语言之Python篇](http://www.code123.cc/1049.html)
* 笨办法学Python
  * [中文版](https://flyouting.gitbooks.io/learn-python-the-hard-way-cn/content/index.html)
  * [英文版](https://learnpythonthehardway.org/book/)
* [廖雪峰的Python 2.7教程](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000)
* [Python基础教程](http://www.runoob.com/python/python-tutorial.html)

### 公开课

* [edX](https://www.edx.org/)上MIT开设的两门课：（不过它们好像也开始教Python3了...）
  * 6.00.1x Introduction to Computer Science and Programming Using Python
  * 6.00.2x Introduction to Computational Thinking and Data Science
* 清华的[学堂在线](https://www.xuetangx.com/)和[edX](https://www.edx.org/)是一个联盟的，说不定会有上述课程的中文版

<br/>

## 笔记&作业

1. 2016/09/29
  * [分分钟学会一门语言之Python篇](http://www.code123.cc/1049.html) 1-230行
    * 注释、基本数据类型、运算符
    * 列表(List)
    * `if....elif....else`判断语句
    * 文章的122-127行似乎有问题，可以先跳过
  * [作业1](https://github.com/wyfsh/python_learning/blob/master/exercises/ex1.md)
    * Due on 2016/10/07 23:59:59
    * 将4个py文件发送到我的邮箱（邮箱地址见群上留言）
  * __Tips__
    * Windows系统的同学可以直接用Vizard软件写代码，Mac系统的同学可以使用IDLE写代码
      * 若以上软件打开以及编译运行等使用方法不清楚的，请先自行在网上搜索（不会搜索的人都不是一个好程序员），实在有问题再在群上提问
      * 进阶同学可以尝试其他更好的IDE，高段位选手选择文本编辑器+命令行的方式
    * 输入可以使用`raw_input()`或`input()`函数（注意二者的区别）
    * 对于有特定格式要求（如小数点后2位、空格间隔…）的输出，可以使用格式化输出方法或是`round()`函数或是`字符串 + ' ' + 字符串`等多种方式
    * `%`用作运算符时，表示取模（求余数），例如：
    ``` python
    29 % 3  # == 2
    ```
    * 注意整数相除、代码层次缩进等重要问题

2. 2016/10/09
  * [分分钟学会一门语言之Python篇](http://www.code123.cc/1049.html) 完结
    * 元组(Tuple)
    * 字典(Dictionary)
    * 集合(Set)
    * `for`循环和`while`循环
    * 异常处理
    * 函数(Function)
    * 类(Class)，略讲，掌握概念
    * 模块导入`import`
  * [Python基础教程 - 文件I/O](http://www.runoob.com/python/python-files-io.html) 刚开始
    * `raw_input()`和`input()`的区别
    * 文件打开
    * 学有余力者请在下节课前预习完上述网页
  * [作业2](https://github.com/wyfsh/python_learning/blob/master/exercises/ex2.md)
    * Due on 2016/10/17 23:59:59
    * 将py文件发送到我的邮箱
    * 参考答案：[题目1](https://github.com/wyfsh/python_learning/blob/master/exercises/ex2_1.py) & [题目2](https://github.com/wyfsh/python_learning/blob/master/exercises/ex2_2.py)

3. 2016/10/21
  * [Python基础教程 - 文件I/O](http://www.runoob.com/python/python-files-io.html)
    * 打开(`open()`)
    * 读写(`read()` & `write()`)
    * 关闭(`close()`)
  * 分析实验室以前代码
    * 导入viz等模块
    * 画面控制
    * 头盔追踪
    * 键盘控制
    * 手柄控制
    * 添置素材
    * 流程控制
    * 记录数据
    * 查看模型、查看坐标等参数

<br/>

## 尾声

短短几次课程无法涵盖有关Python和Vizard的所有内容，在编写程序过程中总会遇到新的问题，需要大家不断地翻阅文档、查询资料，从而在实战中解决实际问题。主要途径包括但不仅限于如下几条：

* Vizard自带的Vizard帮助文档和Python帮助文档
* [Vizard Teacher in a Book](http://www.worldviz.com/virtual-reality-software-documentation/) 有中英版和示例代码（不过多年未更新了...）
* 搜索引擎、各大Python社区
* ...

<br/>

## 反馈

关于本教程的诸项事宜（引用、勘误、建议、扩写、更新失效链接……），可通过Email与作者本人联系。

