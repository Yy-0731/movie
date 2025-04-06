# movie
基于大数据的电影分析系统
一直想做一款管理系统，看了很多优秀的开源项目但是发现没有合适的。于是利用空闲休息时间开始自己写了一套管理系统。现将部分源码开源

演示地址
https://github.com/Yy-0731/movie/edit/main/README.md

项目简介
该项目是基于python的web类库django开发的一套web网站。 本人的研究方向是一项关于搜索的研究项目。在该项目中，笔者开发了一个简单版的搜索网站，实现了对数据库数据的检索和更新。通过开发该项目，笔者学习和巩固了python的相关技术和框架。

运行步骤
下载代码后，进入到bt目录下
新建数据库，并修改settings.py中的数据库配置
移植sql数据，执行 python manage.py migrate
运行项目，执行 python manage.py runserver
