#条件语句

#例1：if 基本用法
# flag = False
# name = 'luren'
# if name == 'python':
#     flag = True
#     print ('welcome')
# else:
#     print (name)

# num = 4
# if num == 1:
#     print (1)
# elif num == 2:
#     print (2)
# elif num == 3:
#     print (3)
# else:
#     print ('other')

# -------------------------   python 并不支持 switch 语句   -------------------------

num = 9
if num >= 0 and num <= 10:  # 判断值是否在0~10之间
    print ('hello')

num = 10
if num < 0 or num > 10:  # 判断值是否在小于0或大于10
    print ('hello')
else:
    print ('undefine')

num = 8
if (num >= 0 and num <= 5) or (num >= 10 and num <= 15):    # 判断值是否在0~5或者10~15之间
    print ('hello')
else:
    print ('undefine')