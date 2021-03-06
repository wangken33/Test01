# 算数运算符
# +	加 - 两个对象相加	                                        a + b 输出结果 30
# -	减 - 得到负数或是一个数减去另一个数                     	a - b 输出结果 -10
# *	乘 - 两个数相乘或是返回一个被重复若干次的字符串            	a * b 输出结果 200
# /	除 - x除以y	                                                b / a 输出结果 2
# %	取模 - 返回除法的余数	                                    b % a 输出结果 0
# **	幂 - 返回x的y次幂	                                    a**b 为10的20次方， 输出结果 100000000000000000000
# //	取整除 - 返回商的整数部分	                            9//2 输出结果 4 , 9.0//2.0 输出结果 4.0

# ----------------------------------------------------------------------
# 比较关系运算符
# ==	等于 - 比较对象是否相等	                                    (a == b)返回 False。
# !=	不等于 - 比较两个对象是否不相等	                            (a != b)返回 true.
# <>	不等于 - 比较两个对象是否不相等	                            (a <> b)返回 true。这个运算符类似 != 。
# >	大于 - 返回x是否大于y	                                        (a > b)返回 False。
# <	小于 - 返回x是否小于y。所有比较运算符返回1表示真，返回0表示假。(a < b) 返回 true。
# >=	大于等于	- 返回x是否大于等于y。	                        (a >= b) 返回 False。
# <=	小于等于 -	返回x是否小于等于y。	                        (a <= b) 返回 true。

# ----------------------------------------------------------------------
#赋值运算符
# =	简单的赋值运算符	                        c = a + b 将 a + b 的运算结果赋值为 c
# +=	加法赋值运算符	                            c += a 等效于 c = c + a
# -=	减法赋值运算符	                            c -= a 等效于 c = c - a
# *=	乘法赋值运算符	                            c *= a 等效于 c = c * a
# /=	除法赋值运算符	                            c /= a 等效于 c = c / a
# %=	取模赋值运算符	                            c %= a 等效于 c = c % a
# **=	幂赋值运算符	                            c **= a 等效于 c = c ** a
# //=	取整除赋值运算符	                        c //= a 等效于 c = c // a

# ----------------------------------------------------------------------
#成员运算符
#in  如果在指定的序列中找到值返回 True，否则返回 False。
#not in 如果在指定的序列中没有找到值返回 True，否则返回 False

# a = 10
# b = 20
# list = [1,2,3,4,5,6]
#
# if(a in list):
#     print('YES')
# else:
#     print('NO')
#
# if(b not in list):
#     print('NO')
# else:
#     print('YES')

# ----------------------------------------------------------------------
#身份运算符
# is  是判断两个标识符是不是引用自一个对象, 如果引用的是同一个对象则返回 True，否则返回 False
# is not  是判断两个标识符是不是引用自不同对象,如果引用的不是同一个对象则返回结果 True，否则返回 False。

# a = 123123123
# b = 123123123
# if (a is b):
#     print ('a 和 b 有相同的标识')
#     print (a is b)
# else:
#     print ('a 和 b 没有相同的标识')

# if (a is not b):
#     print ('a 和 b 没有相同的标识')
# else:
#     print ('a 和 b 有相同的标识')

# b = 30
# if (a is b):
#     print ("a 和 b 有相同的标识")
# else:
#     print ("a 和 b 没有相同的标识")
#
# if (a is not b):
#     print ("a 和 b 没有相同的标识")
# else:
#     print ("a 和 b 有相同的标识")

