def is_valid_identifier(name):
    try:
        exec(f"{name} = None")
        return True
    except:
        return False

print(is_valid_identifier("MAX-ONE"))

print("hello,python") #这是注释
'''这也是注释'''
"""这还是注释"""

item_one = 1
item_two = 2
item_three = 3
total = item_one \
        +  item_two + \
        item_three
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
print(total)

word = '字符串'
sentence = "这是一个句子"
paragrafh = """这是一个段落
可由多行构成"""

agc='123456789'

print(agc)
print(agc[0:-1])    #输出第一个到倒数第二个
print(agc[0])       #输出第一个
'''print(str[2:5])     #第三个到第六个
print(str[2:])      #第三个往后
print(str[0:-1:2])
print(str*2)        #输两遍
'''
print(agc+'你好')

print('----------------------------------')

print('hello\nrunoob')
print(r'hello\nrunoob')

import sys; x = 'runoob'; sys.stdout.write(x + '\n')

x = "a"
y = "b"

print( x )
print( y )

print('---------------------------')

print( x, end=" ")
print( y, end=" ")
print()

import sys
print('========================Python import mode================================')
print('命令行参数为：')
for i in sys.argv:
    print(i)
print('\n python路径为',sys.path)

from sys import argv,path

print('=======================Python from import====================')
print('path:',path)


for i in range(3):
    print(i)

print(type(True))


