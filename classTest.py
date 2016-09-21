# -*- coding:utf-8 -*-
__author__ = 'hly'

class MyDict(object):

    def __init__(self):

        print'call fun __init__'

        self.item = {}
        self.ii={}
        self.d=1

    def __getitem__(self,key):

        print'call fun __getItem__'

        return self.item.get(key)

    def __setitem__(self,key,value):

        print'call fun __setItem__'

        self.item[key] =value

    def __delitem__(self,key):

        print'cal fun __delitem__'

        del self.item[key]

    def __len__(self):

        return len(self.item)

    #找不到类中的属性时，就会去调用此函数
    def __getattr__(self,key):
        print '__getattr__'
        return self.item.get(key, None)
    #当定义属性值时，会调用此函数
    def __setattr__(self, key, value):
        print '__setattr__'
        self.__dict__[key]=value
myDict=MyDict()
myDict.b=85
print myDict.b
# myDict = MyDict()
# print myDict.item
# myDict['a']=11
# myDict.b=4
# print myDict['a']
#
# myDict[2] ='ch'
#
# myDict['hobb'] = 'sing'
#
# print myDict[2]
#
# print myDict.item
#
# del myDict[2]
#
# print myDict.item
#
# print len(myDict)