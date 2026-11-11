counter = 100
mils = 1000.0
name = "runoob"

print(counter, type(counter), '\n', name,type(name),'\n', mils, type(mils),)

a, b, c = 1,2,"runoob"

x=10
y=3.14
name = "Alice"
is_active=True

print(name[0:-1])
print(type(name))

h = 10 + True
print(h)

var = 1
var2 = 2
del var,var2

#布尔类型的值与类型
a = True
b = False
print(type(a))
print(type(b))

print(int(True))
print(int(False))

print(bool(0))
print(bool("python"))
print(bool([]))
print(bool([1314]))

print(True and False)
print(True or False)
print(not True)

if True:
    print("This will always print")

if not False:
    print("This will also always print")

print(int(not True))

x = 10
if x:
    print("x是非零值")

my_list = ['abcd','678',2.34,'runoob',70.2]
tinylist = [123,'runoob']

print(my_list)
print(my_list[0])
print(my_list[1:3])
print(tinylist*2)
print(my_list+tinylist)

k = [1,2,3,4,5,6,7,8,9]
k[0] = 9
k[2:5] = [13, 26, 29]
print(k)
k[2:5] = []
print(k)

def reverseWords(input):

    inputWords = input.split(" ")

    inputWords = inputWords[-1: :-1]

    output = ' '.join(inputWords)

    return output

'''
if __name__ == "__main__":
    input = 'major invest balance outcome'
    rw = reverseWords(input)
    print(rw)
'''

my_tuple = ('asd', 6788, 2.35, 'runoob', 70.2)
tinytuple = (124, 'runoob')

print(my_tuple)
print(tinytuple*2)

tup1 = ()
tup2 = (20,)
not_a_tuple = (42)
print(tup1)
print(tup2)
print(not_a_tuple)
print(tup2*2)

sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}

print(sites)

if 'Runoob' in sites:
    print('Runoob在集合中')
else:
    print('Runoob不在')

a = set('asdfghad')
b = set('alkjhg')

print(a)
print(a-b)
print(a|b)
print(a&b)
print(a^b)

my_dict = {}
my_dict['one'] = "1 - 菜鸟教程？？"
my_dict[2] = "2 - 菜鸟教程"

tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.qq.cn'}

print(my_dict['one'])
print(my_dict[2])
print(tinydict)
print(tinydict.keys())
print(tinydict.values())
print(tinydict.items())

print(dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)]).keys())

print({x: x**2 for x in (2,4,6)})

print(dict(Runoob = 1, Google = 2, Taobao = 3))

x = b"hello"
print(type(x))
print(x)
print(x[0])

y = bytes("welcom leon", encoding = "utf-8")
print(x+y)

if x[0] == ord("h"):
    print("第一个元素是h")