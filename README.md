# Python2_My_Flask



#### 运行环境  

目录下执行

```bash
$ sudo apt-get install python-virtualenv  
$ virtualenv -p /usr/bin/python2 venv  
$ . venv/bin/activate 
#执行完会进入虚拟环境，退出虚拟环境输入deactivate  
```

 在虚拟环境执行，安装依赖

```bash
$pip install -r requirements.txt
```

生成和初始化数据库

```bash
$ cd flaskr
$ python initdb.py  #生成数据库 
```

运行WEB

```bash
$ python2 flaskr.py
```

