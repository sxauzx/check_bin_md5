# check_bin_md5
python脚本检查服务器敏感文件
1、将两个文件放到自己定义的目录下，生成的数据库也会在对应的目录下
2、根据自己需求将敏感的路径配置到urls列表中
3、第一次运行filesystem.py生成自己的初始化数据库
4、讲filesystem.py中的邮箱换成自己的
5、定时任务执行check_md5.py进行检查，有异常会收到异常邮件，正常收到的邮件则为空

#v0.2
将urls列表指定的路径改为指定目录，，然后递归遍历所有子目录