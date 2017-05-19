# Anime
 采集Bilibili上的番剧信息存放在Mongodb，统计各项信息在前端使用Highcharts展示。
 
 （爬取ACFun动漫文化栏目文章有待更新）
 
 
 
 环境 | 版本
---|---
操作系统 | Windows 10 Enterprise (x64)
数据库 | MongoDB 3.4.4
开发语言 | Python 3.5.3
后端框架 | Django 1.11
前端框架 | Semantic UI 2.2.10
IDE | PyCharm 2017.1 x64

爬虫文件见tools（channel_extracing.py、page_parsing、clean_data.py、download.py）。
 

## 使用方法
1、安装MongoDB数据库。

2、安装环境依赖包（不同版本操作系统安装方法有差异，见网上具体解决方案）：<pre><code>pip install -r requirements.txt</code></pre>

3、运行爬虫程序(tools目录)爬取数据。

4、项目目录下运行：<pre><code>python manage.py runserver</code></pre>      

5、浏览器下访问：<pre><code>127.0.0.1:8000</code></pre>
 
 
## 运行效果
 由于展示需要爬取大量数据，为方便大家查看贴上本地运行效果图片：
 
 
![Alt text](https://github.com/yipwinghong/Anime/blob/master/Screenshots/1.png)
![Alt text](https://github.com/yipwinghong/Anime/blob/master/Screenshots/2.png)
![Alt text](https://github.com/yipwinghong/Anime/blob/master/Screenshots/3.png)
