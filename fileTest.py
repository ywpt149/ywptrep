#-*- coding:utf8 -*-
__author__ = 'hly'
import sys,socket,threading,os
import yaml
def _load_file(path):
        fh = open(path, 'r')
        data = yaml.load(fh)
        fh.close()
        return data

#得到当前文件的路径
def get_default_config_path():
        #表示代码本身文件路径
        f = sys.argv[0]
        return f

#得到当前文件所在的目录
def get_appdir(f):
    return os.path.dirname(os.path.realpath(f))

#得到当前文件的名字
def get_appname(f):
    filename = os.path.basename(f)
    for i in range(len(filename)-1, -1, -1):
        if filename[i] == '.':
            return filename[0:i]
    return filename

f=get_default_config_path()+'\n'
appdir=get_appdir(f)
appname=get_appname(f)

print f,appdir,'\n',appname

data=_load_file('%s/app.conf'%appdir)

print data,'\n',data["udp_server_host"]