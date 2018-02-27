# while 循环
# num = 0
# while (num <= 9):
#     print (num)
#     num += 1
# print ('over!!!')

# num = 0
# while (num < 9):
#     num += 1
#     if num >= 6:
#         break   #跳出循环体
#     if num - 2 > 6:
#         continue    #跳出当前循环
#     print(num)
# print ('over!!!')

# ----------------------------------------------------------------------
# while...else 循环
# num = 0;
# while num < 5:
#     print (num, '小于5')
#     num += 1
# else:
#     print (num, '大于或等于5')


# 练习题目----------------------------------------------------------------------
# 练习一：猜大小
# import random
# s = int(random.uniform(1,10))
# print (s)
# m = int(input('输出一个数字：'))
#
# while m != s:
#     if m > s:
#         print ('大了')
#         m = int(input('输入一个数字：'))
#     elif m < s:
#         print ('小了')
#         m = int(input('输入一个数字：'))
# else:
#     print ('恭喜猜中')


# 练习二：猜拳
# import random
# num = 1
# while num <= 20:
#     # s = int(random.uniform(1, 3))
#     s = int(random.randint(1, 3))
#     print (s)
#     num += 1

# import random
# computerlist = ['jiandao','shitou','bu']
# while 1:
#     s = int(random.randint(1, 3))
#     if s == 1:
#         ind = 'jiandao'
#     if s == 2:
#         ind = 'shitou'
#     if s == 3:
#         ind = 'bu'
#
#     m = input('please input shitou or jiandao or bu，input \'end\' sign out：')
#
#     if ((m != 'end') and (m not in computerlist)):
#         print ('input error,please again input!')
#         continue
#     elif m == 'end':
#         print ('sign out game!')
#         break
#     elif ((m == 'jiandao' and ind == 'jiandao') or (m == 'shitou' and ind == 'shitou') or (m == 'bu' and ind == 'bu')):
#         print ('computer is ' + ind + '，ping ju!')
#         continue
#     elif ((m == 'jiandao' and ind == 'bu') or (m == 'shitou' and ind == 'jiandao') or (m == 'bu' and ind == 'shitou')):
#         print ('computer is ' + ind + '，you are win!')
#         continue
#     elif ((m == 'jiandao' and ind == 'shitou') or (m == 'shitou' and ind == 'bu') or (m == 'bu' and ind == 'jiandao')):
#         print ('computer is ' + ind + '，you are fail!')
#         continue



# 练习三：九九乘法表
rownum = 1

while rownum < 10:

    firstnum = 1
    str = ''

    while firstnum <= rownum:
        if firstnum != rownum:
            str = "%s%s*%s=%s,"%(str,firstnum,rownum,firstnum * rownum)
        else:
            str = "%s%s*%s=%s" % (str, firstnum, rownum, firstnum * rownum)
        firstnum += 1

    print(str)
    rownum += 1


























