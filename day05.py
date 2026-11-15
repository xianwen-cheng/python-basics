import math

def quadratic(a, b, c):
    x =( -b + math.sqrt(b*b-4*a*c))/(2*a)
    y =( -b - math.sqrt(b*b-4*a*c))/(2*a)
    return x,y

# 测试:
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5, 3))

def fib(n):
    a,b=0,1
    result = []
    while a<n:
        print(a,end=" ")
        result.append(a)
        a,b=b,a+b
    return result

fib(1000)
print(fib(1000))
    