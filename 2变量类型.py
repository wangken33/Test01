#变量赋值
counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串
#print (counter)
#print (miles)
#print (name)

#----------------------------------------------------------------------
#多个变量赋值
#a = b = c = 1
#a=1;b=2;c='eee'
a,b,c = 1,2,'eee'
#print(a)
#print(b)
#print(c)
#print(a,b,c)

#----------------------------------------------------------------------
#标准数据类型
#Numbers（数字）
#String（字符串）
#List（列表）
#Tuple（元组）
#Dictionary（字典）

#----------------------------------------------------------------------
#删除对象的引用
var1 = 1
var2 = '10'
del var2
#print(var1,var2)
#print(var1)

#----------------------------------------------------------------------
#Python 数字
#int（有符号整型）
#long（长整型[也可以代表八进制和十六进制]）
#float（浮点型）
#complex（复数）
#长整型也可以使用小写 l，但是还是建议您使用大写 L，避免与数字 1 混淆。Python使用 L 来显示长整型。

#----------------------------------------------------------------------
#Python 字符串
testStr = 'Hello World!'
#print(testStr[0])           #输出字符串中的第一个字符
#print(testStr[2:5])         #输出字符串中第三个至第五个之间的字符串
#print(testStr[2:])          #输出从第三个字符开始的所有字符串
#print(testStr * 2)          #输出字符串两次
#print(testStr + 'test')    #输出连接的字符串

#----------------------------------------------------------------------
#Python 列表
list = ['runoob', 786, 2.3, 'join', 89.0]
tinylist = [123, 'join']
#print(list)             #输出完整列表
#print(list[0])          #输出列表的第一个元素
#print(list[1:3])        #输出第二个至第三个元素
#print(list[2:])         #输出从第三个开始至列表末尾的所有元素
#print(tinylist * 2)     #输出列表两次
#print(list + tinylist)  #输出组合的列表
#tinylist.append('test')
#print(tinylist)

#----------------------------------------------------------------------
#Python 元组
#元组是另一个数据类型，类似于List（列表）。
#元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
tuple = ('runoob', 786, 2.3, 'join', 89.0)
tinytuple = (123, 'join')
#print(tuple)
#print(tuple[0])
#print(tuple[1:3])
#print(tuple[2:])
#print(tuple * 2)
#print(tuple + tinytuple)

#----------------------------------------------------------------------
#Python 字典
dict = {}
dict['one'] = 'this is one'
dict[2] = 'this is two'
tinydict={'name': 'john','code':6734, 'dept': 'sales'}

# print(dict['one'])
# print(dict[2])
# print(dict)
# print(tinydict)
# print(dict.keys())
# print(dict.values())

#----------------------------------------------------------------------
#Python 数据类型转换
testIntValue = 1.00000
testIntValue = int(testIntValue)
# print(testIntValue)

# 函数
# int(x [,base])
# 将x转换为一个整数
# long(x [,base] )
# 将x转换为一个长整数
# float(x)
# 将x转换到一个浮点数
# complex(real [,imag])
# 创建一个复数
# str(x)
# 将对象 x 转换为字符串
# repr(x)
# 将对象 x 转换为表达式字符串
# eval(str)
# 用来计算在字符串中的有效Python表达式,并返回一个对象
# tuple(s)
# 将序列 s 转换为一个元组
# list(s)
# 将序列 s 转换为一个列表
# set(s)
# 转换为可变集合
# dict(d)
# 创建一个字典。d 必须是一个序列 (key,value)元组。
# frozenset(s)
# 转换为不可变集合
# chr(x)
# 将一个整数转换为一个字符
# unichr(x)
# 将一个整数转换为Unicode字符
# ord(x)
# 将一个字符转换为它的整数值
# hex(x)
# 将一个整数转换为一个十六进制字符串
# oct(x)
# 将一个整数转换为一个八进制字符串


#----------------------------------------------------------------------
#获取数据类型  type()用来获取数据类型
intTest = 4
# print(type(intTest))
strTest = 'abc'
# print(type(strTest))

#通过 isinstance 来判断数据类型
# print(isinstance(intTest,int))
# print(isinstance(intTest,str))
# print(isinstance(strTest, int))
# print(isinstance(strTest, str))
# print(isinstance(intTest,(str, int, float)))
# print(isinstance(intTest,(str, float)))

#通过 isinstance 来判断一个对象是否是一个类的实例的函数
class A:
    pass

class B(A):
    pass

# instDemo = A()
# print(isinstance(instDemo, A))
# print(isinstance(instDemo, B))

# type主要用于获取未知变量的类型，type()不会认为子类是一种父类类型。
# isinstance主要用于判断A类是否继承于B类，isinstance()会认为子类是一种父类类型。
print(type(A()) == A)
print(isinstance(A(), A))
print(type(B()) == A)
print(isinstance(B(), A))




